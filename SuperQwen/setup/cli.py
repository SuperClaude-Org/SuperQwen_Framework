import sys
import typer
import subprocess
from typing import Optional
from typing_extensions import Annotated

from .. import __version__
from .logging import logger
from .installer import INSTALL_MAP
from .uninstaller import UNINSTALL_MAP
from . import ui
from .interactive import handle_interactive_install, handle_interactive_uninstall

# --- Setup ---
COMPONENTS = ["commands", "modes", "agents", "mcp"]

def version_callback(value: bool):
    if value:
        ui.display_info(f"SuperQwen Framework Version: {__version__}")
        raise typer.Exit()

app = typer.Typer(
    name="superqwen",
    help="SuperQwen Framework CLI - A tool to manage your Qwen CLI enhancements.",
    add_completion=False,
)

@app.callback(invoke_without_command=True)
def main_callback(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=version_callback,
        is_eager=True,
    ),
    help_flag: Optional[bool] = typer.Option(
        None,
        "--help",
        "-h",
        help="Show the help message and exit.",
        is_eager=True,
    )
):
    """
    Manage the SuperQwen Framework.
    """
    if help_flag:
        help() # Call the custom help command
        raise typer.Exit()

    if ctx.invoked_subcommand is None:
        help() # Show help if no command is provided

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

        # Create a progress bar with a dummy total, the installer function will set the real total.
        progress_bar = ui.ProgressBar(1, prefix=f"{component.capitalize()}: ")
        INSTALL_MAP[component](progress_bar=progress_bar) # Pass the progress bar
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

        # We can't show real progress for uninstall, so we'll keep the simulation here
        progress_bar = ui.ProgressBar(100, prefix=f"{component.capitalize()}: ")
        UNINSTALL_MAP[component]()
        for j in range(101):
            import time
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
def help():
    """Show this message and exit."""
    ui.display_header("SuperQwen Framework", f"Version {__version__}")

    ui.display_info("Usage: superqwen [OPTIONS] COMMAND [ARGS]...")

    core_headers = ["Command", "Description"]
    core_rows = [
        ["install", "Install framework components (run interactively)."],
        ["install all", "Install all components non-interactively."],
        ["uninstall", "Uninstall framework components (run interactively)."],
        ["uninstall all", "Uninstall all components non-interactively."],
        ["update", "Update the SuperQwen package to the latest version."],
        ["help, --help, -h", "Show this help message."],
        ["--version, -v", "Show the application's version and exit."],
    ]
    ui.display_table(core_headers, core_rows, title="Core Commands")

    sq_headers = ["Slash Command", "Description"]
    sq_rows = [
        ["/sq:analyze", "Comprehensive code analysis."],
        ["/sq:build", "Build, compile, and package projects."],
        ["/sq:cleanup", "Clean up code and optimize project structure."],
        ["/sq:design", "Design system architecture and interfaces."],
        ["/sq:document", "Generate focused documentation."],
        ["/sq:estimate", "Provide development estimates for tasks."],
        ["/sq:explain", "Provide clear explanations of code and concepts."],
        ["/sq:git", "Git operations with intelligent commit messages."],
        ["/sq:help", "List all available /sq commands."],
        ["/sq:implement", "Feature and code implementation."],
        ["/sq:improve", "Apply systematic improvements to code."],
        ["/sq:index", "Generate comprehensive project documentation."],
        ["/sq:load", "Load session context via MCP."],
        ["/sq:reflect", "Task reflection and validation via MCP."],
        ["/sq:save", "Persist session context via MCP."],
        ["/sq:select-tool", "Intelligent MCP tool selection."],
        ["/sq:test", "Execute tests with coverage analysis."],
        ["/sq:troubleshoot", "Diagnose and resolve issues."],
    ]
    ui.display_table(sq_headers, sq_rows, title="Available /sq Commands")
    ui.display_warning("Note: /sq commands do not accept flags. All text following the command is treated as a single prompt.")

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
