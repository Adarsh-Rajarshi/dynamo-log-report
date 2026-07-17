# Project Dynamo — Fixed Terminal-Bench 2 (Harbor) task: `log-report`

This repo contains a repaired Terminal-Bench 2 (Harbor) task. The underlying task is
simple: parse an Apache-style access log into a small JSON report. The original authoring
was broken in several ways; this repo fixes it into correct Harbor format.

The task lives under [`task/`](./task).

```
task/
├── task.toml            # TB2 Harbor config
├── instruction.md       # agent-facing instructions + success criteria
├── environment/
│   ├── Dockerfile        # agent image (base pinned by digest, no solution leak)
│   └── access.log        # task input
├── solution/
│   ├── solve.sh          # oracle entrypoint
│   └── solve.py          # reference solution
└── tests/
    ├── test.sh           # verifier entrypoint -> /logs/verifier/{reward.txt,ctrf.json}
    └── test_outputs.py   # value-based checks (not just file existence)
```

## Defects fixed

| # | Defect | Fix |
|---|--------|-----|
| 1 | `task.toml` `artifacts` was a string pointing to the wrong file (`/app/out.json`) | `artifacts = ["/app/report.json"]` (array, real output) |
| 2 | `environment/Dockerfile` used an unpinned base (`python:latest`) | pinned `python:3.12-slim@sha256:57cd7c3a…10de` |
| 3 | Agent image leaked the reference solution (`solution_hint.py`) | file removed; no solution ships in the agent image |
| 4 | Verifier was gameable (only checked the file exists / is non-empty) | `test_outputs.py` asserts real values: `total_requests=6`, `unique_ips=3`, `top_path=/index.html` |
| 5 | `tests/test.sh` wrote reward to `/app/reward.txt` and produced no CTRF | writes `/logs/verifier/reward.txt` + `/logs/verifier/ctrf.json` |
| 6 | `instruction.md` was ambiguous and inconsistent with the verifier | clear output path, exact field spec, and numbered success criteria |

Hardening (not one of the graded defects): `allow_internet = false` — the task is fully
local, so the environment is hermetic.

Distractors (correctly left alone): access.log is not corrupted, the task needs no runtime
network, the oracle already computes the right answer, and `memory_mb = 2048` is ample.

## Verification (Harbor 0.19.0)

```
harbor run -p . --agent oracle   ->  Mean 1.000   (reward.txt = 1, 3/3 CTRF tests passed)
harbor run -p . --agent nop      ->  Mean 0.000   (reward.txt = 0, 3/3 failed: no report.json)
```

Run from the `task/` directory:

```bash
cd task
harbor run -p . --agent oracle
harbor run -p . --agent nop
```
