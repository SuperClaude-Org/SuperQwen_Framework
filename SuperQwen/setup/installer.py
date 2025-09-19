import json
import shutil
import subprocess
import importlib.resources
from typing import Optional

from .logging import logger
from .file_utils import QWEN_DIR, get_package_files
from .ui import ProgressBar

def install_commands(progress_bar: Optional[ProgressBar] = None):
    logger.info("Installing Commands...")
    commands_dst = QWEN_DIR / "commands" / "sq"
    commands_dst.mkdir(parents=True, exist_ok=True)

    files = get_package_files("commands")
    files_to_copy = [f for f in files if f.name.endswith('.toml')]

    if progress_bar:
        progress_bar.total = len(files_to_copy)

    for i, file in enumerate(files_to_copy):
        with importlib.resources.as_file(file) as src_path:
            shutil.copy2(src_path, commands_dst)
        if progress_bar:
            progress_bar.update(i + 1)

    logger.info(f"Copied {len(files_to_copy)} command files.")

def install_modes(progress_bar: Optional[ProgressBar] = None):
    logger.info("Installing Modes...")
    modes_dst = QWEN_DIR / "modes"
    modes_dst.mkdir(exist_ok=True)

    files = get_package_files("modes")
    files_to_copy = [f for f in files if f.name.endswith('.md')]

    if progress_bar:
        progress_bar.total = len(files_to_copy)

    for i, file in enumerate(files_to_copy):
        with importlib.resources.as_file(file) as src_path:
            shutil.copy2(src_path, modes_dst)
        if progress_bar:
            progress_bar.update(i + 1)

    logger.info(f"Copied {len(files_to_copy)} mode files.")

def install_agents(progress_bar: Optional[ProgressBar] = None):
    logger.info("Installing Agents...")
    agents_dst = QWEN_DIR / "agents"
    agents_dst.mkdir(exist_ok=True)

    files = get_package_files("agents")
    files_to_copy = [f for f in files if f.name.endswith('.md')]

    if progress_bar:
        progress_bar.total = len(files_to_copy)

    for i, file in enumerate(files_to_copy):
        with importlib.resources.as_file(file) as src_path:
            shutil.copy2(src_path, agents_dst)
        if progress_bar:
            progress_bar.update(i + 1)

    logger.info(f"Copied {len(files_to_copy)} agent files.")

def _verify_npx_package(package_arg: str) -> bool:
    """Verifies if an npx package is available in the npm registry."""
    if not shutil.which("npm"):
        logger.warning("`npm` command not found, cannot verify npx packages.")
        return False

    package_name = package_arg.split('@')[1] if '@' in package_arg else package_arg
    logger.info(f"    - Verifying npm package '{package_name}'...")
    try:
        result = subprocess.run(
            ["npm", "view", package_name, "version"],
            capture_output=True, text=True, check=True
        )
        return result.returncode == 0 and result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        logger.warning(f"    - npm package '{package_name}' not found in registry.")
        return False

def install_mcp(progress_bar: Optional[ProgressBar] = None):
    logger.info("Installing MCP Config...")
    settings_file = QWEN_DIR / "settings.json"

    default_mcp_servers = {
        "serena": {"command": "serena-mcp-server", "args": ["--context", "ide-assistant", "--project", "/path/to/your/project"]},
        "context7": {"command": "npx", "args": ["-y", "@upstash/context7-mcp@latest"]},
        "sequential": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]}
    }

    if progress_bar:
        progress_bar.total = len(default_mcp_servers)

    verified_mcp_servers = {}
    progress_step = 0

    for name, config in default_mcp_servers.items():
        command_to_check = config["command"]
        if shutil.which(command_to_check):
            is_verified = True
            if command_to_check == "npx":
                npx_package_arg = next((arg for arg in config["args"] if arg.startswith('@')), None)
                if npx_package_arg:
                    is_verified = _verify_npx_package(npx_package_arg)

            if is_verified:
                logger.info(f"  ✓ Detected and verified '{command_to_check}', adding '{name}' to config.")
                verified_mcp_servers[name] = config
            else:
                logger.warning(f"  - Verification failed for '{name}', skipping.")
        else:
            logger.warning(f"  - Command '{command_to_check}' not found, skipping '{name}'.")

        progress_step += 1
        if progress_bar:
            progress_bar.update(progress_step)

    if not verified_mcp_servers:
        logger.warning("No MCP servers could be verified. Skipping settings.json creation.")
        return

    final_settings = {"mcpServers": verified_mcp_servers}

    with open(settings_file, "w") as f:
        json.dump(final_settings, f, indent=2)
    logger.info("Configured verified MCP servers.")

INSTALL_MAP = {
    "commands": install_commands,
    "modes": install_modes,
    "agents": install_agents,
    "mcp": install_mcp,
}
