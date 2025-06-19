import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from pathlib import Path

from .forecast import load_data, simple_forecast
from .simulation import simulate_what_if

DATA_PATH = Path(__file__).resolve().parent.parent / 'data' / 'synthetic_sales.csv'

class Handler(SimpleHTTPRequestHandler):
    def _set_headers(self, status=200, content_type='application/json'):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/forecast':
            params = parse_qs(parsed.query)
            periods = int(params.get('periods', ['3'])[0])
            data = load_data(DATA_PATH)
            forecast = simple_forecast(data, periods=periods)
            self._set_headers()
            self.wfile.write(json.dumps(forecast).encode())
        elif parsed.path == '/simulate':
            params = parse_qs(parsed.query)
            shock = float(params.get('shock', ['0.1'])[0])
            data = load_data(DATA_PATH)
            forecast = simple_forecast(data)
            sim = simulate_what_if(forecast, shock=shock)
            self._set_headers()
            self.wfile.write(json.dumps(sim).encode())
        else:
            if self.path == '/':
                self.path = '/index.html'
            return super().do_GET()


def run(server_class=HTTPServer, handler_class=Handler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
