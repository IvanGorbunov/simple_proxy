import logging
import time

from http.client import HTTPSConnection
from http.server import SimpleHTTPRequestHandler

from proxy.parser import process_html

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(module)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(process)d] %(message)s',
                    )
LOG = logging.getLogger(__name__)


class ProxyHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        target_host = 'news.ycombinator.com'
        LOG.info('Connection opened...')

        client = HTTPSConnection(target_host)
        client.request('GET', self.path)
        response = client.getresponse()

        html = response.read().decode('utf-8')
        new_page = process_html(html)

        time.sleep(1)

        self.send_response(response.status)
        for header in response.getheaders():
            self.send_header(*header)
        self.end_headers()
        self.wfile.write(new_page)

        client.close()
        LOG.info('Connection closed...')
