# MCP Local File Resource Server

The **MCP Local File Resource Server** is a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that exposes files from a local directory as **resources** and **tools**.  
It allows LLMs and MCP clients to **search, read, and batch-process files**—including text, code, and PDF documents—using standardized MCP URIs and methods.  

## ✨ Features

- 📂 **Read Local Files as Resources**  
  Fetch the content of any file in your target directory via a simple URI. Supports `.txt`, `.md`, `.csv`, `.pdf`, and more.  

- 📄 **PDF Extraction**  
  Extracts text from PDF files using [PyMuPDF (`fitz`)](https://pymupdf.readthedocs.io/).  

- 🔍 **File Search**  
  Search files by partial name or extension using either a **resource** or a **tool**.  

- 📑 **Batch File Reading**  
  Load multiple files at once and return their contents in a single dictionary.  

- ⚡ **MCP-Compliant**  
  Fully compatible with the [MCP Inspector](https://github.com/modelcontextprotocol/inspector) and other MCP clients.  

## ⚙️ How It Works

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
# CHALLENGES *****
# ✨ What Makes This Server Special: The Engineering Behind It ✨

Building this server wasn't just about writing code; it was about solving key challenges to create a tool that is powerful, smart, and safe. Here’s a look at the engineering that went into it.

---

#### 🔌 **1. Speaking the AI's Language (MCP Integration)**

> **The Problem:** How do you get a server to communicate flawlessly with a new, advanced AI communication standard?
>
> **Our Solution:** We dove deep into the Model Context Protocol (MCP) rulebook to build a fully compliant server. After rigorous testing, we created a tool that speaks the AI's language perfectly, making it a reliable partner for any MCP-ready application.

---

#### 🚀 **2. Fast, Focused Data for the AI (Efficiency)**

> **The Problem:** AI models get bogged down by too much information. How do you give it *just* the right data, and do it quickly?
>
> **Our Solution:** We designed a smart, two-step system. It first **identifies** the exact files needed and then **extracts** content *only* from them. This keeps the AI focused, fast, and efficient, avoiding information overload.

---

#### 🛡️ **3. Fort-Knox Security for Your Files (Sandboxing)**

> **The Problem:** The server needs to read local files, but it absolutely *must not* be allowed to wander outside its designated folder.
>
> **Our Solution:** We built a digital "sandbox"—a secure, fenced-in area for all file operations. The server is strictly locked down to its folder, with safeguards to block any escape attempts. Your files are safe, and the server only accesses what you allow.



