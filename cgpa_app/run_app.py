import http.server
import socketserver
import webbrowser
import os
import threading
import time

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    # Change directory to the app folder to ensure relative paths work
    os.chdir(DIRECTORY)
    
    # Start the server in a separate thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Give the server a moment to start
    time.sleep(1)
    
    # Open the browser
    url = f"http://localhost:{PORT}"
    print(f"Opening {url} in your browser...")
    webbrowser.open(url)
    
    print("\n" + "="*50)
    print("      STUDENT CGPA PRO WEB APP IS RUNNING")
    print("="*50)
    print("Keep this terminal open while using the app.")
    print("Press Ctrl+C to stop the server.")
    print("="*50)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down server...")
