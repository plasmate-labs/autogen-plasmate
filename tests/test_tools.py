"""Tests for autogen-plasmate tools."""

import subprocess
from unittest.mock import patch, MagicMock
from autogen_plasmate.tools import plasmate_fetch


def test_fetch_success():
    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = "<som>example content</som>"

    with patch("subprocess.run", return_value=mock_result) as mock_run:
        result = plasmate_fetch("https://example.com")
        assert result == "<som>example content</som>"
        mock_run.assert_called_once_with(
            ["plasmate", "fetch", "https://example.com"],
            capture_output=True,
            text=True,
            timeout=30,
        )


def test_fetch_error():
    mock_result = MagicMock()
    mock_result.returncode = 1
    mock_result.stderr = "connection refused"

    with patch("subprocess.run", return_value=mock_result):
        result = plasmate_fetch("https://example.com")
        assert "Error:" in result


def test_fetch_not_installed():
    with patch("subprocess.run", side_effect=FileNotFoundError):
        result = plasmate_fetch("https://example.com")
        assert "not installed" in result


def test_fetch_timeout():
    with patch("subprocess.run", side_effect=subprocess.TimeoutExpired(cmd="plasmate", timeout=30)):
        result = plasmate_fetch("https://example.com")
        assert "Timeout" in result
