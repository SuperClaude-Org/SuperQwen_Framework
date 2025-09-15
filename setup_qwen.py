#!/usr/bin/env python3
"""
Qwen Framework Setup Script
"""

import os
import sys
import json
from pathlib import Path

def setup_qwen_framework():
    """Setup Qwen framework with default configuration"""
    # Get the .qwen directory
    qwen_dir = Path(".qwen").absolute()
    qwen_dir.mkdir(exist_ok=True)
    
    # Create or update settings.json
    settings_file = qwen_dir / "settings.json"
    
    # Default settings with MCP servers
    default_settings = {
        "mcpServers": {
            "serena": {
            "command": "serena-mcp-server",
            "args": [
                "--context",
                "ide-assistant",
                "--project",
                "/home/mkh0813/transfer_server_all"
            ]
            },
            "context7": {
            "command": "npx",
            "args": [
                "-y",
                "@upstash/context7-mcp@latest"
            ]
            },
            "sequential": {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-sequential-thinking"
            ]
            }
  }
    }
    
    # Write settings
    with open(settings_file, "w") as f:
        json.dump(default_settings, f, indent=2)
    
    print(f"✅ Qwen Framework settings configured at {settings_file}")
    print("\nMCP Servers configured:")
    for server in default_settings["mcpServers"]:
        print(f"  - {server}")

if __name__ == "__main__":
    setup_qwen_framework()