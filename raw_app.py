import http.server
import socketserver

PORT = 8000


class ApiHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()

    def do_DELETE(self):
        self.send_response(200)
        self.end_headers()


with socketserver.TCPServer(("", PORT), ApiHTTPRequestHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
