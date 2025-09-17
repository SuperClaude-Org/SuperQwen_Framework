import sys
import typer
from rich.console import Console
from rich.theme import Theme
from rich.progress import Progress
from typing_extensions import Annotated

from .. import __version__
from .logging import logger
from .installer import INSTALL_MAP, install_commands, install_modes, install_agents, install_mcp
from .uninstaller import UNINSTALL_MAP, uninstall_commands, uninstall_modes, uninstall_agents, uninstall_mcp
import subprocess
from .interactive import handle_interactive_install, handle_interactive_uninstall

# --- Setup ---
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red",
    "success": "bold green",
})
console = Console(theme=custom_theme)
COMPONENTS = ["commands", "modes", "agents", "mcp"]

def get_banner():
    name = "SuperQwen_Framework"
    version = f"version {__version__}"
    width = max(len(name), len(version)) + 4
    banner = (
        f"[bold cyan]{'=' * width}[/bold cyan]\n"
        f"[bold cyan]  {name.center(width - 4)}  [/bold cyan]\n"
        f"[dim cyan]  {version.center(width - 4)}  [/dim cyan]\n"
        f"[bold cyan]{'=' * width}[/bold cyan]"
    )
    return banner

app = typer.Typer(
    name="superqwen",
    help="SuperQwen Framework CLI - A tool to manage your Qwen CLI enhancements.",
    add_completion=False,
    rich_markup_mode="rich",
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
        console.print(get_banner())
        handle_interactive_install()

@install_app.command("all")
def install_all_cmd():
    """Install all framework components."""
    console.print(get_banner())
    with Progress(console=console) as progress:
        task = progress.add_task("[green]Installing all components...", total=len(COMPONENTS))
        for component in COMPONENTS:
            INSTALL_MAP[component]()
            progress.update(task, advance=1)
    console.print("\n[success]✅ All components installed successfully![/success]")

@install_app.command("commands")
def install_commands_cmd():
    """Install only the Commands."""
    install_commands()

@install_app.command("modes")
def install_modes_cmd():
    """Install only the Modes."""
    install_modes()

@install_app.command("agents")
def install_agents_cmd():
    """Install only the Agents."""
    install_agents()

@install_app.command("mcp")
def install_mcp_cmd():
    """Install only the MCP Config."""
    install_mcp()

# --- Uninstall Commands ---

@uninstall_app.callback(invoke_without_command=True)
def uninstall_main(ctx: typer.Context):
    """
    Uninstall SuperQwen components. Run without a subcommand for an interactive menu.
    """
    if ctx.invoked_subcommand is None:
        console.print(get_banner())
        handle_interactive_uninstall()

@uninstall_app.command("all")
def uninstall_all_cmd():
    """Uninstall all framework components."""
    console.print(get_banner())
    with Progress(console=console) as progress:
        task = progress.add_task("[red]Uninstalling all components...", total=len(COMPONENTS))
        for component in COMPONENTS:
            UNINSTALL_MAP[component]()
            progress.update(task, advance=1)
    console.print("\n[success]✅ All components uninstalled successfully![/success]")

@uninstall_app.command("commands")
def uninstall_commands_cmd():
    """Uninstall only the Commands."""
    uninstall_commands()

@uninstall_app.command("modes")
def uninstall_modes_cmd():
    """Uninstall only the Modes."""
    uninstall_modes()

@uninstall_app.command("agents")
def uninstall_agents_cmd():
    """Uninstall only the Agents."""
    uninstall_agents()

@uninstall_app.command("mcp")
def uninstall_mcp_cmd():
    """Uninstall only the MCP Config."""
    uninstall_mcp()

@app.command()
def update():
    """
    Update the SuperQwen package to the latest version from PyPI.
    """
    console.print("[bold green]🚀 Checking for updates...[/bold green]")
    with console.status("[bold green]Running pip install --upgrade SuperQwen...") as status:
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "--upgrade", "SuperQwen"],
                capture_output=True, text=True, check=True
            )
            logger.info(result.stdout)
            console.print("[bold green]✅ SuperQwen updated successfully![/bold green]")
        except subprocess.CalledProcessError as e:
            logger.error("Update failed!")
            logger.error(e.stderr)
            console.print("[bold red]❌ Update failed. See logs for details.[/bold red]")

# --- Main entry point ---
def main():
    app()

if __name__ == "__main__":
    main()
