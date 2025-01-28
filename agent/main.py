from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from routers.status import get_status
from routers.processes import get_processes
from routers.restart import restart_system
from config.settings import HOST, PORT 

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/status":
            self.handle_status()
        elif self.path == "/processes":
            self.handle_processes()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def do_POST(self):
       
        if self.path == "/restart":
            self.handle_restart()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def handle_status(self):
        data = get_status() 
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def handle_processes(self):
        data = get_processes() 
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def handle_restart(self):
        try:
            restart_system() 
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"System is restarting...")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), RequestHandler)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()
