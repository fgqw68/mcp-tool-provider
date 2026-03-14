import os
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv


print(f"--- DEBUG: start of execution ---")

# This loads the variables from your .env file into os.environ
load_dotenv()
# Global state
mcp = FastMCP("Sentinel-Knowledge-Base")

if __name__ == "__main__":
    try:
        print(f"--- inside main ---")

        # Use PORT from environment (Render sets this), default to 8000
        port = int(os.environ.get("PORT", 8000))
        host = "0.0.0.0"  # Bind to all interfaces for Render

        print(f"Starting server on {host}:{port}")
        mcp.run(transport='sse', host=host, port=port)

    except Exception as e:
        print(f"--- CRITICAL ERROR DURING STARTUP ---")
        print(str(e))
      