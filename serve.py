from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os

port = int(os.getenv("PORT", "8000"))
root = Path(__file__).parent / "app"
os.chdir(root)
server = ThreadingHTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
print(f"Serving on http://127.0.0.1:{port}")
server.serve_forever()
