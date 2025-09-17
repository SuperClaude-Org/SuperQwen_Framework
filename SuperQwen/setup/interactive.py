import time
import typer
import questionary
from rich.console import Console
from rich.progress import Progress

from .installer import INSTALL_MAP
from .uninstaller import UNINSTALL_MAP

console = Console()

def handle_interactive_install():
    """Handles the interactive installation prompt."""
    console.print("[bold]Welcome to the SuperQwen interactive installer![/bold]")

    choices = questionary.checkbox(
        "Select the components you want to install:",
        choices=[
            questionary.Choice("Commands", checked=True),
            questionary.Choice("Modes", checked=True),
            questionary.Choice("Agents", checked=True),
            questionary.Choice("MCP Config", checked=False),
        ]
    ).ask()

    if not choices:
        console.print("[warning]No components selected. Exiting.[/warning]")
        raise typer.Exit()

    selected_components = [c.lower().split()[0] for c in choices]

    with Progress(console=console) as progress:
        task = progress.add_task("[green]Installing...", total=len(selected_components))
        for component in selected_components:
            if component in INSTALL_MAP:
                INSTALL_MAP[component]()
                time.sleep(0.3)
                progress.update(task, advance=1)

    console.print("\n[success]✅ Interactive installation complete![/success]")

def handle_interactive_uninstall():
    """Handles the interactive uninstallation prompt."""
    console.print("[bold]Welcome to the SuperQwen interactive uninstaller![/bold]")

    choices = questionary.checkbox(
        "Select the components you want to uninstall:",
        choices=[
            questionary.Choice("Commands"),
            questionary.Choice("Modes"),
            questionary.Choice("Agents"),
            questionary.Choice("MCP Config"),
        ]
    ).ask()

    if not choices:
        console.print("[warning]No components selected. Exiting.[/warning]")
        raise typer.Exit()

    selected_components = [c.lower().split()[0] for c in choices]

    with Progress(console=console) as progress:
        task = progress.add_task("[red]Uninstalling...", total=len(selected_components))
        for component in selected_components:
            if component in UNINSTALL_MAP:
                UNINSTALL_MAP[component]()
                time.sleep(0.3)
                progress.update(task, advance=1)

    console.print("\n[success]✅ Interactive uninstallation complete![/success]")
