# JDE Assistant — Client Setup

This is the client-side piece. It connects to a hosted API (you'll be
given its URL and your API key) — it contains no business logic, table
definitions, or database credentials of its own.

## Step 1 — Check/install Python

Open Command Prompt (Windows key → type `cmd` → Enter):
```
python --version
```
If you see a version number (3.10+), continue. If "not recognized,"
install Python from python.org/downloads (check "Add Python to PATH"
during install), then reopen Command Prompt.

## Step 2 — Install dependencies

```
pip install mcp requests
```

## Step 3 — Find your Python path

```
where python
```
Copy the first path shown (the real install, not any Microsoft Store
stub under `WindowsApps`).

## Step 4 — Edit manifest.json

Open `manifest.json` in Notepad. Find these two lines:
```json
"command": "REPLACE_WITH_YOUR_PYTHON_EXE_PATH",
"args": ["REPLACE_WITH_YOUR_MCP_SERVER_PY_PATH"],
```
Replace with your real paths (double backslashes `\\`, not single):
```json
"command": "C:\\Users\\yourname\\AppData\\Local\\Programs\\Python\\Python312\\python.exe",
"args": ["C:\\Users\\yourname\\wherever-you-put-this\\mcp_server.py"],
```
Save.

## Step 5 — Build the extension

```
python build_mcpb.py
```
This creates `dist\jde-assistant.mcpb`.

## Step 6 — Install in Claude Desktop

Settings → Extensions → Advanced settings → Extension Developer →
Install Extension… → select `dist\jde-assistant.mcpb`.

You'll be prompted for two fields:
- **JDE API URL** — the hosted API's address you were given (e.g.
  `https://jde-server.onrender.com`)
- **JDE API Key** — the API key you were given

Click Install.

## Step 7 — Test it

New conversation, ask: `what is item 10001?`

## Note

**"Settings → Connectors → Add custom connector" will NOT work for
this** — that screen is for remote MCP servers reachable by URL only.
This is a local script, so it has to be installed as an extension
(steps 5–6 above), not added through that screen.

## If something breaks

Settings → Developer → Local MCP servers → View Logs, for the exact
error text.
