# Getting Started with Cursor for Editorial Review

**For**: Editors familiar with Microsoft Word who want to use AI-powered editorial tools
**Time**: ~15 minutes to set up

## What is Cursor?

Cursor is like Microsoft Word for code, but with a built-in AI assistant. You can ask it to help with tasks, and it has access to our editorial tools directly.

Think of it as: **Word + AI assistant that knows our style guide**

## Step 1: Request Cursor Access

**Cisco Employees**: Go to https://appstore.cisco.com/details/cursor and request access.

Wait for approval email (usually same day).

## Step 2: Download and Install Cursor

1. Go to https://cursor.sh
2. Click **Download for Mac** (or Windows)
3. Open the downloaded file
4. Drag Cursor to your Applications folder (Mac) or run the installer (Windows)
5. Open Cursor from your Applications

## Step 3: First Time Setup

When you first open Cursor:

1. It may ask you to sign in - use your email
2. If it asks about "settings from VS Code" - click **Skip** (you don't have VS Code)
3. You'll see a welcome screen - you can close it

### What You'll See

Cursor looks like this:

```
┌────────────────────────────────────────────────────────────────┐
│ File  Edit  Selection  View  ...                               │
├────────────────────────────────────────────────────────────────┤
│          │                                    │                │
│  Files   │         Main Editor Area          │   AI Chat     │
│  List    │    (where you work on files)      │   Panel       │
│          │                                    │               │
│          │                                    │               │
└──────────┴────────────────────────────────────┴───────────────┘
```

The **AI Chat Panel** on the right is where you'll interact with the editorial tools.

## Step 4: Open Our Project

1. Click **File** > **Open Folder**
2. Navigate to where you downloaded `course-content-testing`
3. Select the folder and click **Open**

You should now see our project files in the left sidebar.

## Step 5: Set Up the Editorial Tools

### Install Python (if not installed)

1. Open **Terminal** in Cursor:
   - Press `Ctrl+`` (backtick key, below Escape)
   - Or click **View** > **Terminal**

2. Type this command and press Enter:
   ```
   python3 --version
   ```

3. If you see a version number (like `Python 3.10.0`), you're good. If not:
   - **Mac**: Download from https://www.python.org/downloads/
   - Run the installer and restart Cursor

### Install Required Tools

In the Terminal at the bottom of Cursor, run:

```bash
pip3 install fastmcp python-docx pyyaml
```

Wait for it to finish (you'll see some text scrolling by).

## Step 6: Configure the MCP Server

1. In Cursor, press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows)
2. Type "settings json" and select **Preferences: Open User Settings (JSON)**
3. Add this configuration (ask Jason for the correct path):

```json
{
    "mcpServers": {
        "editorial": {
            "command": "python3",
            "args": ["/path/to/course-content-testing/tools/mcp_editorial_server.py"]
        }
    }
}
```

4. Save the file (`Cmd+S` or `Ctrl+S`)
5. Restart Cursor

## Step 7: Using the Editorial Tools

### Analyze a Document

1. In the AI Chat panel (right side), type:
   ```
   Analyze the document at /path/to/your-course.docx
   ```

2. The AI will return a report showing:
   - Quality score
   - Issues found (categorized)
   - Suggested fixes

### Look Up an Acronym

Type in the chat:
```
Look up the acronym VXLAN
```

You'll get:
- What it stands for
- If it's deprecated
- How to use it correctly

### Apply Fixes

To automatically apply safe fixes:
```
Apply SAFE fixes to /path/to/your-course.docx
```

This creates a new file with track changes enabled.

## Quick Reference

| What You Want | What to Type |
|---------------|--------------|
| Analyze a document | "Analyze the document at [path]" |
| Look up acronym | "Look up the acronym [ABC]" |
| Apply safe fixes | "Apply SAFE fixes to [path]" |
| List all rules | "List all editorial rules" |
| Check server status | "Get server info" |

## Troubleshooting

### "Command not found" Error

Python may not be installed. Run this in Terminal:
```
python3 --version
```

If it fails, install Python from https://www.python.org/downloads/

### "MCP server not responding"

1. Restart Cursor
2. Check that the path in settings.json is correct
3. Make sure you saved the settings file

### "File not found" Error

- Make sure you're using the full path to your DOCX file
- On Mac, paths look like: `/Users/yourname/Documents/course.docx`
- On Windows, paths look like: `C:\Users\yourname\Documents\course.docx`

## Getting Help

- **Jason (jabelk)**: Technical issues, setup help
- **GitHub Issues**: https://github.com/CiscoLearning/course-content-testing/issues

## Next Steps

Once you're comfortable:
1. Try analyzing one of the test courses in `test-courses/`
2. Review the generated report
3. Use the DOCX track changes output for SME review

---

*This guide assumes no prior experience with code editors or command line tools.*
