import shutil

from .logging import logger
from .file_utils import QWEN_DIR, get_package_files

def uninstall_commands():
    logger.info("Uninstalling Commands...")
    commands_dir = QWEN_DIR / "commands" / "sq"
    if commands_dir.exists():
        shutil.rmtree(commands_dir)
        logger.info("Removed commands directory.")
    else:
        logger.warning("Commands directory not found, skipping.")

def uninstall_modes():
    logger.info("Uninstalling Modes...")
    modes_dir = QWEN_DIR / "modes"
    if modes_dir.exists():
        files = get_package_files("modes")
        count = 0
        for file in files:
            if file.name.endswith('.md'):
                target_file = modes_dir / file.name
                if target_file.exists():
                    target_file.unlink()
                    count += 1
        logger.info(f"Removed {count} mode files.")
    else:
        logger.warning("Modes directory not found, skipping.")

def uninstall_agents():
    logger.info("Uninstalling Agents...")
    agents_dir = QWEN_DIR / "agents"
    if agents_dir.exists():
        files = get_package_files("agents")
        count = 0
        for file in files:
            if file.name.endswith('.md'):
                target_file = agents_dir / file.name
                if target_file.exists():
                    target_file.unlink()
                    count += 1
        logger.info(f"Removed {count} agent files.")
    else:
        logger.warning("Agents directory not found, skipping.")

def uninstall_mcp():
    logger.info("Uninstalling MCP Config...")
    settings_file = QWEN_DIR / "settings.json"
    if settings_file.exists():
        settings_file.unlink()
        logger.info("Removed MCP settings file.")
    else:
        logger.warning("MCP settings file not found, skipping.")

UNINSTALL_MAP = {
    "commands": uninstall_commands,
    "modes": uninstall_modes,
    "agents": uninstall_agents,
    "mcp": uninstall_mcp,
}
