#!/usr/bin/env python3
"""Run the isolated hierarchical routing eval on the Sandler integration branch.

This wrapper reuses the validated Prototype A host without weakening its branch
safety check. It only changes the expected branch from the historical
architecture-review branch to the current integration branch.

Examples:
  python3 scripts/run_sandler_integration_eval.py --case R031 --case R032
  python3 scripts/run_sandler_integration_eval.py \
    --case R031 --case R032 --case R033 --case R034 --case R035 \
    --case R036 --case R037 --case R038 --case R039 --case R040 --case R041
"""

from __future__ import annotations

import run_hierarchical_retriever_prototype_a_host as runner


runner.EXPECTED_BRANCH = "integrate-sandler-v1"


if __name__ == "__main__":
    raise SystemExit(runner.main())
