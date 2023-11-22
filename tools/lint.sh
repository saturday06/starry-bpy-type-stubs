#!/bin/sh

set -eux

cd "$(dirname "$0")/.."

poetry check
git ls-files "*.sh" | xargs shellcheck
git ls-files "*.py" "*.pyi" | xargs poetry run ruff
git ls-files "*.py" "*.pyi" | xargs poetry run codespell
git ls-files "*.py" "*.pyi" | xargs poetry run mypy --show-error-codes
git ls-files "*.py" "*.pyi" | xargs poetry run pyright
