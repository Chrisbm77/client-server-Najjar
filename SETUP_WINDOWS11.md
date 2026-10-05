# JDE Assistant (Najjar) - Setup Guide for Windows 11

This guide connects Claude Desktop on your PC to the Najjar JD Edwards database. It takes about 10 to 15 minutes. Follow the steps in order. Every command below has been run on Windows 11 and worked.

**How to use this guide**

- Each block in a gray box is a command. Type or paste it into **Command Prompt** and press Enter.
- If a step fails, use the **If it does not work** part of that step. Do not skip ahead.

## Before you start

You need these four things:

1. **Claude Desktop** installed and signed in with **your own account** ([download](https://claude.ai/download)).
2. The **JDE API URL** (sent to you separately).
3. The **JDE API Key** (sent to you separately, starts with `sk_live_`).
4. An internet connection.

> **About the key**
> - It is personal to you. Never paste it in a chat, an email or a screenshot.
> - It may lock itself to the **first computer** that uses it. Do the whole setup on the computer you will use every day.

**How to open Command Prompt:** press the Windows key, type `cmd` and press Enter. Use Command Prompt, not PowerShell. Keep the same window open for all the steps.

---

## Step 1 - Check that Python 3.12 is installed

This project works with Python 3.12. Use 3.12 even if you already have a newer Python (for example 3.14).

```
py -3.12 --version
```

**Expected result:** `Python 3.12.x` (any number after `3.12.`). If you see that, go to Step 2.

### If it does not work

If you see "No suitable Python runtime found" or "py is not recognized":

**Option A - Windows Python install manager (try this first)**

```
py install 3.12
```

Answer `Y` if it asks to confirm. Then check again:

```
py -3.12 --version
```

**Option B - Install with winget**

```
winget install Python.Python.3.12
```

Close the Command Prompt window, open a new one, then run `py -3.12 --version` again.

**Option C - Install from the website**

1. Open <https://www.python.org/downloads/release/python-31210/>
2. Download **Windows installer (64-bit)**.
3. Run it and **tick "Add python.exe to PATH"** on the first screen, then click **Install Now**.
4. Close Command Prompt, open a new one, then run `py -3.12 --version` again.

---

## Step 2 - Download the project files

**Method 1 - No extra software needed (recommended)**

```
cd %USERPROFILE%
curl -L -o client.zip https://github.com/Chrisbm77/client-server-Najjar/archive/HEAD.zip
tar -xf client.zip
dir
```

The last command lists a new folder named like `client-server-Najjar-007e92efd5a2074e30b731356fb1c418cba67576`. The long ending can be different. That is normal.

Go into that folder. Type the first part of its name, press the **TAB** key to complete it, then press Enter:

```
cd client-server-Najjar-
```

Check you are in the right place. This must show a file called `install.py`:

```
dir install.py
```

### If it does not work

**Option A - Download from the browser**

1. Open <https://github.com/Chrisbm77/client-server-Najjar>
2. Click the green **Code** button, then **Download ZIP**.
3. Open your Downloads folder, right-click the ZIP file, then **Extract All...**
4. Open the extracted folder until you see the file `install.py` (sometimes there is a folder inside a folder).
5. Click the address bar of that File Explorer window, type `cmd` and press Enter. A Command Prompt opens already in the right folder.

**Option B - Use git**

```
winget install --id Git.Git -e
```

Close Command Prompt, open a new one, then:

```
cd %USERPROFILE%
git clone https://github.com/Chrisbm77/client-server-Najjar.git
cd client-server-Najjar
```

If `curl` or `tar` are not recognized, use Option A. If the download says "404 Not Found" or "Repository not found", tell the person who sent you this guide.

---

## Step 3 - Run the setup script

Make sure you are in the folder that contains `install.py` (Step 2), then run:

```
py -3.12 install.py
```

It runs four stages. Near the end you should see:

```
==> 4/4 Building the extension
Setup complete.
```

A file named `jde-assistant.mcpb` is created in the `dist` folder. The last lines on screen show its full path. Keep this window open.

A line saying `[notice] A new release of pip is available` is **not** an error. Ignore it.

### If it does not work

**"pip install failed" or a network error**

1. Check your internet connection (open any website).
2. If you use a VPN or a company proxy, try again without it or from another network.
3. Update pip, then run the setup again:

```
py -3.12 -m pip install --upgrade pip
py -3.12 install.py
```

**"py is not recognized"**

```
python --version
```

If it shows 3.10, 3.11, 3.12 or 3.13, run `python install.py`. If it shows 3.14, go back to Step 1 and install 3.12 instead.

**Anything else:** do not keep re-running it. Take a photo or copy the last 15 lines of the window and send them to the person who sent you this guide.

You can safely run `py -3.12 install.py` again at any time.

---

## Step 4 - Install the extension in Claude Desktop

1. Open Claude Desktop (signed in with your own account).
2. Click **Settings**.
3. Go to **Extensions** -> **Advanced settings** -> **Extension Developer**.
4. Click **Install Extension...**
5. Select the file `jde-assistant.mcpb` from the `dist` folder. Its full path looks like `C:\Users\<your name>\client-server-Najjar-<long number>\dist\jde-assistant.mcpb`. To open that folder from Command Prompt, run `start dist`.
6. When asked, fill in the two fields:
   - **JDE API URL** - the address you were given
   - **JDE API Key** - the key you were given
7. Click **Install**.

> Do **not** use *Settings -> Connectors -> Add custom connector*. That screen does not work for this project.

### If it does not work

- **You cannot find "Extension Developer":** update Claude Desktop to the latest version (download it again from <https://claude.ai/download> and install over it), then look again under Settings -> Extensions -> Advanced settings.
- **The file picker does not accept the file:** in File Explorer open the `dist` folder and double-click `jde-assistant.mcpb`. Claude Desktop should open and offer to install it.
- **It installs but does not work:** fully close Claude Desktop, including from the system tray near the clock (right-click the icon, then Quit), and open it again.
- **You already had an older version installed:** uninstall it first (Settings -> Extensions), then install the new file.

---

## Step 5 - Test that it works

Open a **new chat** in Claude Desktop and ask, one at a time:

1. `what is item 10001?`
2. `What is the real title of table F4101?` (expected: *Item Master*)
3. `What are the decimals for USD in the currency table?` (expected: *2*)

If you get real answers, you are connected.

**Good habits when you read amounts**

- Amounts are stored without a decimal point. The assistant scales them using the currency table (USD, LBP and EUR use 2 decimals).
- Never add amounts of different currencies together. Ask for the result by currency, or in USD only.

---

## If it does not work - common messages

| Message you see | What it means / what to do |
|---|---|
| `ACCESS ERROR: invalid API key` | Wrong, revoked or expired key. Check you pasted it fully, with no spaces. Otherwise ask for a new key. |
| `ACCESS ERROR:` (department or table) | Your key is limited to certain data. This is expected, not a bug. |
| `ACCESS ERROR` about another device | The key is locked to a different computer. Ask the administrator to reset the device lock. |
| `CONFIGURATION ERROR: JDE_API_URL and/or JDE_API_KEY are not set` | The URL or key was not entered at install. Uninstall the extension, install it again and fill both fields (Step 4). |
| `CONNECTION ERROR: could not reach the JDE service` | The server may be waking up. Wait 60 seconds and ask again. If it persists, check your internet and the URL. |
| Extension fails to start / "Unable to connect to extension server" | The setup script did not finish. Run `py -3.12 install.py` again and reinstall the extension. |

To see the exact error: Claude Desktop -> Settings -> Developer -> Local MCP servers -> **View Logs**.

---

## Good to know

- Do **not** move, rename or delete the `client-server-Najjar-...` folder after installing. The extension points to that exact location.
- Do **not** delete the hidden file `.device_id` inside that folder.
- The first answer after a long pause can take up to 90 seconds while the server wakes up.

**Updating later (only if you are told to)**

1. Repeat Step 2 (download again) in a new folder.
2. Run `py -3.12 install.py` in the new folder.
3. In Claude Desktop, **uninstall** the old extension, then install the new `jde-assistant.mcpb` (Step 4).

---

## Summary - the whole setup in 8 commands

```
py -3.12 --version
py install 3.12
cd %USERPROFILE%
curl -L -o client.zip https://github.com/Chrisbm77/client-server-Najjar/archive/HEAD.zip
tar -xf client.zip
dir
cd client-server-Najjar-    (then press TAB and Enter)
py -3.12 install.py
```

`py install 3.12` is only needed if the first line failed. Then install `dist\jde-assistant.mcpb` in Claude Desktop (Step 4).
