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
        # 1. Get port safely
        final_port = os.getenv("PORT", 8000)
        print(f"--- DEBUG: Attempting to start on port {final_port} ---")

        # 2. COMMENT THIS OUT temporarily to test Render connectivity
        # print("Indexing document...")
        # index_document() 

        print(f"--- DEBUG: Reached mcp.run() ---")
        
        # 3. Use the most basic run command possible
        mcp.run(
            transport="sse", 
            host="0.0.0.0", 
            port=final_port
        )

    except Exception as e:
        print(f"--- CRITICAL ERROR DURING STARTUP ---")
        print(str(e))
      