#!/bin/sh
# Rebuild the site from tools_*.py + guides.py and copy the result into the repo root (what Cloudflare Pages serves).
set -e
cd "$(dirname "$0")"
python3 build.py
cp -r site/. .
rm -rf site preview.html __pycache__
echo "published files refreshed in repo root"
