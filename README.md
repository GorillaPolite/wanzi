# Wanzi (丸子)

A comprehensive Git repository management tool with various features - "want everything" you need for Git operations!

## Features

Wanzi provides a rich set of commands to manage and inspect Git repositories:

- **status**: Show the current repository status with optional verbose mode
- **log**: Display commit history with customizable output
- **branches**: List all branches (local and remote)
- **info**: Show comprehensive repository information
- **diff**: Display changes in working directory
- **tags**: List all tags in the repository
- **config**: Set and get custom configuration values
- **stats**: Show detailed repository statistics
- **remotes**: Display remote repositories
- **clean-check**: Preview files that would be removed by git clean

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/GorillaPolite/wanzi.git
cd wanzi

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

### Using pip

```bash
pip install -r requirements.txt
python setup.py install
```

## Usage

After installation, you can use the `wanzi` command from anywhere:

```bash
# Show help
wanzi --help

# Show repository status
wanzi status

# Show detailed status
wanzi status --verbose

# Show last 5 commits in oneline format
wanzi log --limit 5 --oneline

# List all branches including remote
wanzi branches --all

# Show repository information
wanzi info

# Show working directory changes
wanzi diff

# List all tags
wanzi tags

# Show repository statistics
wanzi stats

# Show remote repositories
wanzi remotes

# Check what files would be cleaned
wanzi clean-check

# Set a configuration value
wanzi config-set mykey myvalue

# Get a configuration value
wanzi config-get mykey

# Get all configuration values
wanzi config-get
```

## Configuration

Wanzi stores custom configuration in `~/.wanzi_config.json`. You can set and retrieve custom key-value pairs using the `config-set` and `config-get` commands.

## Requirements

- Python 3.7 or higher
- Git installed and available in PATH
- Required Python packages (installed automatically):
  - click >= 8.0.0
  - colorama >= 0.4.0

## Development

```bash
# Run directly without installation
python wanzi.py --help

# Run a specific command
python wanzi.py status
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Author

GorillaPolite
