# mcp-tool-provider (MCP Server)

This repository contains the **Model Context Protocol (MCP)** server that powers the semantic search and long-term memory for the Sentinel AI ecosystem. It transforms a local Word document into a searchable, vector-indexed knowledge base.

---

## 🛠️ Technical Core

The server implements a local **RAG (Retrieval-Augmented Generation)** pipeline. It handles document ingestion, sliding-window chunking, and similarity search without requiring external vector databases.

| Component | Technology |
| :--- | :--- |
| **Framework** | [FastMCP](https://github.com/jlowin/fastmcp) |
| **Embeddings** | `all-MiniLM-L6-v2` (SentenceTransformers) |
| **Vector Math** | NumPy (Cosine Similarity) |
| **Storage** | `knowledge_base.docx` (python-docx) |
| **Transport** | **SSE** (Server-Sent Events) |

---

## 🔧 Exposed MCP Tools

Once the server is running, it exposes the following tools to any MCP-compliant client (like Claude Desktop or custom orchestrators):

### 1. `search_knowledge_base`
* **Description**: Performs a semantic search across the indexed document.
* **Input**: `query` (string).
* **Threshold**: Returns results with a cosine similarity > **0.3**.

### 2. `append_to_knowledge_base`
* **Description**: Adds new facts or records to the permanent `.docx` file.
* **Logic**: Appends the text and **immediately re-indexes** the embeddings so the new information is instantly searchable.
* **Input**: `text` (string).

---

## 🚀 Deployment & Execution

### Local Development
1. **Install Dependencies**: `pip install -r requirements.txt`
2. **Run Server**: `python main.py`

### Cloud Deployment (Render/Railway)
This server is optimized for cloud environments. It binds to the `PORT` environment variable and uses **SSE** transport for remote accessibility.

**Render Start Command**:
```bash
uvicorn main:mcp.app --host 0.0.0.0 --port $PORT
