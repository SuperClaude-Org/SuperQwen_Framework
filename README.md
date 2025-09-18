# SuperQwen Framework

[![PyPI version](https://img.shields.io/pypi/v/SuperQwen.svg)](https://pypi.org/project/SuperQwen/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python versions](https://img.shields.io/pypi/pyversions/SuperQwen.svg)](https://pypi.org/project/SuperQwen/)

**SuperQwen is an AI-enhanced development framework designed to supercharge your command-line workflow.**

Forked from the original SuperClaude/SuperGemini projects, SuperQwen provides structured development capabilities with a powerful command-line interface, specialized AI agents, and behavioral modes to streamline your development process.

## Key Features

*   **✨ Modern & User-Friendly UI**: A polished and intuitive command-line interface with a custom UI for a consistent experience.
*   **🧩 Modular Components**: Install and uninstall exactly the components you need (`commands`, `modes`, `agents`, etc.).
*   **🤖 Interactive Experience**: Run `superqwen install` for a guided, interactive setup to get you started in seconds.
*   **🚀 Self-Updating**: Keep your framework up-to-date with a simple `superqwen update` command.
*   **🔧 Extensible by Design**: Easily add your own commands, agents, and modes to customize your workflow.
*   **🧠 Intelligent MCP Integration**: Leverages the Model Context Protocol (MCP) for advanced, context-aware AI interactions.

---

## Installation

Install the framework directly from PyPI using pip:

```bash
pip install SuperQwen
```

After installation, it is highly recommended to run the interactive setup to install the core components:

```bash
superqwen install
```

This will launch the interactive installer, allowing you to choose which components to set up.

### Installer Preview

Here's a glimpse of the installer in action:

```
$ superqwen install

============================================================
                    SuperQwen Installer
                     Interactive Setup
NomenAK <anton.knoery@gmail.com> | Mithun Gowda B <mithungowda.b7411@gmail.com>
============================================================


Installation Options
====================
1. Core Components (Commands, Modes, Agents)
2. MCP Config (for advanced users)
3. All of the above

Enter your choice (1-3):
> 3
Ready to install the selected components? [Y/n]
> y
[INFO] Starting installation...
[1/4] Installing commands...
Commands: [██████████████████████████████████████████████████] 100.0% Complete
[2/4] Installing modes...
Modes:    [██████████████████████████████████████████████████] 100.0% Complete
[3/4] Installing agents...
Agents:   [██████████████████████████████████████████████████] 100.0% Complete
[4/4] Installing mcp...
Mcp:      [██████████████████████████████████████████████████] 100.0% Complete

✅ Interactive installation complete!
```

---

## Usage

The `superqwen` CLI is the main entry point for managing your framework.

### Core Commands

| Command                             | Description                                           |
| ----------------------------------- | ----------------------------------------------------- |
| `superqwen install`                 | Launch the interactive installer.                     |
| `superqwen install all`             | Install all components non-interactively.             |
| `superqwen install [component]`     | Install a specific component (e.g., `commands`).      |
| `superqwen uninstall`               | Launch the interactive uninstaller.                   |
| `superqwen uninstall all`           | Uninstall all components non-interactively.           |
| `superqwen uninstall [component]`   | Uninstall a specific component.                       |
| `superqwen update`                  | Update the framework to the latest version from PyPI. |
| `superqwen --help`                  | Get help on any command or subcommand.                |


### Available `/sq` Commands

Once installed, you can use the following slash commands (`/sq:*`) within your Qwen CLI session to leverage the power of SuperQwen's AI agents.

> **Note:** These commands do not currently accept flags (e.g., `--verbose`). All text following the command is treated as a single, continuous prompt for the AI.

| Command         | Description                                                                          |
| --------------- | ------------------------------------------------------------------------------------ |
| `/sq:analyze`   | Comprehensive code analysis (quality, security, performance, architecture).          |
| `/sq:build`     | Build, compile, and package projects with intelligent error handling.                |
| `/sq:cleanup`   | Systematically clean up code, remove dead code, and optimize project structure.      |
| `/sq:design`    | Design system architecture, APIs, and component interfaces.                          |
| `/sq:document`  | Generate focused documentation for components, functions, APIs, and features.        |
| `/sq:estimate`  | Provide development estimates for tasks, features, or projects.                      |
| `/sq:explain`   | Provide clear explanations of code, concepts, and system behavior.                   |
| `/sq:git`       | Git operations with intelligent commit messages and workflow optimization.           |
| `/sq:help`      | List all available `/sq` commands and their functionality.                           |
| `/sq:implement` | Feature and code implementation with intelligent persona activation.                 |
| `/sq:improve`   | Apply systematic improvements to code quality, performance, and maintainability.     |
| `/sq:index`     | Generate comprehensive project documentation and a knowledge base.                   |
| `/sq:load`      | Session lifecycle management for loading project context via MCP.                    |
| `/sq:reflect`   | Task reflection and validation using MCP analysis capabilities.                      |
| `/sq:save`      | Session lifecycle management for persisting session context via MCP.                 |
| `/sq:select-tool` | Intelligent MCP tool selection based on complexity scoring and operation analysis.   |
| `/sq:test`      | Execute tests with coverage analysis and automated quality reporting.                |
| `/sq:troubleshoot`| Diagnose and resolve issues in code, builds, deployments, and system behavior.     |

---

## Configuration

### MCP Servers

SuperQwen can integrate with Model Context Protocol (MCP) servers for advanced AI capabilities. During installation (`superqwen install mcp`), the installer will attempt to detect and configure any available MCP servers on your system.

The configuration is saved in `~/.qwen/settings.json`. You can manually edit this file to add or modify MCP server configurations.

---

## Contributing

Contributions are welcome! Whether it's reporting a bug, suggesting a feature, or submitting a pull request, your help is appreciated. Please see the `CONTRIBUTING.md` file for more details on how to get started.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

This framework was originally forked from the **SuperGemini Framework**. We sincerely thank the **SuperClaude Team** for their outstanding work, which served as the foundation and inspiration for this project.

-   [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)
-   [SuperGemini Framework](https://github.com/SuperClaude-Org/SuperGemini_Framework)
