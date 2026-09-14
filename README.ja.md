# Dawn of the Dipplin: Eight Small Policies, One Big Festival

**Pokémon TCG AI Battle Challenge（2026）** Strategy 部門に提出したレポートの裏付け資料です。

> English: [README.md](README.md)

- Kaggle のレポート: [Dawn of the Dipplin: Eight Small Policies, One Big Festival](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle-challenge-strategy/writeups/new-writeup-1788440804579)
- チーム **perrodawn** — perrodawn, tora, RB25det, Shinzo Takayama
- Simulation 部門: **6,807チーム中26位**、最終スコア **1123.7**

## 概要

Festival Lead デッキ（Dipplin + Thwackey）専用のエージェントを作りました。組み合わせたのは次の5つです。
- ルールベースのエージェントが作った棋譜を教師にした模倣学習（IL）
- リーグ型の強化学習（RL）
- 対面別に特化した強化学習
- 公開情報にもとづく方策の切り替え
- 確実な勝ち筋を探すリーサル探索

計算資源の限られた学生だけのチームなので、大きなモデルを1つ学習する代わりに、**約0.83Mパラメータの方策を8本**（汎用1本・対面特化7本）使い、60枚のデッキ1つを共有させました。

![Figure 1. Our strategy](figures/figure1-strategy.png)

## 主な結果

| | |
|---|---|
| Simulation 部門 | **26位 / 6,807チーム**、最終スコア **1123.7** |
| 最終評価期間 | **1,330戦 781勝549敗（58.7%）** |
| 汎用方策だけ → 8モデルの使い分け（12対面 × 1,000戦） | **48.9% → 63.9%** |
| ルールベースのリーサル検知つき強化学習 | 約 **207 iteration** で対照の最終勝率（53.6%）に到達。iteration は **31%少なく**、実時間は約 **29%短い**。1 iteration あたりの時間は **+3.4%** |
| Dragapult ex 戦での Rabsca のフィードバック | 勝率 **20.0% → 55.6%**、Rabsca を場に出した割合 **8.5% → 62.8%** |

## レポートの裏付け

| レポート | このリポジトリの裏付け |
|---|---|
| §1・§4 — 26位 / 6,807、1123.7、1,330戦 781勝549敗 | [`results/ladder/final_result.csv`](results/ladder/final_result.csv) |
| §4 表2 — 対面別の成績 | [`results/ladder/results_by_matchup.csv`](results/ladder/results_by_matchup.csv) |
| §2 図2 — 60枚のデッキ | [`configs/deck.csv`](configs/deck.csv) · [`docs/deck.md`](docs/deck.md) |
| §2 表1 — キーカード、200 / 340 ダメージ | [`docs/deck.md`](docs/deck.md) |
| §3 — 8本の方策、0.83M パラメータ、122 / 45 / 54 次元 | [`manifests/models.csv`](manifests/models.csv) |
| §3 — 相手が公開したキーカードでの切り替え | [`configs/switch_table.json`](configs/switch_table.json) · [`docs/agent.md`](docs/agent.md) |
| §3 — リーサル探索の上限（2秒・12,288 状態遷移・深さ18） | [`manifests/environment.md`](manifests/environment.md) |
| §4 図3 — 587局・24,013局面、特徴グループ別の flip rate、対 Crustle での変化 | [`results/feature_occlusion/`](results/feature_occlusion/) · [`figures/figure3-feature-occlusion.png`](figures/figure3-feature-occlusion.png) |
| §3・§4 — リーサル検知による学習時間の増加 +3.4% | [`results/lethal_aware_rl/sec_per_iteration.csv`](results/lethal_aware_rl/sec_per_iteration.csv) |
| §4 図4 — リーサル検知あり・なしの強化学習 | [`results/lethal_aware_rl/`](results/lethal_aware_rl/) · [`figures/figure4-lethal-aware-rl.png`](figures/figure4-lethal-aware-rl.png) |
| §4 — 勝ちを証明できる局面により多く到達 | [`results/lethal_aware_rl/provable_win_positions.csv`](results/lethal_aware_rl/provable_win_positions.csv) |
| §4 図5 — 汎用方策 48.9% → 8モデル 63.9% | [`results/specialists/matchup_win_rates.csv`](results/specialists/matchup_win_rates.csv) |
| §4 — 誤った切り替えなし | [`results/specialists/router_identification.csv`](results/specialists/router_identification.csv) |
| §4 図6 — Dragapult ex 戦での Rabsca のフィードバック | [`results/rabsca/rabsca_vs_dragapult.csv`](results/rabsca/rabsca_vs_dragapult.csv) · [`figures/figure6-rabsca-vs-dragapult.png`](figures/figure6-rabsca-vs-dragapult.png) |

CSV からこれらの数値を計算し直すには、次を実行します（Python の標準ライブラリだけで動きます）。

```
python tools/verify_report_numbers.py
```

## 次に読むもの（英語）

| | |
|---|---|
| [`docs/deck.md`](docs/deck.md) | デッキ、ゲームプラン、キーカード、60枚のリスト |
| [`docs/agent.md`](docs/agent.md) | 特徴量、模倣学習、リーグ型強化学習、対面特化方策、人のフィードバック、リーサル探索、エージェントの判断手順 |
| [`docs/results.md`](docs/results.md) | ラダーの成績と、図3・4・5・6の元になった評価 |
| [`results/README.md`](results/README.md) | 各 CSV の列の意味 |

## リポジトリの構成

```
docs/        デッキ・エージェント・結果の説明
figures/     レポートの図
results/
  ladder/             最終結果と対面別の成績
  feature_occlusion/  特徴グループ別の flip rate（図3）
  lethal_aware_rl/    ルールベースのリーサル検知あり・なしの強化学習（図4）
  specialists/        汎用方策と担当方策の勝率（図5）、切り替えの確認
  rabsca/             Dragapult ex 戦の勝率と Rabsca を場に出した割合（図6）
configs/     60枚のデッキと、方策の切り替え表
manifests/   8本の方策と実行環境
tools/       verify_report_numbers.py
```

## 含まないもの

このリポジトリはレポートの裏付け資料です。エージェントのソースコード、学習済みの重み、学習ログ、大会配布のシミュレータライブラリ（`cg/`、再配布しません）は含みません。カード画像やゲームの素材も再配布していません。カード名と効果文は、デッキを説明するためだけに、大会シミュレータのカードデータベースから引用しています。

## ライセンス

MIT — [`LICENSE`](LICENSE) を参照してください。Pokémon および Pokémon TCG は、それぞれの権利者の商標です。
