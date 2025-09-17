import json
import shutil
import importlib.resources

from .logging import logger
from .file_utils import QWEN_DIR, get_package_files

def install_commands():
    logger.info("Installing Commands...")
    commands_dst = QWEN_DIR / "commands" / "sq"
    commands_dst.mkdir(parents=True, exist_ok=True)
    files = get_package_files("commands")
    count = 0
    for file in files:
        if file.name.endswith('.toml'):
            with importlib.resources.as_file(file) as src_path:
                shutil.copy2(src_path, commands_dst)
                count += 1
    logger.info(f"Copied {count} command files.")

def install_modes():
    logger.info("Installing Modes...")
    modes_dst = QWEN_DIR / "modes"
    modes_dst.mkdir(exist_ok=True)
    files = get_package_files("modes")
    count = 0
    for file in files:
        if file.name.endswith('.md'):
            with importlib.resources.as_file(file) as src_path:
                shutil.copy2(src_path, modes_dst)
                count += 1
    logger.info(f"Copied {count} mode files.")

def install_agents():
    logger.info("Installing Agents...")
    agents_dst = QWEN_DIR / "agents"
    agents_dst.mkdir(exist_ok=True)
    files = get_package_files("agents")
    count = 0
    for file in files:
        if file.name.endswith('.md'):
            with importlib.resources.as_file(file) as src_path:
                shutil.copy2(src_path, agents_dst)
                count += 1
    logger.info(f"Copied {count} agent files.")

def install_mcp():
    logger.info("Installing MCP Config...")
    settings_file = QWEN_DIR / "settings.json"
    default_settings = {
        "mcpServers": {
            "serena": {"command": "serena-mcp-server", "args": ["--context", "ide-assistant", "--project", "/path/to/your/project"]},
            "context7": {"command": "npx", "args": ["-y", "@upstash/context7-mcp@latest"]},
            "sequential": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]}
        }
    }
    with open(settings_file, "w") as f:
        json.dump(default_settings, f, indent=2)
    logger.info("Configured MCP servers.")

INSTALL_MAP = {
    "commands": install_commands,
    "modes": install_modes,
    "agents": install_agents,
    "mcp": install_mcp,
}
