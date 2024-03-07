"""Handler Package."""

from http.server import BaseHTTPRequestHandler
import json
from conf.constraints import JSON_PATH
from utils import open_json_file, validate_json
from controller import PropertyController


class PropertyHandler(BaseHTTPRequestHandler):
    """Property Handler Class.

    Arguments:
        BaseHTTPRequestHandler --  HTTP class server.
    """

    _controller = PropertyController()

    def do_POST(self) -> None:
        """Make a POST Request."""
        # Load and decode request body.
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        body = json.loads(post_data.decode("utf-8"))

        # Validate the body according to the schema.
        body_schema = open_json_file(f"{JSON_PATH}/filters_validator_schema.json")
        data = validate_json(body, body_schema)
        response = self._controller.find_properties(data)

        # Send response body.
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))
