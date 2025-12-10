# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-12-07

### Added
- Initial release of Wanzi - comprehensive Git repository management tool
- `status` command to show repository status with optional verbose mode
- `log` command to display commit history with customizable output
- `branches` command to list all branches (local and remote)
- `info` command to show comprehensive repository information
- `diff` command to display working directory changes
- `tags` command to list all repository tags
- `config-set` and `config-get` commands for custom configuration management
- `stats` command to show detailed repository statistics
- `remotes` command to display remote repositories
- `clean-check` command to preview files that would be removed by git clean
- Colorful terminal output using colorama
- Configuration file support (~/.wanzi_config.json)
- Comprehensive documentation in README.md
- MIT License
- Python package setup with setup.py

### Technical Details
- Built with Python 3.7+ support
- Uses Click for CLI argument parsing
- Proper error handling for Git commands
- Memory-efficient file counting for large repositories
- JSON configuration with error handling
