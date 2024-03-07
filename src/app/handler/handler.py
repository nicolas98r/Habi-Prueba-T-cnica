"""Handler Package."""

from http.server import BaseHTTPRequestHandler
import json
from controller import PropertyController


class PropertyHandler(BaseHTTPRequestHandler):
    """Property Handler Class.

    Arguments:
        BaseHTTPRequestHandler --  HTTP class server.
    """

    _controller = PropertyController()

    def do_POST(self) -> None:
        """Make a POST Request"""
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode("utf-8"))
        # Convertir JSON
        filters = self.convert_to_list_filter(data)
        print(filters)
        response = self._controller.find_properties(filters)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        print(response)
        self.wfile.write(response.encode("utf-8"))
