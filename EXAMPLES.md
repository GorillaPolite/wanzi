# Wanzi Examples

This file demonstrates various use cases of the Wanzi CLI tool.

## Basic Commands

### Check Repository Status
```bash
$ wanzi status
Repository Status:
On branch main
nothing to commit, working tree clean

# Verbose mode shows additional branch information
$ wanzi status --verbose
```

### View Commit History
```bash
# Show last 10 commits (default)
$ wanzi log

# Show last 5 commits in compact format
$ wanzi log --limit 5 --oneline

# Show last 20 commits
$ wanzi log -n 20
```

### List Branches
```bash
# List local branches
$ wanzi branches

# List all branches including remote
$ wanzi branches --all
```

## Repository Information

### Get Repository Info
```bash
$ wanzi info
Repository Information:
Remote URL: https://github.com/user/repo
Current Branch: main
Total Commits: 42

Contributors:
     25  John Doe
     17  Jane Smith
```

### Show Statistics
```bash
$ wanzi stats
Repository Statistics:
Total Files: 150
Tracked Files: 45
Commits (Last Week): 12
```

### View Remotes
```bash
$ wanzi remotes
Remote Repositories:
origin  https://github.com/user/repo.git (fetch)
origin  https://github.com/user/repo.git (push)
```

## Working with Changes

### View Differences
```bash
$ wanzi diff
Working Directory Changes:
diff --git a/file.py b/file.py
...
```

### Check Untracked Files
```bash
$ wanzi clean-check
Untracked Files (that would be removed):
Would remove temp.txt
Would remove cache/
```

## Tags

### List All Tags
```bash
$ wanzi tags
v1.0.0
v1.1.0
v2.0.0
```

## Configuration

### Set Configuration Values
```bash
# Set a custom configuration value
$ wanzi config-set author "John Doe"
Configuration updated: author = John Doe

# Set another value
$ wanzi config-set default_branch main
```

### Get Configuration Values
```bash
# Get a specific value
$ wanzi config-get author
author: John Doe

# Get all configuration values
$ wanzi config-get
All Configuration:
author: John Doe
default_branch: main
```

## Other Commands

### Get Help
```bash
# General help
$ wanzi --help

# Command-specific help
$ wanzi log --help
```

### Check Version
```bash
$ wanzi --version
wanzi, version 1.0.0
```

## Tips and Tricks

1. **Colorful Output**: Wanzi uses colors to make output more readable
2. **Git Required**: Make sure Git is installed and in your PATH
3. **Custom Config**: Store your preferences in `~/.wanzi_config.json`
4. **Quick Status**: Use `wanzi status` for a quick overview
5. **Verbose Mode**: Add `-v` or `--verbose` to status for more details

## Integration with Shell

You can create shell aliases for frequently used commands:

```bash
# In your ~/.bashrc or ~/.zshrc
alias ws='wanzi status'
alias wl='wanzi log --limit 5 --oneline'
alias wb='wanzi branches --all'
alias wi='wanzi info'
```

## Use Cases

### Quick Repository Overview
```bash
# Get a comprehensive view of your repository
wanzi info && wanzi stats && wanzi status
```

### Pre-commit Check
```bash
# Check status and changes before committing
wanzi status && wanzi diff
```

### Repository Audit
```bash
# Full repository information
wanzi info && wanzi stats && wanzi branches --all && wanzi remotes
```
