#!/usr/bin/env python3
"""
Wanzi - A comprehensive Git repository management tool
"""

import os
import sys
import json
import subprocess
from pathlib import Path
import click
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Configuration file path
CONFIG_FILE = Path.home() / '.wanzi_config.json'


def load_config():
    """Load configuration from file"""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_config(config):
    """Save configuration to file"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)


def run_git_command(args):
    """Run a git command and return the output"""
    try:
        result = subprocess.run(
            ['git'] + args,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
    except FileNotFoundError:
        return "Error: Git is not installed or not in PATH"


@click.group()
@click.version_option(version='1.0.0')
def cli():
    """Wanzi - A comprehensive Git repository management tool with various features"""
    pass


@cli.command()
@click.option('--verbose', '-v', is_flag=True, help='Show detailed information')
def status(verbose):
    """Show the current repository status"""
    click.echo(f"{Fore.CYAN}Repository Status:{Style.RESET_ALL}")
    output = run_git_command(['status'])
    click.echo(output)
    
    if verbose:
        click.echo(f"\n{Fore.CYAN}Branch Information:{Style.RESET_ALL}")
        branch_output = run_git_command(['branch', '-vv'])
        click.echo(branch_output)


@cli.command()
@click.option('--limit', '-n', default=10, help='Number of commits to show')
@click.option('--oneline', is_flag=True, help='Show compact one-line format')
def log(limit, oneline):
    """Show commit history"""
    click.echo(f"{Fore.CYAN}Commit History:{Style.RESET_ALL}")
    args = ['log', f'-{limit}']
    if oneline:
        args.append('--oneline')
    output = run_git_command(args)
    click.echo(output)


@cli.command()
@click.option('--all', '-a', is_flag=True, help='Show all branches including remote')
def branches(all):
    """List all branches"""
    click.echo(f"{Fore.CYAN}Branches:{Style.RESET_ALL}")
    args = ['branch']
    if all:
        args.append('-a')
    output = run_git_command(args)
    click.echo(output)


@cli.command()
def info():
    """Show repository information"""
    click.echo(f"{Fore.CYAN}Repository Information:{Style.RESET_ALL}")
    
    # Get remote URL
    remote_url = run_git_command(['config', '--get', 'remote.origin.url'])
    click.echo(f"{Fore.GREEN}Remote URL:{Style.RESET_ALL} {remote_url.strip()}")
    
    # Get current branch
    current_branch = run_git_command(['rev-parse', '--abbrev-ref', 'HEAD'])
    click.echo(f"{Fore.GREEN}Current Branch:{Style.RESET_ALL} {current_branch.strip()}")
    
    # Get total commits
    commit_count = run_git_command(['rev-list', '--count', 'HEAD'])
    click.echo(f"{Fore.GREEN}Total Commits:{Style.RESET_ALL} {commit_count.strip()}")
    
    # Get contributors
    contributors = run_git_command(['shortlog', '-sn', '--all'])
    click.echo(f"\n{Fore.GREEN}Contributors:{Style.RESET_ALL}")
    click.echo(contributors)


@cli.command()
def diff():
    """Show changes in working directory"""
    click.echo(f"{Fore.CYAN}Working Directory Changes:{Style.RESET_ALL}")
    output = run_git_command(['diff'])
    if output.strip():
        click.echo(output)
    else:
        click.echo(f"{Fore.YELLOW}No changes in working directory{Style.RESET_ALL}")


@cli.command()
@click.option('--all', '-a', is_flag=True, help='Show all tags')
def tags(all):
    """List tags"""
    click.echo(f"{Fore.CYAN}Tags:{Style.RESET_ALL}")
    args = ['tag']
    if all:
        args.append('-l')
    output = run_git_command(args)
    if output.strip():
        click.echo(output)
    else:
        click.echo(f"{Fore.YELLOW}No tags found{Style.RESET_ALL}")


@cli.command()
@click.argument('key')
@click.argument('value')
def config_set(key, value):
    """Set a configuration value"""
    config = load_config()
    config[key] = value
    save_config(config)
    click.echo(f"{Fore.GREEN}Configuration updated:{Style.RESET_ALL} {key} = {value}")


@cli.command()
@click.argument('key', required=False)
def config_get(key):
    """Get configuration value(s)"""
    config = load_config()
    if key:
        value = config.get(key, 'Not set')
        click.echo(f"{Fore.GREEN}{key}:{Style.RESET_ALL} {value}")
    else:
        click.echo(f"{Fore.CYAN}All Configuration:{Style.RESET_ALL}")
        if config:
            for k, v in config.items():
                click.echo(f"{Fore.GREEN}{k}:{Style.RESET_ALL} {v}")
        else:
            click.echo(f"{Fore.YELLOW}No configuration set{Style.RESET_ALL}")


@cli.command()
def stats():
    """Show repository statistics"""
    click.echo(f"{Fore.CYAN}Repository Statistics:{Style.RESET_ALL}")
    
    # File count
    try:
        file_count = len(list(Path('.').rglob('*')))
        click.echo(f"{Fore.GREEN}Total Files:{Style.RESET_ALL} {file_count}")
    except Exception as e:
        click.echo(f"{Fore.RED}Error counting files:{Style.RESET_ALL} {e}")
    
    # Lines of code (simplified)
    output = run_git_command(['ls-files'])
    files = output.strip().split('\n') if output.strip() else []
    click.echo(f"{Fore.GREEN}Tracked Files:{Style.RESET_ALL} {len(files)}")
    
    # Commit activity
    recent_commits = run_git_command(['rev-list', '--count', '--since=1.week.ago', 'HEAD'])
    click.echo(f"{Fore.GREEN}Commits (Last Week):{Style.RESET_ALL} {recent_commits.strip()}")


@cli.command()
@click.option('--remote', '-r', default='origin', help='Remote name')
def remotes(remote):
    """Show remote repositories"""
    click.echo(f"{Fore.CYAN}Remote Repositories:{Style.RESET_ALL}")
    output = run_git_command(['remote', '-v'])
    click.echo(output)


@cli.command()
def clean_check():
    """Check what would be removed by git clean"""
    click.echo(f"{Fore.CYAN}Untracked Files (that would be removed):{Style.RESET_ALL}")
    output = run_git_command(['clean', '-n'])
    if output.strip():
        click.echo(output)
    else:
        click.echo(f"{Fore.GREEN}No untracked files to clean{Style.RESET_ALL}")


if __name__ == '__main__':
    cli()
