# The deck

## Festival Lead

We chose a deck built around **Festival Lead**. While the Stadium **Festival Grounds** is in play,
Pokémon with the Festival Lead Ability — such as **Dipplin** — can use two attacks in a single turn.
If the first attack Knocks Out the opponent's Active Pokémon, the Pokémon may attack again after the
opponent chooses a new Active Pokémon.

Dipplin's **Do the Wave** deals 20 damage for each of our own Benched Pokémon, so with five Pokémon
on the Bench it deals 100 damage twice, for **200 damage** in total. The basic plan is to hold down the
number of Prize cards the opponent takes by relying mainly on non-ex Pokémon, while knocking out
several Pokémon in one turn to pull ahead in the Prize race. No Pokémon in the deck has a Rule Box
([`configs/deck.csv`](../configs/deck.csv), column `has_rule_box`).

Against opponents built around ex and Mega ex Pokémon, we use the damage boosts from **Black Belt's
Training** (+40) and **Brave Bangle** (+30). Adding them to the base 100 damage gives **170** for one
attack, or up to **340** damage across two attacks. Rather than settling into a long game against
healing and high-HP Pokémon, the concept is to line up the right conditions and take the knockout in a
single turn.

## Why this deck

We chose Festival Lead for its matchups and low usage. We expected favorable matchups against major
decks except Dragapult ex and Archaludon ex. Archaludon ex was uncommon among top teams, while we
expected Rabsca to bring the Dragapult ex matchup to around 50%. Festival Lead decks with Rabsca were
also rare near the top of the leaderboard, suggesting that opponents might have devoted less training
and counterplay to this matchup.

## Key cards

| Card | Role | Reason for inclusion |
|---|---|---|
| Festival Grounds | Dipplin | The core of the non-ex strategy: two attacks per turn create a tempo advantage and improve Prize trades. |
| Rabsca | Dragapult counter | Blocks Phantom Dive's damage-counter placement on the Bench, improving a matchup that can otherwise be unfavorable. |
| Shaymin | Bench protection | Protects against Bench attacks. Included for Grimmsnarl, it also proved useful against Slowking decks. |
| Rillaboom | Cornerstone Mask Ogerpon ex counter | Provides damage against Cornerstone Mask Ogerpon ex, mainly seen in Crustle decks, which blocks damage from Pokémon with Abilities. |
| Black Belt's Training | Damage boost | Two copies improve access on the required turn, helping knock out high-HP or healing-focused Mega ex Pokémon in one turn. |
| Brave Bangle | Damage boost for Pokémon without a Rule Box | Helps non-ex attackers such as Dipplin reach knockout thresholds against ex and Mega ex Pokémon while retaining their favorable Prize trade. |

## Deck list (60 cards)

Card IDs are the competition simulator's IDs. The card text of every card — abilities, attacks and
Trainer effects — is in [`configs/deck.csv`](../configs/deck.csv).

| Count | Card | ID | Kind |
|--:|---|--:|---|
| 1 | Applin | 42 | Pokémon (Basic) |
| 3 | Applin | 149 | Pokémon (Basic) |
| 4 | Dipplin | 93 | Pokémon (Stage 1) |
| 1 | Goldeen | 100 | Pokémon (Basic) |
| 1 | Seaking | 240 | Pokémon (Stage 1) |
| 4 | Grookey | 89 | Pokémon (Basic) |
| 3 | Thwackey | 90 | Pokémon (Stage 1) |
| 1 | Rillaboom | 91 | Pokémon (Stage 2) |
| 1 | Rellor | 73 | Pokémon (Basic) |
| 1 | Rabsca | 74 | Pokémon (Stage 1) |
| 1 | Shaymin | 343 | Pokémon (Basic) |
| 4 | Buddy-Buddy Poffin | 1086 | Item |
| 1 | Secret Box | 1092 | Item |
| 3 | Bug Catching Set | 1094 | Item |
| 2 | Night Stretcher | 1097 | Item |
| 4 | Poké Pad | 1152 | Item |
| 1 | Air Balloon | 1174 | Pokémon Tool |
| 2 | Brave Bangle | 1175 | Pokémon Tool |
| 2 | Boss's Orders | 1182 | Supporter |
| 1 | Lana's Aid | 1184 | Supporter |
| 1 | Kieran | 1191 | Supporter |
| 2 | Black Belt's Training | 1211 | Supporter |
| 4 | Lillie's Determination | 1227 | Supporter |
| 2 | Dawn | 1231 | Supporter |
| 4 | Festival Grounds | 1245 | Stadium |
| 6 | Basic Grass Energy | 1 | Energy |
