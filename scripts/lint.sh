#!/bin/sh

set -eux

cd "$(dirname "$0")/.."

git ls-files "*.sh" | xargs shellcheck
git ls-files "*.pyi" | xargs poetry run mypy --show-error-codes
git ls-files "*.py" "*.pyi" | xargs poetry run flake8 --count --show-source --statistics
git ls-files "*.py" "*.pyi" | xargs poetry run pylint
