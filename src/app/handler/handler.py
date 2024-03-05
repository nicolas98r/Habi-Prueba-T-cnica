"""Handler Package."""

from http.server import BaseHTTPRequestHandler


class PropertyHandler(BaseHTTPRequestHandler):
    """Property Handler Class.

    Arguments:
        BaseHTTPRequestHandler --  HTTP class server.
    """

    def do_POST(self):
        """Make a POST Request"""
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Pong")
