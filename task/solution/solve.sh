#!/bin/bash
set -euo pipefail

# The solution/ directory is copied to /solution by the Oracle agent at runtime.
python3 /solution/solve.py
