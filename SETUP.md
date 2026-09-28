# JDE Assistant — Client Setup

This is the client-side piece only. It connects to a hosted API (you'll
be given its URL and an API key) and contains no business logic, table
definitions, or database credentials of its own — without a valid key
pointed at a live server, this file does nothing at all.

## What you'll need before starting

- Python 3.10 or newer, installed on this machine
- Claude Desktop, installed and signed in
- A JDE API URL and JDE API Key from your vendor (contact them if you
  don't have these yet)

## Step 1 — Get the files

If you were sent a `.zip`, unzip it anywhere convenient. If instead
you're pulling from GitHub:

```
git clone <repo-url>
cd client-server
```

## Step 2 — Check Python

Open a terminal (Windows: Command Prompt) in this folder:

```
python --version
```

If you see 3.10 or higher, continue. If it says "not recognized,"
install Python from python.org/downloads — check **"Add Python to
PATH"** during install — then reopen the terminal.

## Step 3 — Run the setup script

```
python install.py
```

This single command:
- installs the exact dependency versions this project needs (from
  `requirements.txt` — the `mcp` package is pinned to a specific
  version on purpose, because newer versions have broken this project
  before)
- detects the real path to your Python and to `mcp_server.py`, and
  writes both into `manifest.json` for you (this used to be a manual
  edit and was the single most common cause of a failed install — if
  you ever see `REPLACE_WITH_YOUR_PYTHON_EXE_PATH` still sitting in
  `manifest.json`, this step didn't run or didn't finish)
- builds the installable extension at `dist\jde-assistant.mcpb`

If it fails partway, read the error it prints — it's written to tell
you what to do next, not just that something broke.

## Step 4 — Install the extension in Claude Desktop

Claude Desktop → Settings → Extensions → Advanced settings → Extension
Developer → **Install Extension…** → select `dist\jde-assistant.mcpb`.

You'll be prompted for two fields:
- **JDE API URL** — e.g. `https://jde-server.onrender.com`
- **JDE API Key** — the key your vendor gave you

Click Install.

> **Note:** "Settings → Connectors → Add custom connector" will **not**
> work for this. That screen is for remote MCP servers reachable by URL
> alone. This is a local script, so it has to go in as an extension via
> the steps above.

## Step 5 — Test it

Start a new conversation and ask: `what is item 10001?`

If you get a real answer back, you're done.

## Updating later

If your vendor pushes an update to this repo:

```
git pull
python install.py
```

Then, in Claude Desktop, **uninstall the old extension first**, and
install the freshly built `dist\jde-assistant.mcpb` as a new install.

This last part matters: pulling from GitHub, or even rebuilding the
`.mcpb`, does **not** update an extension that's already installed —
Claude Desktop only picks up the new code when you remove the old
install and add the new one.

## About device binding

Some API keys are locked to a single device the first time they're
used — a small random ID is generated and saved next to `mcp_server.py`
as a hidden file, `.device_id`. If your key has this turned on:

- The first machine to use the key "claims" it.
- Using the same key from a second machine, or after deleting
  `.device_id`, will be rejected by the server as a different device.
- If that happens unexpectedly (a new PC, a wiped machine, a moved
  folder), it isn't something you can fix locally — contact your
  vendor and ask them to reset the binding for your key.

Not every key has this enabled. If yours doesn't, the ID is still sent
with every request but simply ignored by the server.

## Other things worth knowing

- **Request timeout:** the client waits up to 90 seconds for a
  response by default (some queries against a live database take a
  while). If you need it longer, set an environment variable before
  launching Claude Desktop: `JDE_REQUEST_TIMEOUT_SECONDS=180`. Most
  people never need to touch this.
- **This folder is not the server.** All table access rules, security,
  and database credentials live on the hosted API, not here. There is
  nothing sensitive in this folder to protect beyond your own API key,
  which you enter once during Step 4 and which Claude Desktop stores
  for you.

## If something breaks

Claude Desktop → Settings → Developer → Local MCP servers → View Logs,
for the exact error text. Common ones:

| Message | Likely cause |
|---|---|
| `ACCESS ERROR: invalid API key` | Wrong key, or key was revoked/expired — contact your vendor |
| `ACCESS ERROR: <department/table message>` | Your key is scoped to certain data and this question falls outside it — expected behavior, not a bug |
| `CONFIGURATION ERROR: JDE_API_URL and/or JDE_API_KEY are not set` | The extension wasn't installed with those fields filled in — reinstall via Step 4 |
| `CONNECTION ERROR: could not reach the JDE service` | The hosted API is down or waking up from idle — wait 30–60 seconds and try again |
| Extension fails to start / "Unable to connect to extension server" | `manifest.json` still has a `REPLACE_WITH_...` placeholder — re-run `python install.py` |
