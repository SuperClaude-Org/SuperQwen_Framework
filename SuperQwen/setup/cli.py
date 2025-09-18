import sys
import typer
import subprocess
import time
from typing_extensions import Annotated

from .. import __version__
from .logging import logger
from .installer import INSTALL_MAP
from .uninstaller import UNINSTALL_MAP
from . import ui
from .interactive import handle_interactive_install, handle_interactive_uninstall

# --- Setup ---
COMPONENTS = ["commands", "modes", "agents", "mcp"]

app = typer.Typer(
    name="superqwen",
    help="SuperQwen Framework CLI - A tool to manage your Qwen CLI enhancements.",
    add_completion=False,
    rich_markup_mode="rich", # This can stay, Typer uses it for its own help formatting
)
install_app = typer.Typer(name="install", help="Install framework components.")
uninstall_app = typer.Typer(name="uninstall", help="Uninstall framework components.")
app.add_typer(install_app)
app.add_typer(uninstall_app)

# --- Install Commands ---

@install_app.callback(invoke_without_command=True)
def install_main(ctx: typer.Context):
    """
    Install SuperQwen components. Run without a subcommand for an interactive menu.
    """
    if ctx.invoked_subcommand is None:
        handle_interactive_install()

@install_app.command("all")
def install_all_cmd():
    """Install all framework components."""
    ui.display_header("SuperQwen Installer", "Installing All Components")

    total_components = len(COMPONENTS)
    for i, component in enumerate(COMPONENTS, 1):
        ui.display_step(i, total_components, f"Installing {component}...")

        progress_bar = ui.ProgressBar(100, prefix=f"{component.capitalize()}: ")
        INSTALL_MAP[component]() # Call the actual install function
        for j in range(101):
            time.sleep(0.01)
            progress_bar.update(j)
        progress_bar.finish()

    ui.display_success("\n✅ All components installed successfully!")

@install_app.command("commands")
def install_commands_cmd():
    """Install only the Commands."""
    INSTALL_MAP["commands"]()
    ui.display_success("Commands installed.")

@install_app.command("modes")
def install_modes_cmd():
    """Install only the Modes."""
    INSTALL_MAP["modes"]()
    ui.display_success("Modes installed.")

@install_app.command("agents")
def install_agents_cmd():
    """Install only the Agents."""
    INSTALL_MAP["agents"]()
    ui.display_success("Agents installed.")

@install_app.command("mcp")
def install_mcp_cmd():
    """Install only the MCP Config."""
    INSTALL_MAP["mcp"]()
    ui.display_success("MCP Config installed.")

# --- Uninstall Commands ---

@uninstall_app.callback(invoke_without_command=True)
def uninstall_main(ctx: typer.Context):
    """
    Uninstall SuperQwen components. Run without a subcommand for an interactive menu.
    """
    if ctx.invoked_subcommand is None:
        handle_interactive_uninstall()

@uninstall_app.command("all")
def uninstall_all_cmd():
    """Uninstall all framework components."""
    ui.display_header("SuperQwen Uninstaller", "Uninstalling All Components")

    total_components = len(COMPONENTS)
    for i, component in enumerate(COMPONENTS, 1):
        ui.display_step(i, total_components, f"Uninstalling {component}...")

        progress_bar = ui.ProgressBar(100, prefix=f"{component.capitalize()}: ")
        UNINSTALL_MAP[component]() # Call the actual uninstall function
        for j in range(101):
            time.sleep(0.01)
            progress_bar.update(j)
        progress_bar.finish()

    ui.display_success("\n✅ All components uninstalled successfully!")

@uninstall_app.command("commands")
def uninstall_commands_cmd():
    """Uninstall only the Commands."""
    UNINSTALL_MAP["commands"]()
    ui.display_success("Commands uninstalled.")

@uninstall_app.command("modes")
def uninstall_modes_cmd():
    """Uninstall only the Modes."""
    UNINSTALL_MAP["modes"]()
    ui.display_success("Modes uninstalled.")

@uninstall_app.command("agents")
def uninstall_agents_cmd():
    """Uninstall only the Agents."""
    UNINSTALL_MAP["agents"]()
    ui.display_success("Agents uninstalled.")

@uninstall_app.command("mcp")
def uninstall_mcp_cmd():
    """Uninstall only the MCP Config."""
    UNINSTALL_MAP["mcp"]()
    ui.display_success("MCP Config uninstalled.")

@app.command()
def update():
    """
    Update the SuperQwen package to the latest version from PyPI.
    """
    ui.display_info("🚀 Checking for updates...")
    spinner = ui.StatusSpinner("Running pip install --upgrade SuperQwen...")
    spinner.start()
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "SuperQwen"],
            capture_output=True, text=True, check=True
        )
        logger.info(result.stdout)
        spinner.stop()
        ui.display_success("✅ SuperQwen updated successfully!")
    except subprocess.CalledProcessError as e:
        logger.error("Update failed!")
        logger.error(e.stderr)
        spinner.stop()
        ui.display_error("❌ Update failed. See logs for details.")

# --- Main entry point ---
def main():
    app()

if __name__ == "__main__":
    main()
