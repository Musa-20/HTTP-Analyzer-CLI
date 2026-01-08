"""Tests for the main module."""

from click.testing import CliRunner
from http_analyzer_cli.main import main


def test_main_no_args():
    """Test CLI runs without arguments."""
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "Welcome to HTTP Analyzer CLI!" in result.output
