#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FACTORY="${SCRIPT_DIR}/IDUNEX_PROJECT_FACTORY_v1.0.0.py"
TMP_WORKDIR="$(mktemp -d)"
cleanup() { rm -rf "${TMP_WORKDIR}"; }
trap cleanup EXIT
cd "${TMP_WORKDIR}"
exec python3 "${FACTORY}" "$@"
