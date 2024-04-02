#!/bin/sh

set -eux

cd "$(dirname "$0")/../src"
rm -fr ../subprojects/pseudo-bpy/src
mkdir ../subprojects/pseudo-bpy/src
find . -maxdepth 1 -type d | while read -r f; do
  echo "$f"
  dest=$(echo "$f" | sed -e 's/-stubs$//')
  cp -fr "$f" "../subprojects/pseudo-bpy/src/$dest"
done

cd ../subprojects/pseudo-bpy/src
find . -name "*.pyi" | while read -r f; do
  dest=$(echo "$f" | sed -e 's/\.pyi$/.py/')
  echo "from __future__ import annotations" >>"$dest"
  cat "$f" >>"$dest"
  rm -f "$f"
done
