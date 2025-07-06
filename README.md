# 🚀 MCPs Integration Hub

A unified server hub to run **Monitoring Control Points (MCPs)** for popular services like **PagerDuty**, **Bugsnag**, **RedHat APIs**, and **LangSmith**.

This project helps enterprises integrate incident management, observability, and control-point automation into their internal workflows via independent plug-and-play modules.

---

## 📂 Folder Structure

```bash
/MCPs
│
├── pagerduty-mcp-server/       # Python-based MCP for PagerDuty
├── bugsnag-mcp/                # Node.js-based MCP for Bugsnag
├── redhat-api-mcp/             # Python-based MCP for RedHat APIs
├── langsmith-mcp-server/       # LangSmith MCP agent
├── main.py                     # Master launcher or config checker

```

---

## 🔧 Prerequisites

Make sure the following tools are installed:

* **Python ≥ 3.10**
* **Node.js ≥ 16.x** (required for Bugsnag MCP)
* **[uv](https://github.com/astral-sh/uv)** (Python dependency manager)
* **Git**
* Valid API tokens/keys for:

  * `PAGERDUTY_API_TOKEN`
  * `BUGSNAG_API_KEY`
  * `RH_API_OFFLINE_TOKEN`
  * `LANGSMITH_API_KEY`
  * `GROQ_API_KEY`

---

## 📦 Setup Instructions

### ✅ Common Setup

#### 1. Clone the repository

```bash
git clone https://github.com/your-org/mcp-server.git
cd MCPs
```

#### 2. Setup `uv` (Python package manager)

```bash
# For macOS
brew install uv

# For other platforms
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## ⚙️ Module-wise Setup

### 🔹 1. PagerDuty MCP

```bash
cd pagerduty-mcp-server

# Install dependencies
uv sync

# Activate virtual environment
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

# Run server
uv run python -m pagerduty_mcp_server
```

---

### 🔹 2. Bugsnag MCP

```bash
cd bugsnag-mcp

# Install dependencies
npm install

# Build MCP
npm run build

# Run the MCP
node build/index.js
```

---

### 🔹 3. RedHat API MCP

```bash
cd redhat-api-mcp

# Install dependencies
uv sync

# Activate virtual environment and run
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

# Start RedHat MCP
uv run python redhat_mcp_server.py
```

---

### 🔹 4. LangSmith MCP

```bash
cd langsmith-mcp-server

# Install dependencies
uv sync

# Run MCP
uv run python -m langsmith_mcp_server.server
```

---

## ▶️ Running from `main.py`

You can define and launch multiple MCPs from `main.py` using the sample configuration below:

### 📁 `sample_mcp_config.json`

```json
{
  "pagerduty": {
    "command": "uv",
    "args": ["run", "python", "-m", "pagerduty_mcp_server"],
    "cwd": "D:/Adya/MCPs_Server/pagerduty-mcp-server",
    "transport": "stdio",
    "env": {
      "PAGERDUTY_API_TOKEN": "your-token-here"
    }
  },
  "bugsnag": {
    "command": "node",
    "args": ["D:/Adya/MCPs/bugsnag-mcp/build/index.js"],
    "cwd": "D:/Adya/MCPs/bugsnag-mcp",
    "transport": "stdio",
    "env": {
      "BUGSNAG_API_KEY": "your-api-key"
    },
    "disabled": false,
    "alwaysAllow": []
  },
  "redhat": {
    "command": "uv",
    "args": ["run", "redhat_mcp_server.py"],
    "cwd": "D:/Adya/MCPs_Server/redhat-api-mcp",
    "transport": "stdio",
    "env": {
      "RH_API_OFFLINE_TOKEN": "your-token"
    }
  },
  "langsmith": {
    "command": "D:/Adya/MCPs/langsmith-mcp-server/.venv/Scripts/python.exe",
    "args": ["-m", "langsmith_mcp_server.server"],
    "cwd": "D:/Adya/MCPs/langsmith-mcp-server",
    "transport": "stdio",
    "env": {
      "LANGSMITH_API_KEY": "your-key"
    }
  }
}
```

---

## 📌 Notes
* **GROQ API:** Always use `.env` files or secrets managers for API keys. Avoid hardcoding them.
* **API Tokens:** Always use `.env` files or secrets managers for API keys. Avoid hardcoding them.
* **Windows/macOS Compatibility:** Windows uses `.venv\Scripts\activate`, macOS/Linux uses `source .venv/bin/activate`.
* **uv vs pip:** `uv` ensures fast and reproducible Python environments, preferred over `pip` for team setups.

---

## 🧪 Testing

Run the master test script to verify setup:

```bash
cd MCPs
.venv\Scripts\activate     # or `source .venv/bin/activate`
python -u main.py
```

---

## 🛠 Contributing

Contributions are welcome!

* Fork the repo
* Create a new branch
* Submit a Pull Request

---



