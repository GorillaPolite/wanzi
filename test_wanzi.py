"""
Test suite for Wanzi - Git repository management tool
"""

import unittest
import json
from pathlib import Path
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
import wanzi


class TestWanziCommands(unittest.TestCase):
    """Test cases for Wanzi CLI commands"""

    def setUp(self):
        """Set up test fixtures"""
        self.runner = CliRunner()

    def test_cli_version(self):
        """Test that version command works"""
        result = self.runner.invoke(wanzi.cli, ['--version'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('1.0.0', result.output)

    def test_cli_help(self):
        """Test that help command works"""
        result = self.runner.invoke(wanzi.cli, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Wanzi', result.output)
        self.assertIn('status', result.output)

    @patch('wanzi.run_git_command')
    def test_status_command(self, mock_git):
        """Test status command"""
        mock_git.return_value = "On branch main\nnothing to commit"
        result = self.runner.invoke(wanzi.cli, ['status'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Repository Status', result.output)
        mock_git.assert_called_with(['status'])

    @patch('wanzi.run_git_command')
    def test_log_command(self, mock_git):
        """Test log command"""
        mock_git.return_value = "abc123 Test commit"
        result = self.runner.invoke(wanzi.cli, ['log', '--limit', '5'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Commit History', result.output)

    @patch('wanzi.run_git_command')
    def test_branches_command(self, mock_git):
        """Test branches command"""
        mock_git.return_value = "* main\n  develop"
        result = self.runner.invoke(wanzi.cli, ['branches'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Branches', result.output)

    @patch('wanzi.run_git_command')
    def test_info_command(self, mock_git):
        """Test info command"""
        mock_git.side_effect = [
            "https://github.com/test/repo",
            "main",
            "42",
            "5 User Name"
        ]
        result = self.runner.invoke(wanzi.cli, ['info'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Repository Information', result.output)

    def test_config_commands(self):
        """Test config set and get commands"""
        with self.runner.isolated_filesystem():
            # Create a temporary config file path
            temp_config = Path('.wanzi_config.json')
            
            with patch('wanzi.CONFIG_FILE', temp_config):
                # Test setting a config value
                result = self.runner.invoke(wanzi.cli, ['config-set', 'test_key', 'test_value'])
                self.assertEqual(result.exit_code, 0)
                self.assertIn('Configuration updated', result.output)
                
                # Test getting the config value
                result = self.runner.invoke(wanzi.cli, ['config-get', 'test_key'])
                self.assertEqual(result.exit_code, 0)
                self.assertIn('test_value', result.output)

    def test_load_config_with_invalid_json(self):
        """Test that load_config handles invalid JSON gracefully"""
        with self.runner.isolated_filesystem():
            temp_config = Path('.wanzi_config.json')
            temp_config.write_text('invalid json{')
            
            with patch('wanzi.CONFIG_FILE', temp_config):
                config = wanzi.load_config()
                self.assertEqual(config, {})

    def test_load_config_with_missing_file(self):
        """Test that load_config handles missing file gracefully"""
        with self.runner.isolated_filesystem():
            temp_config = Path('.wanzi_config_nonexistent.json')
            
            with patch('wanzi.CONFIG_FILE', temp_config):
                config = wanzi.load_config()
                self.assertEqual(config, {})

    @patch('wanzi.run_git_command')
    def test_diff_command_with_changes(self, mock_git):
        """Test diff command when there are changes"""
        mock_git.return_value = "diff --git a/file.txt"
        result = self.runner.invoke(wanzi.cli, ['diff'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Working Directory Changes', result.output)

    @patch('wanzi.run_git_command')
    def test_diff_command_no_changes(self, mock_git):
        """Test diff command when there are no changes"""
        mock_git.return_value = ""
        result = self.runner.invoke(wanzi.cli, ['diff'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('No changes', result.output)


class TestGitCommandRunner(unittest.TestCase):
    """Test cases for Git command execution"""

    @patch('subprocess.run')
    def test_run_git_command_success(self, mock_run):
        """Test successful Git command execution"""
        mock_run.return_value = MagicMock(stdout="Success", returncode=0)
        result = wanzi.run_git_command(['status'])
        self.assertEqual(result, "Success")

    @patch('subprocess.run')
    def test_run_git_command_failure(self, mock_run):
        """Test failed Git command execution"""
        mock_run.side_effect = FileNotFoundError()
        result = wanzi.run_git_command(['status'])
        self.assertIn('Git is not installed', result)


if __name__ == '__main__':
    unittest.main()
