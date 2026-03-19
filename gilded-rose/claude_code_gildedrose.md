# Claude Code Quickstart: Gilded Rose Kata
_Hands-on introduction to AI pair programming with a coding agent_

## Overview
Claude Code is a powerful terminal-based AI coding assistant with automatic checkpointing, memory management, and code review capabilities. You'll learn these features while refactoring the Gilded Rose Kata.

## Prerequisites
- Node.js 20 or newer
- Claude.ai account (recommended) or Claude Console account 
- Git installed

## Part 1: Setup & Core Features

### 1.1 Install Claude Code (if running locally, i.e. not in DevContainer / Codespace)
```bash
npm install -g @anthropic/claude-code
```

### 1.2 Start Claude Code Session (in the gildedrose directory)
```bash
cd gildedrose # If not already there
claude
```

### 1.3 Initialize Project Context
Once in Claude Code:
```
/init
```

This analyzes your project structure, identifies languages, frameworks, and dependencies.

💡 **Key Feature**: `/init` gives Claude deep understanding of your entire project
⚠️ **Note**: You may be prompted to allow file access permissions. Select the option for accepting changes in this session.

### 1.4 Check Session Status and Context
See how much context space is used:
```bash
/context
```

### 1.5 Restart Session
To make sure we re-load CLAUDE.md, restart the session by exiting and starting claude again
```bash
# Press `Ctrl+D` twice to exit
claude # Start claude again
```


## Part 2: Understanding & Memory Management

### 2.1 Initial Analysis
```
Now that you've analyzed the project, explain what the Gilded Rose kata is about. 
What are the main code quality issues you can see?
```

### 2.2 Create Business Rules Memory

_Prompt:_
```
Create a business-rules.md file with a clear table showing how each item type changes over time.
Include examples for normal items, Aged Brie, Backstage passes, and Sulfuras.
 
Replace any existing business rules summary in CLAUDE.md with this:
"_Fully read @business-rules.md for comprehensive business rules._"

Also, copy guidelines, rules etc from the template CLAUDE.md (../CLAUDE.template.md), making sure the paths are correct to guidelines.
```

**When done**: Have a look at the created file business rules file and see if it makes sense. 


### 2.3 View/Edit Memories
Open your memory files in your editor:
```
/memory
```

**Verify** that `business-rules.md` is listed as a memory file. 


## Part 3: Test-Driven Safety Net

### 3.1 Check Automatic Checkpointing
Verify that automatic checkpoints are enabled by typing the command `/config` and checking the setting _`Rewind code (checkpoints)`_.

Remember: **Every prompt you send creates an automatic checkpoint!** You can always rewind if needed.

### 3.2 Assess Current Testing - Establishing a Baseline

Before we change anything, we must ensure we don't break anything.

_Prompt:_
```
Check if there are existing tests in this project. If they exist, run them and show me the output.
What test coverage do we currently have?
```

### 3.3 Write Comprehensive Tests

_Prompt:_
```
Write characterization tests that capture all current behavior:
- Normal items degrading in quality
- Aged Brie increasing in quality  
- Backstage passes with their complex rules
- Sulfuras never changing
- Quality bounds (0-50)
- Sell-by date edge cases

Then run the tests to verify they pass.
```

### 3.4 Try out Command History Navigation
- Use `↑` and `↓` arrow keys to navigate through previous commands
- Useful to quickly re-run commands or to verify previous prompts


## Part 4: Refactoring with Rewind Safety

### 4.1 Analyze Code Quality
```
What are the main code quality issues in this implementation? 
List the top 3 problems that make this code hard to maintain.
```

### 4.2 First Refactoring
```
Let's start refactoring. Extract the logic for each item type into separate methods.
Make the changes and run the tests to ensure they still pass.
```

### 4.3 Experiment with Bigger Changes
```
I need an additional refactoring - add an additional test case for the item type "Vegemite". Treat this as a normal item.
```

Check the code to ensure "Vegemite" is added correctly.

### 4.4 Use Rewind Feature
Press `Esc` twice (or type `/rewind`) to open the rewind menu:
- Choose a previous checkpoint to restore (choose one before the "Vegemite" change)
- Options:
  - **Restore code and conversation**: Full restoration to that point
  - **Restore conversation**: Keep code changes, rewind conversation
  - **Restore code**: Revert file changes, keep conversation  

💡 **Key Feature**: Automatic checkpoints at each prompt + `/rewind` = fearless experimentation

### 4.5 Add New Feature
```
Perfect! Now add support for "Conjured" items that degrade in quality twice as fast as normal items.
Write tests first, then implement the feature, and verify tests pass.
```


## Part 5: Advanced Features & Workflows

### 5.1 Check Token Usage and Context
```
/context
```
Shows your current context window usage - helpful to know when you're approaching limits.

### 5.2 Review Your Work
```
Can you summarize all the refactoring changes we made today?
What improvements did we achieve in terms of code quality?
```

### 5.3 Create Commit
```
Create a git commit with all our changes. Write a detailed commit message explaining 
the refactoring steps and the new Conjured items feature.
```


## Command Reference

### Essential Claude Code Commands

| Command | Purpose | Usage |
|---------|---------|-------|
| `/init` | Analyze project structure | Start of project session |
| `/rewind` | Access checkpoint history | Undo changes/conversation |
| `/memory` | Open memory files in editor | Organize persistent context |
| `/context` | Show context window usage | Monitor available space |
| `/compact [focus]` | Compress conversation | Manage long sessions |
| `/status` | Session information | Check model, tools, state |
| `/help` | List all commands | Discover features |
| `Ctrl+D` | Exit session | End Claude Code |

### Keyboard Shortcuts

| Shortcut | Action | Context |
|----------|--------|---------|
| `#` at line start | Add to memory | Persistent across sessions |
| `Esc` | Interrupt | Interrupt the current operation |
| `Esc + Esc` | Open rewind menu | Restore previous state. Also clears the current message. |
| `↑/↓` arrows | Command history | Recall previous inputs |
| `Shift+Tab` | Toggle permissions | Auto-accept/Plan/Normal |


### Multiline Input
For pasting code or writing multiple lines:
- **Quick escape**: `\` + Enter
- **macOS**: Option + Enter
- **After setup**: Shift + Enter (run `/terminal-setup` first)

## Memory Hierarchy

| Type | Location | Purpose |
|------|----------|---------|
| Project | `./CLAUDE.md` | Team-shared context |
| User | `~/.claude/CLAUDE.md` | Personal preferences |


---

*Remember: Claude Code automatically checkpoints every prompt, so experiment fearlessly! The combination of memories, checkpoints, and code review makes it a true AI pair programmer.*
