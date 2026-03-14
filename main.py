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
   
        mcp.run(transport='sse')

    except Exception as e:
        print(f"--- CRITICAL ERROR DURING STARTUP ---")
        print(str(e))
      