import time
import typer

from . import ui
from .installer import INSTALL_MAP
from .uninstaller import UNINSTALL_MAP

def handle_interactive_install():
    """Handles the interactive installation prompt using the custom UI."""
    ui.display_header("SuperQwen Installer", "Interactive Setup")

    menu_options = [
        "Core Components (Commands, Modes, Agents)",
        "MCP Config (for advanced users)",
        "All of the above"
    ]

    # We can simplify the choices a bit for the single-choice menu
    install_menu = ui.Menu("Installation Options", menu_options)
    choice = install_menu.display()

    if choice == -1:
        ui.display_warning("Installation cancelled.")
        raise typer.Exit()

    tasks_to_run = []
    if choice == 0: # Core
        tasks_to_run.extend(['commands', 'modes', 'agents'])
    elif choice == 1: # MCP
        tasks_to_run.append('mcp')
    elif choice == 2: # All
        tasks_to_run.extend(['commands', 'modes', 'agents', 'mcp'])

    if not tasks_to_run:
        ui.display_warning("No components selected. Exiting.")
        raise typer.Exit()

    if ui.confirm(f"Ready to install the selected components?"):
        ui.display_info("Starting installation...")
        total_tasks = len(tasks_to_run)

        for i, component in enumerate(tasks_to_run, 1):
            if component in INSTALL_MAP:
                ui.display_step(i, total_tasks, f"Installing {component}...")

                # Simulate work with a progress bar
                progress_bar = ui.ProgressBar(100, prefix=f"{component.capitalize()}: ")
                INSTALL_MAP[component]() # Call the actual install function
                for j in range(101):
                    time.sleep(0.01)
                    progress_bar.update(j)
                progress_bar.finish()

        ui.display_success("\n✅ Interactive installation complete!")
    else:
        ui.display_warning("Installation aborted by user.")


def handle_interactive_uninstall():
    """Handles the interactive uninstallation prompt using the custom UI."""
    ui.display_header("SuperQwen Uninstaller", "Interactive Removal")

    menu_options = [
        "Core Components (Commands, Modes, Agents)",
        "MCP Config",
        "All of the above"
    ]

    uninstall_menu = ui.Menu("Uninstallation Options", menu_options)
    choice = uninstall_menu.display()

    if choice == -1:
        ui.display_warning("Uninstallation cancelled.")
        raise typer.Exit()

    tasks_to_run = []
    if choice == 0: # Core
        tasks_to_run.extend(['commands', 'modes', 'agents'])
    elif choice == 1: # MCP
        tasks_to_run.append('mcp')
    elif choice == 2: # All
        tasks_to_run.extend(['commands', 'modes', 'agents', 'mcp'])

    if not tasks_to_run:
        ui.display_warning("No components selected. Exiting.")
        raise typer.Exit()

    if ui.confirm(f"Are you sure you want to uninstall these components?", default=False):
        ui.display_info("Starting uninstallation...")
        total_tasks = len(tasks_to_run)

        for i, component in enumerate(tasks_to_run, 1):
            if component in UNINSTALL_MAP:
                ui.display_step(i, total_tasks, f"Uninstalling {component}...")

                # Simulate work with a progress bar
                progress_bar = ui.ProgressBar(100, prefix=f"{component.capitalize()}: ")
                UNINSTALL_MAP[component]() # Call the actual uninstall function
                for j in range(101):
                    time.sleep(0.01)
                    progress_bar.update(j)
                progress_bar.finish()

        ui.display_success("\n✅ Interactive uninstallation complete!")
    else:
        ui.display_warning("Uninstallation aborted by user.")
