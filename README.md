# SuperQwen Framework

[![PyPI version](https://img.shields.io/pypi/v/SuperQwen.svg)](https://pypi.org/project/SuperQwen/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python versions](https://img.shields.io/pypi/pyversions/SuperQwen.svg)](https://pypi.org/project/SuperQwen/)

SuperQwen is an AI-enhanced development framework designed to supercharge your command-line workflow, forked from the original SuperClaude/SuperGemini projects. It provides structured development capabilities with a powerful command-line interface, specialized AI agents, and behavioral modes.

## Why SuperQwen?

- **Modern & User-Friendly**: A polished and intuitive command-line interface built with Typer and Rich.
- **Granular Control**: Install and uninstall exactly the components you need (`commands`, `modes`, `agents`, etc.).
- **Interactive Experience**: Run `superqwen install` for a guided, interactive setup.
- **Self-Updating**: Keep your framework up-to-date with a simple `superqwen update` command.
- **Extensible**: Easily add your own commands, agents, and modes to customize your workflow.

---

## Installation

Install the framework directly from PyPI:

```bash
pip install SuperQwen
```

After installation, set up the framework components using the interactive installer:

```bash
superqwen install
```
This will present you with a checklist of components to install.

---

## Usage

The SuperQwen CLI (`superqwen`) is the main entry point for managing your framework.

### CLI Screenshot

Here's a glimpse of the installer in action:
```
$ superqwen install all

 =======================
  SuperQwen_Framework
    version 4.1.0-b2
=======================
[13:52:01] INFO     Installing Commands...
           INFO     Copied 18 command files.
           INFO     Installing Modes...
           INFO     Copied 5 mode files.
           INFO     Installing Agents...
           INFO     Copied 13 agent files.
           INFO     Installing MCP Config...
           INFO     Configured verified MCP servers.
Installing all components... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00

✅ All components installed successfully!
```

### Core Commands

- **`superqwen install [component]`**: Install components.
  - `superqwen install all`: Install everything non-interactively.
  - `superqwen install commands`: Install just the commands.
  - `superqwen install`: Launch the interactive installer (recommended).
- **`superqwen uninstall [component]`**: Uninstall components.
  - `superqwen uninstall all`: Uninstall everything non-interactively.
  - `superqwen uninstall`: Launch the interactive uninstaller.
- **`superqwen update`**: Update the framework to the latest version from PyPI.
- **`superqwen --help`**: Get help on any command or subcommand.

Once installed, you can use the slash commands (e.g., `/sq:analyze`, `/sq:implement`) and modes within your Qwen CLI session.

---

## Contributing

Contributions are welcome! Whether it's reporting a bug, suggesting a feature, or submitting a pull request, your help is appreciated. Please see the `CONTRIBUTING.md` file for more details on how to get started.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgment

This framework was originally forked from the **SuperGemini Framework**. We sincerely thank the **SuperClaude Team** for their outstanding work, which served as the foundation and inspiration for this project.

- https://github.com/SuperClaude-Org/SuperClaude_Framework
- https://github.com/SuperClaude-Org/SuperGemini_Framework
