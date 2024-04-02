#!/bin/sh

set -eux

cd "$(dirname "$0")/.."

poetry check
git ls-files "*.sh" | xargs shellcheck
git ls-files "*.py" "*.pyi" | xargs poetry run ruff check
git ls-files "*.py" "*.pyi" | xargs poetry run codespell
git ls-files "*.pyi" | xargs poetry run mypy --show-error-codes
git ls-files "*.pyi" | xargs poetry run pyright
