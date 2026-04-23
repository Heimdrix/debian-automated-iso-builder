#!/bin/sh
set -eu

BASE_DIR="/tmp/preseed"

find "$BASE_DIR" -type f -name '*.sh' ! -name 'post_install.sh' | sort | while IFS= read -r script; do
  chmod 700 "$script"
  "$script"
done