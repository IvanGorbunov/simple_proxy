import logging
import socketserver

from sys import argv

from proxy.request import ProxyHandler

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(module)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(process)d] %(message)s',
                    )
LOG = logging.getLogger(__name__)


def run_proxy_server(host: str = '127.0.0.1', port: int = 8030) -> None:
    LOG.info(f'Server is running at: {host}:{port}')
    with socketserver.TCPServer((host, port), ProxyHandler) as httpd:
        httpd.serve_forever()


if __name__ == '__main__':
    if len(argv) > 1:
        host = argv[1]
        port = argv[2]
        run_proxy_server(host=host, port=port)
    else:
        run_proxy_server()
