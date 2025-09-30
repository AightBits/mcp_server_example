# Minimal MCP HTTP/SSE Server Example

A simple demonstration of the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) using [FastMCP](https://gofastmcp.com/) and a SQLite database.  
This project shows how to expose a local database through MCP so that clients (like Claude’s web interface) can call structured tools for data access.

## Dependencies
- Python 3.9+  
- `fastmcp` (installed via `requirements.txt`)  
- SQLite (bundled with Python)  
- Caddy (for reverse proxy and automatic TLS if exposing over HTTPS)

Install requirements with:

```bash
pip install -r requirements.txt
```

## Setup

Create a virtual environment and install dependencies:

```bash
./setup.sh
```

Initialize the database (only creates it if it does not exist):

```bash
python init_demo_db.py
```

## Usage

Start the MCP server:

```bash
source start.sh
```

The server runs locally on `http://127.0.0.1:8000/mcp`.  
If exposed via Caddy and a valid domain, it will be available over HTTPS.

### Integrating with Claude Web
1. Go to **Claude.ai → Settings → Integrations → Add custom integration**.  
2. Enter your public MCP endpoint, for example:  
   ```
   https://[address]/mcp
   ```  
3. Enable the connector in a chat and try prompts such as:
   - `Get customer 1`
   - `List orders for customer 1`
   - `call tool sql_select {"sql": "SELECT * FROM customers;"}`

## Files
- `setup.sh` – Creates the Python virtual environment and installs dependencies.  
- `start.sh` – Activates the environment and starts the MCP server.  
- `init_demo_db.py` – Initializes a simple SQLite database with test data.  
- `mcp_server_example.py` – MCP server exposing SQLite queries as tools.  
- `requirements.txt` – Python dependencies.

## Limitations
- Only demonstrates a toy SQLite database (customers and orders).  
- No authentication — intended for local/demo use.  
- Requires a working domain and TLS proxy (e.g., Caddy) for integration with Claude Web.

## License
Apache 2.0 License.
