#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import requests
import json


class S(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n",
                     str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET Request".encode('utf-8'))

    def do_POST(self):
        # <--- Gets the size of data
        content_length = int(self.headers['Content-Length'])
        # <--- Gets the data itself
        post_data = self.rfile.read(content_length)
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))
        url = "http://localhost:5005/webhooks/rest/webhook"

        post_data = post_data.decode('utf-8')

        post_data = post_data.replace('\"', '')
        post_data = post_data.replace('}', '')
        sender = post_data.split(',')[0].split(':')[1]
        message = post_data.split(',')[1].split(':')[1]

        obj = {
            "sender": sender,
            "message": message, }
        x = requests.post(url, data=json.dumps(obj))

        _res = x.json()
        _res = _res[0]
        self._set_response()

        self.wfile.write(json.dumps(_res).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('192.168.10.7', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting http...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping http...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
