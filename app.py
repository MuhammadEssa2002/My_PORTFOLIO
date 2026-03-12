import http.server
import socketserver
import webbrowser

PORT = 8000

webbrowser.open("http://localhost:8000")

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
