# Reddit Content Research Agent

A lightweight agent designed to research and analyze Reddit content using LLMs and SERP APIs.
This project integrates tools like **Bright Data SERP API**, **Google Gemini LLM**, and **LangChain** to automate content discovery and analysis.

## 📂 Project Structure

```
.
├── nbs/                         # Jupyter notebooks for experimentation and testing
│   ├── 01-init.ipynb            # Initial setup and environment checks
│   ├── 02-serp-api-init.ipynb   # Bright Data SERP API integration tests
│   ├── 03-google-gemini-llm-... # Gemini LLM + LangChain integration
│   ├── 04-structured-output-... # Structured output with LangChain + Pydantic
│   ├── 05-hard-way-llm-tool...  # Manual LLM tool calling approach
│   └── 06-llm-tool-calling...   # Simplified tool calling using LangGraph React agent
├── requirements.txt             # Python dependencies
├── rav.yaml                     # Configuration for agent or tools
├── .pre-commit-config.yaml      # Pre-commit hooks for linting/formatting
└── README.md                    # Project documentation
```

## 🚀 Features

* 🔎 **Search Automation:** Uses Bright Data SERP API for search queries.
* 🤖 **LLM Integration:** Google Gemini with LangChain for intelligent responses.
* 🧩 **Tool Calling:** Demonstrates manual and automated approaches to LLM tool usage.
* 🧱 **Structured Output:** Pydantic for clean, validated data formats.

## 🛠️ Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/Reddit-Content-Research-Agent.git
   cd Reddit-Content-Research-Agent
   ```
2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## ▶️ Usage

* Open any notebook in `nbs/` using Jupyter:

  ```bash
  jupyter notebook
  ```
* Run the notebooks step-by-step to validate API integrations and experiment with LLM tool calls.

## 📌 Notes

* Ensure your API keys for Bright Data and Google Gemini are set in your environment or configuration files.
* Use the pre-commit hooks to maintain consistent code formatting:

  ```bash
  pre-commit install
  ```