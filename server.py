"""
Tiny local server to download music into the iOS Simulator's Files app.

Usage:
    python3 server.py

Then open http://localhost:8000 in the Simulator's Safari.
"""

import html
import os
import sys
import urllib.parse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

FOLDER = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
PORT = 8000
EXTENSIONS = (".mp3", ".m4a", ".aac", ".wav", ".flac")


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FOLDER, **kwargs)

    def do_GET(self):
        path = urllib.parse.unquote(self.path.split("?")[0])
        if path == "/":
            self.send_index()
        else:
            super().do_GET()

    def end_headers(self):
        # Force Safari to download the file instead of playing it in the page.
        path = urllib.parse.unquote(self.path.split("?")[0])
        if path.lower().endswith(EXTENSIONS):
            name = urllib.parse.quote(os.path.basename(path))
            self.send_header(
                "Content-Disposition", f"attachment; filename*=UTF-8''{name}"
            )
        super().end_headers()

    def send_index(self):
        files = sorted(
            f for f in os.listdir(FOLDER) if f.lower().endswith(EXTENSIONS)
        )
        rows = "\n".join(
            f'<li><a href="/{urllib.parse.quote(f)}">{html.escape(f)}</a></li>'
            for f in files
        )
        if not rows:
            rows = "<li>No music files found in this folder.</li>"

        page = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Music</title>
<style>
  body {{ font-family: -apple-system, sans-serif; padding: 16px; }}
  li {{ margin: 14px 0; font-size: 18px; word-break: break-word; }}
</style>
</head>
<body>
<h2>Music ({len(files)})</h2>
<p>Tap a song, then tap Download...</p>
<ul>
{rows}
</ul>
</body>
</html>"""
        data = page.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        super().end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    if not os.path.isdir(FOLDER):
        sys.exit(f"Folder not found: {FOLDER}")
    print(f"Serving {FOLDER}")
    print(f"Open http://localhost:{PORT} in the Simulator's Safari")
    print("Press Ctrl+C to stop")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()