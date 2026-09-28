#!/usr/bin/env python3
"""
JDE Assistant — one-command local setup
========================================
Run this once, from this folder, with the same Python you intend to use:

    python install.py

What it does:
  1. Installs the pinned dependencies from requirements.txt.
  2. Detects the real path to this Python interpreter and to
     mcp_server.py in this folder, and writes them into manifest.json
     automatically — this is the step that used to be a manual, easy-to-
     get-wrong edit (the "REPLACE_WITH_..." placeholders).
  3. Builds the installable extension (dist/jde-assistant.mcpb) by
     calling build_mcpb.py.
  4. Prints the exact next step (install the .mcpb in Claude Desktop).

Safe to re-run any time — e.g. after `git pull` picks up a new version
of mcp_server.py, run this again, then reinstall the extension in
Claude Desktop (uninstall old one first). A `git pull` alone does NOT
update an already-installed extension; you must rebuild and reinstall.
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MANIFEST_PATH = os.path.join(ROOT, "manifest.json")
SERVER_PATH = os.path.join(ROOT, "mcp_server.py")
REQUIREMENTS_PATH = os.path.join(ROOT, "requirements.txt")


def fail(msg: str):
    print(f"\nERROR: {msg}")
    sys.exit(1)


def step(msg: str):
    print(f"\n==> {msg}")


def check_python_version():
    if sys.version_info < (3, 10):
        fail(
            f"Python 3.10+ is required; this is {sys.version_info.major}.{sys.version_info.minor}. "
            "Install a newer Python from python.org and re-run this script with it "
            "(e.g. `py -3.12 install.py` on Windows)."
        )
    print(f"Python OK: {sys.executable} (version {sys.version.split()[0]})")


def install_dependencies():
    if not os.path.exists(REQUIREMENTS_PATH):
        fail("requirements.txt not found next to install.py. Did the clone finish correctly?")
    print(f"Installing from {REQUIREMENTS_PATH} ...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", REQUIREMENTS_PATH],
        cwd=ROOT,
    )
    if result.returncode != 0:
        fail(
            "pip install failed (see output above). On some systems you may need:\n"
            f"    {sys.executable} -m pip install -r requirements.txt --break-system-packages"
        )
    print("Dependencies installed.")


def patch_manifest():
    if not os.path.exists(MANIFEST_PATH):
        fail("manifest.json not found next to install.py.")
    if not os.path.exists(SERVER_PATH):
        fail("mcp_server.py not found next to install.py.")

    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    python_path = sys.executable
    server_path = SERVER_PATH

    try:
        mcp_config = manifest["server"]["mcp_config"]
    except KeyError:
        fail("manifest.json is missing server.mcp_config — is this the right file?")

    old_command = mcp_config.get("command")
    old_args = mcp_config.get("args")

    mcp_config["command"] = python_path
    mcp_config["args"] = [server_path]

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")

    print(f"manifest.json updated:")
    print(f"  command : {old_command!r}  ->  {python_path!r}")
    print(f"  args    : {old_args!r}  ->  {[server_path]!r}")


def build_extension():
    build_script = os.path.join(ROOT, "build_mcpb.py")
    if not os.path.exists(build_script):
        fail("build_mcpb.py not found next to install.py.")
    result = subprocess.run([sys.executable, build_script], cwd=ROOT)
    if result.returncode != 0:
        fail("build_mcpb.py failed (see output above).")


def main():
    print("JDE Assistant — local setup\n" + "=" * 40)
    step("1/4 Checking Python version")
    check_python_version()

    step("2/4 Installing dependencies")
    install_dependencies()

    step("3/4 Writing correct paths into manifest.json")
    patch_manifest()

    step("4/4 Building the extension")
    build_extension()

    dist_path = os.path.join(ROOT, "dist", "jde-assistant.mcpb")
    print("\n" + "=" * 40)
    print("Setup complete.")
    print(f"\nNext step (in Claude Desktop):")
    print("  Settings -> Extensions -> Advanced settings -> Extension Developer")
    print(f"  -> Install Extension... -> select:\n      {dist_path}")
    print("\nIf you already had this extension installed from an earlier version,")
    print("uninstall it first, then install the newly built one — reinstalling")
    print("is how an update actually takes effect; a git pull alone does not.")
    print("\nYou'll be prompted for JDE API URL and JDE API Key — get these from")
    print("your vendor if you don't already have them.")


if __name__ == "__main__":
    main()
