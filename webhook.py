import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
import sys
import subprocess


class HttpGetHandler(BaseHTTPRequestHandler):
    def _add_headers(self, code):
        self.send_response(code)
        self.send_header('Content-Length', '0')
        self.end_headers()

    def do_GET(self):
        if self.headers.get(args.header) == args.secret:
            exec_file(args.exec)
            self._add_headers(200)
        else:
            self._add_headers(403)

    def do_HEAD(self):
        self._add_headers(200)

    def do_POST(self):
        self._add_headers(403)


def exec_file(path):
    subprocess.Popen(path, shell=True)


def server_run(address, port, server_class=HTTPServer, handler_class=HttpGetHandler):
    server_address = (address, port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on {address}:{port}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-l', '--listen', default='localhost', help='IP address to listen')
    p.add_argument('-p', '--port', type=int, default=1212, help='Server port')
    p.add_argument('-x', '--exec', help='Path to file which should be executed with webhook')
    p.add_argument('-H', '--header', default='X-Gitlab-Token', help='Header with secret')
    p.add_argument('-s', '--secret',  help='Secret value')
    args = p.parse_args()
    if not args.exec or not args.secret:
        print('Insufficient arguments')
        sys.exit(1)
    server_run(args.listen, args.port)
