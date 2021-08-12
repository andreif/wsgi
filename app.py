import json
import os
from wsgiref import simple_server


def filter_env(env):
    return {
        key: value
        for key, value in sorted(env.items())
        if key in ["REMOTE_ADDR"] or key.startswith(("HTTP_", "REQUEST_", "SERVER_PROTOCOL"))
        if key not in os.environ
    }


def app(environ, start_response):
    start_response("200 OK", [("Content-type", "application/json; charset=utf-8")])
    return [json.dumps(filter_env(environ), indent=2).encode()]


simple_server.ServerHandler.server_software = ""
port = os.environ.get("PORT", 8000)
with simple_server.make_server(host="", port=port, app=app) as httpd:
    print(f"Serving on port {port}...")
    httpd.serve_forever()
