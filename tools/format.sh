#!/bin/sh

set -eux

cd "$(dirname "$0")/.."

git ls-files "*.py" "*.pyi" | xargs poetry run ruff format
git ls-files "*.py" "*.pyi" | xargs poetry run ruff --fix
git ls-files "*.sh" | xargs shfmt -w -s
