from test.test_asyncio.utils import *

from OpenSSL import SSL


def dummy_ssl_context():
    return SSL.Context(SSL.TLSv1_2_METHOD)
