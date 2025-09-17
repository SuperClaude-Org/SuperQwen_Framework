# SuperQwen Framework

SuperQwen is an AI-enhanced development framework designed to supercharge your command-line workflow, forked from the original SuperClaude/SuperGemini projects. It provides structured development capabilities with a powerful command-line interface, specialized AI agents, and behavioral modes.

![SuperQwen CLI](https://user-images.githubusercontent.com/12345/some-image.png) <!-- Placeholder for a future screenshot -->

## Features

- **Modern CLI**: A polished and user-friendly command-line interface built with Typer and Rich.
- **Granular Installation**: Install and uninstall exactly the components you need (`commands`, `modes`, `agents`, `mcp`) or all at once.
- **Interactive Mode**: Run `superqwen install` for a guided, interactive setup experience.
- **Self-Updating**: Keep your framework up-to-date with the simple `superqwen update` command.
- **18 Slash Commands**: TOML-based commands for systematic workflow automation (`/analyze`, `/implement`, etc.).
- **Behavioral Modes**: Context-aware operation modes (Brainstorming, Introspection, etc.).
- **13 Specialized AI Agents**: Domain experts to assist with various development tasks.

## Installation

Install the framework directly from PyPI:

```bash
pip install SuperQwen
```

After installation, set up the framework components:

```bash
# Run the interactive installer to choose components
superqwen install

# Or, install all components at once
superqwen install all
```

## Usage

The SuperQwen CLI (`superqwen`) is the main entry point for managing your framework installation.

### Core Commands

- **`superqwen install [component]`**: Install components.
  - `superqwen install all`: Install everything.
  - `superqwen install commands`: Install just the commands.
  - `superqwen install`: Launch the interactive installer.
- **`superqwen uninstall [component]`**: Uninstall components.
- **`superqwen update`**: Update the framework to the latest version.
- **`superqwen --help`**: Get help on any command or subcommand.

Once installed, you can use the slash commands (e.g., `/sq:analyze`, `/sq:implement`) and modes within your Qwen CLI session.

## Uninstallation

You can uninstall components gracefully:

```bash
# Run the interactive uninstaller
superqwen uninstall

# Or, uninstall all components at once
superqwen uninstall all
```

To completely remove the package from your system:
```bash
pip uninstall SuperQwen
```

---

### Acknowledgment

This framework was originally forked from the **SuperGemini Framework**. We sincerely thank the **SuperClaude Team** for their outstanding work, which served as the foundation and inspiration for this project.

- https://github.com/SuperClaude-Org/SuperClaude_Framework
- https://github.com/SuperClaude-Org/SuperGemini_Framework
