# Results — file and column guide

Win rates are percentages of **decided** games: `wins / (wins + losses)`. Undecided games are counted
in `games` but excluded from the win-rate denominator. (Table 2 has no undecided games.)

## `ladder/`

| File | Columns |
|---|---|
| `final_result.csv` | `metric`, `value` — Simulation-track rank, number of teams, final score, games, wins, losses, win rate, and the Kaggle submission reference |
| `results_by_matchup.csv` | `opponent_deck`, `games`, `wins`, `losses`, `win_rate_pct` — Table 2 of the write-up, final evaluation period |

## `lethal_aware_rl/` — Figure 4

The same initial policy trained for 300 iterations with the rule-based lethal detector
(`with_detector`) and without it (`without_detector`), three seeds each, evaluated on 12 held-out
opponents with the detector enabled during evaluation. Seats are alternated, half the games going first.

| File | Columns |
|---|---|
| `win_rate_by_checkpoint.csv` | `arm`, `seed`, `iteration`, `opponents`, `games_per_opponent`, `games_total`, `win_rate_pct` (average of the 12 per-opponent win rates), `win_rate_95ci_low`, `win_rate_95ci_high` |
| `win_rate_by_checkpoint_mean.csv` | `arm`, `iteration`, `seeds`, `mean_win_rate_pct` — the values plotted in Figure 4 |
| `time_to_reach.csv` | the control's iteration-300 win rate, the detector-trained arm's win rate at iterations 200 and 300, the interpolated iteration at which it reaches the control's value, fewer iterations (%), seconds per iteration for each arm, cost per iteration (%), less wall-clock time (%), and the method |
| `sec_per_iteration.csv` | `arm`, `seed`, `iterations`, `games_per_iter`, `sec_per_iter_mean` — timing runs, two seeds per arm |
| `provable_win_positions.csv` | `arm`, `seed`, `iteration`, `opponents`, `games`, `own_turns`, `turns_with_a_provable_win`, `rate_pct` — measured with the detector observing only (actions unchanged) |

## `specialists/` — Figure 5

| File | Columns |
|---|---|
| `matchup_win_rates.csv` | per opponent deck: the generalist's `games` / `wins` / `losses` / `undecided` / `win_rate_pct`, and the same for the policy assigned to that matchup (`assigned_slot`, `assigned_policy`, 95% confidence interval). 1,000 games per cell. For the three matchups played by the generalist (slot a), both columns come from the same 1,000 games |
| `router_identification.csv` | `opponent_deck`, `expected_slot`, `expected_policy`, `games`, `games_switched_to_expected_slot`, `switched_at_turn0_by_mulligan`, `median_switch_turn`, `incorrect_switches` |

## `rabsca/` — Figure 6

| File | Columns |
|---|---|
| `rabsca_vs_dragapult.csv` | `point`, `stage`, `training_games_vs_dragapult` (cumulative), `rabsca_reward` (on/off during that stage's training), `games`, `decided_games`, `win_rate_pct`, `win_rate_95ci_half`, `rabsca_in_play_pct` (games in which Rabsca was put into play), `rabsca_in_play_95ci_half`. Each value combines three Dragapult ex opponent policies with weights 0.4 / 0.3 / 0.3 |
