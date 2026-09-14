# Runtime and training environment

## The submitted agent

| | |
|---|---|
| Kaggle submission | ref `55565476`, submitted 2026-08-16 23:48 UTC |
| Language | Python 3.10+ |
| Inference dependencies | numpy only |
| Policies | 8 (`policy_attn2.npz` per slot), one shared 60-card deck |
| Archive size | 24.3 MiB (limit 197.7 MiB) |
| Feature contract | `features_version = 45`, `feature_schema_hash = 0a89872219a887ee`, identical for all eight policies and checked at load time |
| Lethal search limits | 2 seconds, 12,288 state transitions and depth 18 per call (constants of the submitted lethal search) |
| Policy switching | one-way, on public key cards only ([`../configs/switch_table.json`](../configs/switch_table.json)) |
| Pre-submission checks | scoring simulation 5/5 passed (loads without `__file__`, 60-card deck selection, policy load, full game completion); a 12-matchup smoke run with every matchup routed to its assigned policy |

## Training

PyTorch, on three personal desktop machines:

| GPU | Memory |
|---|---|
| NVIDIA GeForce RTX 4070 SUPER | 12 GB |
| NVIDIA GeForce RTX 4060 | 8 GB |
| NVIDIA GeForce GTX 1080 Ti | 11 GB |

Reinforcement learning uses 512 games per iteration with PPO and GAE.
