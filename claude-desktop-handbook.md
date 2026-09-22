# The Claude Desktop Handbook

*Internal training reference · v1*

Every option in the Claude desktop app — what it is, when it's the right tool, and exactly how to use it. Written to be read once end-to-end, then kept open as a reference during a live training session.

**Covers:** Chat · Cowork mode · Artifacts · Files & browser · Automation · Extensibility · Memory & safety
**Last verified against:** Claude Help Center, September 2026

> A version of this handbook with illustrative screen mockups for each feature is published as a live page — useful when presenting to a group. Ask for the link if you need it again.

---

## Legend

Every option below follows the same shape — **what it is**, **when to reach for it**, **how to use it** — so you can scan for the piece you need mid-training.

Badges used throughout:

| Badge | Meaning |
|---|---|
| 🖥 desktop | Available in the desktop app |
| 🌐 web | Available on web |
| 📱 mobile | Available on mobile |
| free plan | Works on the free plan |
| pro / max | Requires Pro or Max |
| team / enterprise | Team / Enterprise only (or has extra features there) |
| beta | Beta or limited-availability feature |

Plan and platform availability change frequently — treat badges as "true as of verification date" and confirm anything training-critical in **Settings** before you present it.

---

## 1 · Chat vs. Cowork mode

The Claude desktop app has two ways of working, started from the same message box. Knowing which one you're in changes what to expect.

### What each one is

**Chat**
- A conversation. You ask, Claude answers in the message thread.
- Best for questions, drafting, explaining, quick back-and-forth.
- Can still read attached files and use connected tools, but stays synchronous — Claude waits for your next message.

**Cowork**
- An agentic mode for multi-step work: Claude plans, uses tools, checks in for approval, and keeps working.
- Runs in an isolated cloud session — it keeps going even if you close the app or your laptop sleeps.
- Can touch local files/folders, browse the web, and be scheduled to repeat.

### When to use which

**Reach for Chat when…**
- You want a fast answer or a single draft, not a multi-step job.
- You're thinking something through and want a back-and-forth.
- The task finishes in one or two turns.

**Reach for Cowork when…**
- The task has several steps: research, build, check, revise.
- It touches files, folders, spreadsheets, or the browser.
- You want to describe an outcome, step away, and come back to it done.
- It should repeat on a schedule.

### How to switch

1. In the message box, select `Cowork` before sending — or just describe the task; the app will suggest Cowork when it looks multi-step.
2. Cowork sessions appear in their own list, separate from chat history, and can be reopened later from any device.
3. You can move a chat conversation into a Cowork project (see §3) to give it files, memory, and standing instructions.

> **Training tip:** Open both side by side and run the same request through each — a one-line question through Chat, then "build me a tracker from this spreadsheet" through Cowork. The contrast is the fastest way to teach the distinction.

---

## 2 · Starting & approving work

`🖥 desktop` `🌐 web` `📱 mobile` `pro / max / team`

Cowork acts on your behalf — reading files, running commands, sending things. The approval mode controls how much it checks with you first.

### The three approval modes

| Mode | What happens | When to use it |
|---|---|---|
| **Manually approve** | Claude pauses before every action and waits for your OK. | Sensitive files, financial or legal work, anything touching real accounts — and always for the first run of a new kind of task. |
| **Automatically approve** | Claude runs read-only actions freely; for anything that writes or changes something, it does a quick safety check itself before proceeding. Deletion always needs your explicit approval regardless of mode. | Routine, well-understood tasks you've already seen Claude do safely. |
| **Skip all approvals** | No pauses at all, except deletion protection, which stays on. | Only for tasks you fully trust and have already scoped tightly — e.g. inside a sandboxed folder. |

### How to set it

1. The approval mode is chosen per Cowork session (and can be set as the default per scheduled task).
2. Start stricter than you think you need — you can loosen it mid-task, but you can't undo an action that already ran.
3. Deleting files always requires your explicit yes, no matter the mode.

> **Your responsibility:** Be selective about which folders you connect, limit browser access to sites you trust, and watch for anything that looks off — a task quietly doing something you didn't ask for. Report it immediately rather than letting it continue.

---

## 3 · Projects

`🖥 desktop` `🌐 web` `pro / max / team`

A project is a standing workspace for related work — its own files, instructions, and memory — so you stop re-explaining context every time.

**What it gives you**
- Custom instructions applied to every task in the project.
- Context: connected local folders, linked chat projects, or reference URLs.
- Project-scoped memory — what Claude learns here stays here, and doesn't leak into unrelated projects.
- Its own recurring scheduled tasks.

**When to make one**
- You'll come back to the same area of work repeatedly (a client, a department, a recurring report).
- Several people need to share the same context and instructions.
- You're tired of re-attaching the same files or re-explaining the same conventions.

### How to create one

1. **From scratch** — set instructions and add files as you go.
2. **From an existing chat project** — imports its files and instructions.
3. **From a folder on your computer** — the folder becomes the project's working context.

> **Know the sync rule:** Projects created on desktop stay local to that machine and don't sync to your account. Projects created in the cloud sync everywhere. Pick deliberately if you need the project on more than one device.

Team and Enterprise plans can share a project with colleagues as *Can view* or *Can edit*.

---

## 4 · Artifacts

`🖥 desktop` `🌐 web` `📱 mobile` `pro / max / team`

Artifacts are the things Cowork builds that are meant to be opened again — not a one-off answer in the chat thread, but a saved, shareable piece of work with its own place to live.

### The building-block types

| Type | Use it for |
|---|---|
| **Docs** | Memos, plans, specs, write-ups — text people will read and edit together, not a one-time reply. |
| **Slides** | Presentation decks — downloadable as PowerPoint or PDF when you need a file to send. |
| **Sheets** | Tables you'll sort, filter, or calculate with — budgets, trackers, lists of records. |
| **Design** | Mockups, landing pages, posters — anything judged by how it looks. |
| **Design System** | A reusable brand reference — colors, type, components — that other artifacts build on. |
| **Whiteboard** | Brainstorms, retros, flowcharts, architecture sketches — visual, collaborative thinking. |
| **Tasks** | To-do lists and project boards with owners, status, and dates. |
| **Custom pages** | Dashboards, trackers, reference pages, calculators, comparison tools — anything none of the above quite fits, built as a small live web page. |

### When Claude reaches for an artifact vs. just a file

**Artifact (persisted, reopenable)**
- You'll revisit it, update it, or check it later.
- You mention sharing it or a team using it.
- It replaces something you'd otherwise keep open in a tab — a dashboard, a status page, a tracker.

**Plain file instead**
- You explicitly ask for a file format (.docx, .xlsx, .pptx) or a download.
- It's a one-off — "just to see," a throwaway sketch or quick demo.
- It's code headed into your own codebase.

### How to use one

1. Ask Claude to build it during a Cowork session — mention any connected apps it should pull from.
2. Or start fresh from the Artifacts view in the sidebar.
3. Every change creates a new version, so you can track how it evolved.
4. Share it selectively within your organization, or externally depending on your plan.

> **Training tip:** Have participants ask for the same output two ways — "give me this as a quick table" vs. "build me a tracker I can keep updating" — and compare what comes back. It's the clearest way to feel the artifact-vs-file line.

---

## 5 · Local files & folders

`🖥 desktop only*` `pro / max / team`

On desktop, Claude can read and write files on your actual computer — not just files you manually upload.

**What it is**
- You connect a folder; Claude can then list, read, search, edit, convert, and reorganize files inside it directly — no upload/download round trip.
- Edits happen in place with the actual file tools (not by retyping content from a preview), so nothing gets silently truncated.
- *From web or mobile, this still works — but only while the desktop app is open on a computer with that folder connected (see §8, Dispatch).

**Good fit**
- Cleaning up or merging files that already live in one place (exports, reports, contracts).
- Ongoing work in a folder you'll keep coming back to — connect it once per project.
- Letting Claude search across many local documents at once.

**Think twice**
- Folders with anything sensitive you don't want touched — connect the narrowest folder that covers the task.
- Bulk deletes — always require your explicit approval, and there's no undo once approved.

### How to connect one

1. Use the "Add folder" control in the desktop app, or let Claude request access when a task needs it — you approve which folder on a prompt.
2. New files Claude produces are written beside their sources, or into a clearly named subfolder, not overwriting originals unless you asked for that.
3. Revoking access or disconnecting a folder is available any time in settings.

---

## 6 · Browser & computer use

`🖥 desktop only` `pro / max` `computer use: beta`

Beyond files, Claude can act on the web and, in beta, directly on your screen — useful when the information or the action only exists inside a website or app.

**Built-in browser / Chrome**
- A browser pane inside the app, or control of your actual Chrome via the extension.
- Reads pages, fills forms, clicks through multi-step flows, takes screenshots.
- Use for: research across many pages, filling out a web form, checking a site's current state.

**Computer use (beta)**
- Claude can click, type, and navigate your actual screen and desktop apps — not just the browser.
- Use for: a task that lives entirely inside a desktop app with no other way in.
- Per-app permissions — you approve which applications it may touch.

### How to use it

1. When a task needs the browser, Claude will open a tab in the built-in browser (or ask to use Chrome) — you can watch it work in the side panel.
2. For computer use, grant access to specific applications when prompted; nothing is touched outside that list.
3. Sites can require a one-time approval before Claude acts on them; some sites are blocked outright.

> **Don't trigger dialogs:** Avoid steering Claude toward buttons that pop a confirm/alert dialog (e.g. "Delete") — a blocking browser dialog can freeze the session until a person dismisses it manually.

---

## 7 · Scheduled tasks

`🖥 desktop` `🌐 web` `📱 mobile` `pro / max / team`

Anything you can ask Cowork to do once, you can ask it to do again — on a timer, without you starting it.

**What it's for**
- Runs entirely in the cloud — your computer doesn't need to be on or the app open.
- Frequencies: hourly, daily, weekly, weekdays, or manual/on-demand.

**Good candidates**
- A daily brief summarizing messages, email, or calendar.
- A weekly report pulled from connected tools or spreadsheets.
- Recurring competitor or industry research.
- Periodic file cleanup or organization.

**Be careful with**
- Anything touching sensitive data unattended — nobody is there to catch an approval prompt.
- Complex, judgment-heavy tasks — schedule the well-understood, repeatable ones.

### How to create one

1. Type `/schedule` inside a Cowork task, or open the "Scheduled" section directly.
2. Either describe the goal and let Claude propose the schedule, or set it manually: name, prompt, approval mode, frequency, and (optionally) which model to use.
3. Review results, and pause, edit, or delete any scheduled task from the same section.

> **Training tip:** Have each participant schedule one small recurring task — even something trivial like "summarize my inbox every weekday at 8am" — so the mechanic is muscle memory before they trust it with anything real.

---

## 8 · Dispatch — working across devices

`🖥 desktop` `📱 mobile` `pro / max` `limited beta`

The same conversation follows you: start on your phone, continue at your desk, without losing context.

**What it does**
- Message Claude from your phone; it can reach into your desktop's local files, connectors, and — where enabled — desktop apps via computer use, as long as that computer is on and the app is open.
- Same thread, same context, wherever you pick it up.

**When to use it**

On the move and need something from your desktop machine specifically — pull a figure from a local spreadsheet, kick off a task you'll review later at your desk, keep a conversation going between contexts.

> **Availability:** Dispatch is in limited beta and isn't available to every account. If you don't have it, use a regular cloud Cowork session from mobile instead — it just won't reach files that only live on your desktop.

---

## 9 · Connectors, plugins & skills

`🖥 desktop` `🌐 web` `free (skills)` `pro+ (connectors vary)`

Three different ways to extend what Claude can do, browsable from one directory — easy to mix up, so here's the line between them.

| Type | What it is | Example |
|---|---|---|
| **Connector** | An authenticated link to an external service or app. | Google Drive, Slack, Salesforce, Jira. |
| **Skill** | A packaged set of instructions/best-practices Claude follows for a task type. Installed from the directory as view-only; copy and modify for personal use. | A house style guide, a spreadsheet-building playbook, a domain checklist. |
| **Plugin** | A bundle of skills, connectors, and sub-agents packaged together — one install, ready to go. | A "Sales" plugin bundling a CRM connector, a proposal-writing skill, and pipeline sub-agents. |

### How to browse & install

1. Click `Customize` in the sidebar.
2. Pick the tab — Skills, Connectors, or Plugins — then `+ → Browse [type]`.
3. Install (skills/plugins) or connect and authenticate (connectors). Everything installed is on by default; toggle off any time.
4. Use an installed skill by typing `/` or the `+` button in a conversation to see what's available.

Team and Enterprise accounts also see org-shared skills colleagues have published for everyone — check there before building your own from scratch.

---

## 10 · Memory & chat search

`🖥 desktop` `🌐 web` `📱 mobile` `pro / max / team`

Two related features that stop you from re-explaining yourself every conversation.

**Chat search**
- Ask Claude about a past conversation in plain language ("what did we decide about X?") — it retrieves relevant older chats.

**Memory**
- Claude saves individual facts as you go — a changed deadline, a preference, your role — rather than a full transcript.
- Applies automatically to future conversations; carries between Chat and cloud Cowork sessions.
- Scoped per project — what's learned in one project doesn't bleed into another.

### How to control it

1. Say "remember this" any time to force-save something specific.
2. Go to `Settings → Memory` to toggle Memory or Chat search off, *pause* memory (keeps existing, stops new), or *reset* it (permanent, deletes everything including project memories).
3. Use an incognito chat to keep one conversation out of both search and memory entirely.

Sensitive categories (health, politics, government IDs, financial account numbers, criminal history) are excluded by default and require explicit opt-in — several are never saved at all.

---

## 11 · Plans & availability, at a glance

A rough map of what unlocks at each tier — confirm current specifics in `Settings → Plan` since limits shift.

| Feature | Free | Pro / Max | Team / Enterprise |
|---|---|---|---|
| Chat | ✅ | ✅ | ✅ |
| Cowork mode | — | ✅ | ✅ |
| Projects | — | ✅ | ✅ + sharing |
| Artifacts | Limited | ✅ | ✅ |
| Local files / browser (desktop) | — | ✅ | ✅ |
| Computer use | — | Beta | Beta |
| Scheduled tasks | — | ✅ | ✅ |
| Dispatch | — | Limited beta | Limited beta |
| Memory & chat search | — | ✅ | ✅ |
| Connectors / plugins / skills | Skills only | ✅ | ✅ + org-shared, admin allowlists |

---

## 12 · Cheat sheet — pick the right tool fast

| # | Situation | Use |
|---|---|---|
| 01 | Quick question, one turn | Chat |
| 02 | Multi-step, touches files/web | Cowork |
| 03 | Recurring area of work | Project |
| 04 | You'll reopen or share the result | Artifact |
| 05 | Need a specific file format / one-off | Plain file |
| 06 | Work on files already on your machine | Connect a folder |
| 07 | Info/action only exists on a website | Browser |
| 08 | Only reachable via a desktop app | Computer use |
| 09 | Should repeat on its own | Scheduled task |
| 10 | Started on phone, finishing on desktop | Dispatch |
| 11 | Need a third-party app or a ready workflow | Connector / Plugin |
| 12 | Sensitive or first-time task | Manual approval |

---

## 13 · Running the training session

A suggested 60–75 minute flow that pairs each concept with something hands-on, in the order this handbook introduces them.

| Time | Segment | Hands-on |
|---|---|---|
| 10 min | Chat vs. Cowork (§1) | Run the same request both ways; compare. |
| 10 min | Approval modes (§2) | Start a Cowork task in Manual mode; watch a pause happen. |
| 10 min | Projects (§3) | Each person creates one project from a real folder they own. |
| 15 min | Artifacts (§4) | Ask for the same output as an artifact, then as a plain file; compare. |
| 10 min | Files & browser (§5–6) | Connect a folder; ask Claude to clean up or summarize what's in it. |
| 10 min | Scheduling (§7) | Everyone schedules one trivial recurring task live. |
| 10 min | Extensibility & memory (§9–10) | Browse the Customize directory; try "remember this." |
| 10 min | Q&A against the cheat sheet (§12) | Throw scenarios at the group, have them pick the right tool. |

> **Before you present:** Skim §2 and §5 out loud once more — approval modes and folder access are where trust is won or lost in week one. Everything else is discoverable; those two are worth getting right from the start.

---

*Sources: Claude Help Center — Get started with Cowork, Use Cowork on web/desktop/mobile, Use artifacts in Cowork, Organize tasks with Projects, Schedule recurring tasks, Assign tasks from anywhere (Dispatch), Use Cowork safely, Local MCP servers on Claude Desktop, Browse skills/connectors/plugins, Use plugins in Claude, Use chat search and memory. Compiled September 2026 — re-verify before relying on exact plan gates.*
