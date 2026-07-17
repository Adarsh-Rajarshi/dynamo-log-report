#!/bin/bash
# Verifier entrypoint. Runs the test suite, then reports the outcome to Harbor by
# writing /logs/verifier/reward.txt (1 = pass, 0 = fail) and a CTRF report at
# /logs/verifier/ctrf.json. Do NOT use `set -e`: a failing test must still fall
# through to write reward 0.
set -uo pipefail

mkdir -p /logs/verifier

# pytest + pytest-json-ctrf are baked into the environment image (environment/Dockerfile).
pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json
status=$?

if [ "$status" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

exit 0
