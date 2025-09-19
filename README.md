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

### Resources
- `document://{filename}` → Read the content of a file (supports text, CSV, Markdown, PDFs, etc.)  
- `search://{pattern}` → List files matching a search pattern  

### Tools
- `get_and_read_all_files` → Read multiple files at once and return contents  
- `find_correct_file_tool` → Search for files by name (tool variant)  

Example:
```text
document://report.pdf   → Extracts text from `report.pdf`
search://.py            → Lists all Python files in the directory
