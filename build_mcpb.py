#!/usr/bin/env python3
"""Builds jde-assistant.mcpb from manifest.json + mcp_server.py."""

import zipfile
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
OUTPUT = os.path.join(DIST, "jde-assistant.mcpb")

os.makedirs(DIST, exist_ok=True)

with open(os.path.join(ROOT, "manifest.json")) as f:
    json.load(f)
print("manifest.json is valid JSON")

with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(ROOT, "manifest.json"), "manifest.json")
    z.write(os.path.join(ROOT, "mcp_server.py"), "mcp_server.py")

print(f"Built {OUTPUT}")
