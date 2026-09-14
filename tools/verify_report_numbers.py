"""Recompute the numbers quoted in the write-up from the CSV files in this repository.

Standard library only. Run from the repository root:

    python tools/verify_report_numbers.py

Every check prints PASS or FAIL together with the value computed from the data and the
expected value: the number printed in the write-up, a property the write-up states, or — for the
per-cell checks of Figure 5 — the win rate stored in the CSV, recomputed from wins and losses.
"""
import csv
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
failures = 0


def rows(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def check(label, computed, expected, tol=0.05):
    global failures
    ok = abs(float(computed) - float(expected)) <= tol
    failures += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {label}: data = {computed}, expected = {expected}")


def mean(v):
    return sum(v) / len(v)


def win_rate(wins, losses):
    """Win rate in percent; undecided games are excluded from the denominator."""
    return 100 * int(wins) / (int(wins) + int(losses))


# Section 1 / Section 4: final result and Table 2
fr = {r["metric"]: r["value"] for r in rows("results/ladder/final_result.csv")}
check("Final rank", fr["final_rank"], 26, 0)
check("Teams", fr["total_teams"], 6807, 0)
check("Final score", fr["final_score"], 1123.7, 0)
t2 = rows("results/ladder/results_by_matchup.csv")
g = sum(int(r["games"]) for r in t2)
w = sum(int(r["wins"]) for r in t2)
l = sum(int(r["losses"]) for r in t2)
check("Table 2 games", g, 1330, 0)
check("Table 2 wins", w, 781, 0)
check("Table 2 losses", l, 549, 0)
check("Table 2 win rate (%)", round(win_rate(w, l), 1), 58.7, 0)
for r, expected in zip(t2, [45.4, 60.6, 55.1, 62.3, 65.7, 77.2, 77.3, 66.8]):
    check(f"Table 2 {r['opponent_deck']} win rate (%)", round(win_rate(r["wins"], r["losses"]), 1), expected, 0)
losing = [r["opponent_deck"] for r in t2 if int(r["wins"]) < int(r["losses"])]
check("Table 2 matchups with a losing record (Dragapult ex only)", len(losing), 1, 0)

# Section 2: deck
deck = rows("configs/deck.csv")
check("Deck size", sum(int(r["count"]) for r in deck), 60, 0)

# Section 3: models
models = rows("manifests/models.csv")
check("Number of policies", len(models), 8, 0)
check("Parameters per policy (millions)", round(int(models[0]["parameters"]) / 1e6, 2), 0.83, 0)
check("Card token dimensions", models[0]["card_token_dim"], 122, 0)
check("Game dimensions", models[0]["game_dim"], 45, 0)
check("Option dimensions", models[0]["option_dim"], 54, 0)
st = json.load(open(os.path.join(ROOT, "configs/switch_table.json"), encoding="utf-8"))
check("Specialist slots (1 generalist + 7 specialists)", st["specialist_slot_count"], 7, 0)

# Section 4: RL with the lethal detector (Figure 4)
cp = rows("results/lethal_aware_rl/win_rate_by_checkpoint.csv")


def arm_mean(arm, it):
    return mean([float(r["win_rate_pct"]) for r in cp if r["arm"] == arm and r["iteration"] == str(it)])


check("Held-out opponents", min(int(r["opponents"]) for r in cp), 12, 0)
check("Seeds per arm at iteration 300", len([r for r in cp if r["arm"] == "with_detector" and r["iteration"] == "300"]), 3, 0)
check("Figure 4 shared start (%)", round(arm_mean("shared_start", 0), 1), 45.8)
for it, on, off in [(100, 52.0, 51.8), (200, 53.5, 52.7), (300, 55.0, 53.6)]:
    check(f"Figure 4 with detector, iteration {it} (%)", round(arm_mean("with_detector", it), 1), on)
    check(f"Figure 4 without detector, iteration {it} (%)", round(arm_mean("without_detector", it), 1), off)
target = arm_mean("without_detector", 300)
lo, hi = arm_mean("with_detector", 200), arm_mean("with_detector", 300)
it_reach = 200 + (target - lo) / (hi - lo) * 100
check("Iterations to reach the control's final win rate", round(it_reach), 207, 0)
check("Fewer iterations (%)", round(100 * (1 - it_reach / 300)), 31, 0)
sp = rows("results/lethal_aware_rl/sec_per_iteration.csv")
s_on = mean([float(r["sec_per_iter_mean"]) for r in sp if r["arm"] == "with_detector"])
s_off = mean([float(r["sec_per_iter_mean"]) for r in sp if r["arm"] == "without_detector"])
check("Training time added by the detector (%)", round(100 * (s_on / s_off - 1), 1), 3.4)
check("Less wall-clock time (%)", round(100 * (1 - it_reach * s_on / (300 * s_off))), 29, 0)
pw = rows("results/lethal_aware_rl/provable_win_positions.csv")
on_rates = [float(r["rate_pct"]) for r in pw if r["arm"] == "with_detector"]
off_rates = [float(r["rate_pct"]) for r in pw if r["arm"] == "without_detector"]
check("Every detector-trained seed reaches provable-win positions more often than every control seed",
      int(min(on_rates) > max(off_rates)), 1, 0)

# Section 4: matchup specialists (Figure 5)
mw = rows("results/specialists/matchup_win_rates.csv")
check("Matchups", len(mw), 12, 0)
check("Every generalist cell has 1,000 games", int(all(r["generalist_games"] == "1000" for r in mw)), 1, 0)
check("Every assigned-policy cell has 1,000 games", int(all(r["assigned_games"] == "1000" for r in mw)), 1, 0)
for r in mw:
    check(f"Figure 5 generalist vs {r['opponent_deck']} (%)",
          round(win_rate(r["generalist_wins"], r["generalist_losses"]), 1), r["generalist_win_rate_pct"], 0)
    check(f"Figure 5 assigned policy vs {r['opponent_deck']} (%)",
          round(win_rate(r["assigned_wins"], r["assigned_losses"]), 1), r["assigned_win_rate_pct"], 0)
check("Generalist average win rate (%)", round(mean([float(r["generalist_win_rate_pct"]) for r in mw]), 1), 48.9)
check("Eight models used selectively, average win rate (%)",
      round(mean([float(r["assigned_win_rate_pct"]) for r in mw]), 1), 63.9)
ri = rows("results/specialists/router_identification.csv")
check("Incorrect switches", sum(int(r["incorrect_switches"]) for r in ri), 0, 0)

# Section 4: human feedback (Figure 6)
rb = rows("results/rabsca/rabsca_vs_dragapult.csv")
first, last = rb[0], rb[-1]
check("Figure 6 first win rate (%)", first["win_rate_pct"], 20.0)
check("Figure 6 last win rate (%)", last["win_rate_pct"], 55.6)
check("Win rate against Dragapult ex over the full range (x)",
      round(float(last["win_rate_pct"]) / float(first["win_rate_pct"]), 1), 2.8)
check("Figure 6 training games at the last point (millions)", round(int(last["training_games_vs_dragapult"]) / 1e6, 1), 1.2)

print()
print("all checks passed" if failures == 0 else f"{failures} check(s) failed")
sys.exit(1 if failures else 0)
