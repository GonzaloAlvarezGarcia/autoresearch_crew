# AutoResearch Crew: Autonomous Multi-Agent System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/Orchestration-CrewAI-red?style=for-the-badge)
![Chainlit](https://img.shields.io/badge/UI-Chainlit-black?style=for-the-badge)
![Groq](https://img.shields.io/badge/Inference-Groq_Llama3-purple?style=for-the-badge)

> **A production-ready Agentic AI application that orchestrates a team of autonomous agents to conduct deep web research and write professional reports in real-time.**

## Project Overview

This project solves the problem of time-consuming manual research. Instead of browsing dozens of tabs, **AutoResearch Crew** deploys a squad of AI agents to do the heavy lifting.

It uses **CrewAI** to orchestrate the workflow and **Groq** (Llama-3.3-70b) for high-speed inference. The system features a "Senior Researcher" agent that browses and scrapes the live web, and a "Technical Writer" agent that synthesizes findings into a coherent blog post, all presented via a ChatGPT-like interface built with **Chainlit**.

### Key Features

- **Multi-Agent Orchestration:** Autonomous collaboration between specialized agents (Researcher & Writer).
- **Real-Time Web Scraping:** Uses `SerperDev` for Google Search and `ScrapeWebsiteTool` to read full website contents.
- **Interactive UI:** A modern chat interface using **Chainlit** for a seamless user experience.
- **Configuration as Code:** Agent personas and tasks are defined in YAML files, decoupling logic from configuration.
- **High-Performance:** Powered by Groq's LPU (Language Processing Unit) for near-instant inference.

## Demo

> **[Click here to watch the agents in action ([Video Demo](https://youtu.be/lvkUCXXsNxw))]**

## Architecture

The system follows a sequential hierarchical process:

1.  **User Input:** The topic is received via the Chainlit UI.
2.  **Agent 1 (Senior Researcher):** \* Formulates search queries.
    - Uses **Serper API** to find relevant URLs.
    - Uses **ScrapeWebsiteTool** to extract content from specific pages.
3.  **Handoff:** Raw data is passed to the next agent.
4.  **Agent 2 (Technical Writer):** \* Analyzes the gathered data.
    - Structures the narrative.
    - Writes a formatted Markdown report.
5.  **Output:** The final report is displayed in the UI and saved locally.

## Tech Stack

- **Orchestration:** CrewAI
- **LLM:** Groq (Llama-3.3-70b-versatile)
- **Interface:** Chainlit
- **Tools:** SerperDev (Google Search), ScrapeWebsiteTool
- **Language:** Python 3.10+

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/GonzaloAlvarezGarcia/autoresearch_crew.git
cd autoresearch_crew
```

### 2. Install Dependencies

It is recommended to use a virtual environment.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Environment Setup

Create a .env file in the root directory and add your API keys:

```Code snippet
GROQ_API_KEY="gsk_..."
SERPER_API_KEY="..."
MODEL_NAME="groq/llama-3.3-70b-versatile"
```

### 4. Run the Application

Launch the Chainlit server:

```bash
chainlit run app.py -w
The application will open automatically at http://localhost:8000.
```

## Customization

You can modify the agents' behavior without touching the Python code by editing the YAML configuration files in src/config/:

- agents.yaml: Define the role, goal, and backstory of your agents.

- tasks.yaml: Define the specific deliverables and expected outputs.
