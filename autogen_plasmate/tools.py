"""Plasmate tool for AutoGen agents."""

import subprocess
import json


def plasmate_fetch(url: str) -> str:
    """Fetch a web page using Plasmate and return semantic content (SOM).

    Uses 10-16x fewer tokens than Chrome for web content extraction.

    Args:
        url: The URL to fetch.

    Returns:
        Semantic Object Model (SOM) representation of the page content.
    """
    try:
        result = subprocess.run(
            ["plasmate", "fetch", url],
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    except FileNotFoundError:
        return "Plasmate not installed. Run: pip install plasmate"
    except subprocess.TimeoutExpired:
        return f"Timeout fetching {url}"
