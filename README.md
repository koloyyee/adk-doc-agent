# Google ADK Swift Keyword Search

This project explores the capabilities of the Google ADK (Agent Development Kit) in Python to create an intelligent agent capable of searching for Swift programming language keywords. The agent is designed to provide comprehensive information, including definitions and practical usage examples, formatted as a vector of Clojure maps.

## Project Overview

The core idea is to leverage the Google ADK to build a multi-agent system that can:
1.  **Main Agent**: Orchestrates the workflow, accepting a Swift keyword as input with chat interface.
2.  **Search Agent**: Utilizes a Google Search tool to find relevant documentation, tutorials, and examples for the specified Swift keyword.
3.  **Writer Sub-Agent**: Processes the information retrieved by the Search Agent, extracts the keyword, its definition, and usage examples (code), and then writes this structured data into a Clojure (`.clj`) file. The output for each keyword will be a Clojure map containing `:keyword`, `:definition`, and `:usage` (example code).

## Features

*   **Intelligent Search**: Leverages Google ADK for efficient and relevant information retrieval.
*   **Swift Keyword Focus**: Specifically tailored to provide details on Swift programming language keywords.
*   **Clojure-Friendly Output**: Generates data in a vector of Clojure maps, making it easy to integrate with Clojure projects.
*   **Detailed Information**: Provides both definitions and practical usage examples for each keyword.

## Getting Started

### Prerequisites

*   Python 3.x
*   Google ADK (installation instructions to be added)

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/adk-doc-agent.git
    cd adk-doc-agent
    ```
2.  Install Python dependencies:
    ```bash
    uv sync --active
    ```

### Usage

```sh
adk web # for web ui, then select "doc_agent"
# or
adk run doc_agent # for cli
```


## Project Structure

*   Find agents in `agent.py` files: Contains the core logic for the Google ADK agent.
*   `swift_keywords.clj`: A file contains the agents result and return as Clojure maps.
*   `README.md`: This file.
