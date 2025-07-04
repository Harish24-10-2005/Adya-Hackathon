# MCP Setup Guide

This repository contains multiple MCP (Monitoring Control Point) implementations including **PagerDuty MCP** and **Bugsnag MCP**. Follow the instructions below to set up and run each module.

---

## 🔧 Prerequisites

- Python 3.10+
- Node.js (for Bugsnag MCP)
- [uv](https://github.com/astral-sh/uv) (Python package/dependency manager)
- Git
- A valid `PAGERDUTY_API_TOKEN` (for PagerDuty MCP)

---

## 📁 Folder Structure

```

/MCPs
│
├── pagerduty-mcp-server
│   └── Python-based MCP server for PagerDuty
│
├── bugsnag-mcp
│   └── Node.js-based MCP integration for Bugsnag
│
└── test.py
└── Sample script to validate environment

````

---

## 🚀 Setup Instructions

### 🔹 1. PagerDuty MCP

```bash
cd pagerduty-mcp-server

# Install uv if not already installed
brew install uv

# Sync and install Python dependencies
uv sync

# Set your PagerDuty API token
export PAGERDUTY_API_TOKEN=your_api_token_here  # On Linux/macOS
# For Windows (Command Prompt):
# set PAGERDUTY_API_TOKEN=your_api_token_here

# Activate the virtual environment
.venv\Scripts\activate

# Run the PagerDuty MCP server
uv run python -m pagerduty_mcp_server
````

---

### 🔹 2. Bugsnag MCP

```bash
cd bugsnag-mcp

# Install Node.js dependencies
npm install

# Build the project
npm run build
```

---

## ▶️ Running from Main Folder (`/MCPs`)

To activate the virtual environment and run test scripts from the root MCPs folder:

```bash
cd /MCPs

# Activate Python environment
.venv\Scripts\activate

# Run test script
python -u "d:\Adya\MCPs\test.py"
```

---

## 📌 Notes

* Ensure all environment variables (like `PAGERDUTY_API_TOKEN`) are securely stored and not committed to version control.
* This setup assumes you're on Windows (`.venv\Scripts\activate`). For macOS/Linux, use `source .venv/bin/activate`.
* Use `uv` for faster and reproducible Python dependency management.

