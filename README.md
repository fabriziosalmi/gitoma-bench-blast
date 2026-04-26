# gitoma-bench-blast

> Hot-symbol blast-radius stress test for the gitoma agent. Targets
> the **CPG-lite BLAST RADIUS** prompt block, **Ψ-full Φ component**,
> and **G18/G19 orphan-symbol detection** introduced in
> gitoma v0.5.0.

## What this bench measures

Patches that touch a single function with MANY callers are the
"don't blindly modify the platform foundation" failure mode. This
repo is built around exactly that shape:

- One **hub function** (`core.process`) called by 30+ callers across
  the repo.
- One **leaf function** (`utils.format_value`) called by 1 caller.
- Several **dead helpers** with zero callers (so we can verify the
  agent doesn't add MORE dead helpers — G19 territory).

Three measurement axes:

### Axis 1 — Φ (caller-impact-weighted safety)

A patch touching `core.process` should score Φ ≈ `1/(1+log(31))` ≈
0.225. Below the `phi_hard_min=0.20` floor only at >55 callers, so
this hub sits JUST ABOVE the trigger — calibrating false-positive
sensitivity.

### Axis 2 — BLAST RADIUS prompt block

The worker's prompt should include "Modifying core.py touches 30+
cross-file callers" when a subtask hints at `core.py`. We can
inspect the trace event `cpg.skeletal_rendered` + manually inspect
the worker prompt under `--verbose` to confirm the block lands.

### Axis 3 — G18 + G19

If the agent's patch:
- Deletes a caller of `core.process` and leaves `core.process`
  unchanged → G18 should NOT fire (1 caller of 31 deleted is
  not "abandoned"; helper still has 30 callers).
- Adds new helpers that only call each other → G19 should fire.

## Repo layout

```
core/
  __init__.py
  hub.py           # contains `process()` — the hub with 31 callers
utils/
  __init__.py
  format.py        # contains `format_value()` — leaf with 1 caller
helpers/
  dead.py          # functions with 0 callers — G16 candidates
callers/
  api_routes.py
  background_jobs.py
  cli_handlers.py
  cron_tasks.py
  webhooks.py
  ...              # 6 caller modules, ~5 callers each = 31 total
tests/
  test_smoke.py
```

## Running the bench

Local (requires LM Studio + gitoma):

```bash
LM_STUDIO_BASE_URL=http://localhost:1234/v1 \
LM_STUDIO_MODEL=qwen/qwen3-8b \
LM_STUDIO_TIMEOUT=300 \
GITOMA_CPG_LITE=on \
GITOMA_PSI_FULL=on \
GITOMA_TEST_GEN=on \
GITOMA_G18_ABANDONED=on \
GITOMA_G19_ECHO_CHAMBER=on \
gitoma run --dry-run --reset --yes \
  https://github.com/fabriziosalmi/gitoma-bench-blast
```

## Success criteria

- `cpg.index_built` trace event reports ≥ 30 callers for
  `process()`.
- The plan emitted by the LLM should AVOID proposing direct edits
  to `core.hub` unless the hint mentions it explicitly.
- Real run that actually touches `core.process` should see the
  worker prompt include a BLAST RADIUS block listing the 30+
  caller files.
- Φ scoring on a patch touching `core.hub`: somewhere ~0.2 (just
  above the 0.20 hard-min floor).
