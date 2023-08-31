#!/bin/sh

set -eux

cd "$(dirname "$0")/.."

git ls-files "*.py" "*.pyi" | xargs poetry run isort
git ls-files "*.py" "*.pyi" | xargs poetry run black
git ls-files "*.sh" | xargs shfmt --write --simplify
