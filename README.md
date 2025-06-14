# MCP Local File Resource Server

This project provides a **Model Context Protocol (MCP)** server that exposes files from a local directory as both resources and tools. It enables LLMs or MCP clients to search, read, and batch-process files—including text, code, and PDF documents—using standardized MCP URIs and methods.

## Features

- **Read Local Files as Resources:**  
  Fetch the content of any file in your target directory by its name using a simple URI.
- **PDF Extraction:**  
  Reads and extracts text from PDF files using [PyMuPDF (`fitz`)](https://pymupdf.readthedocs.io/).
- **File Search:**  
  Search for files by partial name or extension using a dedicated resource or tool.
- **Batch File Reading:**  
  Read multiple files at once and return their contents as a dictionary.
- **MCP-Compliant:**  
  Works seamlessly with the [MCP Inspector](https://github.com/modelcontextprotocol/inspector) and other MCP clients.

## How It Works

- **Resources:**  
  - `document://{filename}` — Read the content of a file (supports `.txt`, `.md`, `.csv`, `.pdf`, etc.).
  - `search://{dummyfilename}` — List all files matching a search pattern.
- **Tools:**  
  - `get_and_read_all_files` — Read multiple files at once.
  - `find_correct_file_tool` — Search for files by name (tool variant).

## Getting Started

### Prerequisites

- Python 3.8+
- [MCP Python SDK](https://pypi.org/project/mcp/) (`pip install mcp`)
- [PyMuPDF](https://pypi.org/project/PyMuPDF/) for PDF support (`pip install pymupdf`)

### Installation

