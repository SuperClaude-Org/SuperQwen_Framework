# SuperQwen Framework

SuperQwen Framework is an AI-enhanced development framework for Qwen CLI, adapted and forked from the **SuperGemini Framework**. It provides structured development capabilities with slash commands, behavioral modes, and specialized AI agents.

Note : This is a test version. We welcome your contributions!

## Features

* **18 Slash Commands**: TOML-based commands for systematic workflow automation (`/analyze`, `/implement`, etc.)
* **Behavioral Modes**: Context-aware operation modes (Brainstorming, Introspection, Task Management, Token Efficiency)
* **Specialized AI Agents**: 13 domain experts (System Architect, Security Engineer, etc.)
* **MCP Server Integration**: Extended capabilities through MCP servers

## Installation

1. Clone this repository
2. Run the installation script:

   ```bash
   python install_qwen.py
   ```
3. Setup the framework:

   ```bash
   python setup_qwen.py
   ```

## Usage

After installation, you can use the following commands in Qwen CLI:

* `/analyze` - Comprehensive code analysis
* `/implement` - Implementation guidance
* `/design` - System design assistance
* `/test` - Test generation and validation
* And 14 more commands...

## Modes

Enable behavioral modes through flags:

* `--brainstorm` - Brainstorming mode for idea generation
* `--introspect` - Introspection mode for self-analysis
* `--task-manage` - Task management mode
* `--token-eff` - Token efficiency mode

## Uninstallation

To uninstall the framework:

```bash
python uninstall_qwen.py
```

---

### TODO

* Add additional slash commands as needed
* Extend pip and npm package support for new dependencies
* Improve documentation for `/sq:` command
* Enhance behavioral modes with more fine-grained controls
* Integrate additional specialized AI agents
* Ensure cross-platform compatibility for installation scripts

### Acknowledgment

This framework was originally forked from the **SuperGemini Framework**. I would like to sincerely thank the **SuperClaude Team** for their outstanding work, which served as the foundation and inspiration for this contribution.

* https://github.com/SuperClaude-Org/SuperClaude_Framework
* https://github.com/SuperClaude-Org/SuperGemini_Framework

---
