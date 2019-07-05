from test.test_asyncio.utils import *

from OpenSSL import SSL
import ssl


def verify_cb(conn, cert, errnum, depth, ok):
    return ok


# client/server is set on the connection, not the context in PyOpenSSL
def simple_server_sslcontext():
    server_context = SSL.Context(SSL.TLSv1_2_METHOD)
    # server_context.load_cert_chain(ONLYCERT, ONLYKEY)
    server_context.check_hostname = False
    # server_context.verify_mode = ssl.CERT_NONE
    return server_context


def simple_client_sslcontext(*, disable_verify=True):
    client_context = SSL.Context(SSL.TLSv1_2_METHOD)
    client_context.check_hostname = False
    if disable_verify:
        client_context.set_verify(SSL.VERIFY_NONE, verify_cb)
        pass
    return client_context


def dummy_ssl_context():
    return SSL.Context(SSL.TLSv1_2_METHOD)


def simple_server_sslcontext_stdlib():
    server_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    server_context.load_cert_chain(ONLYCERT, ONLYKEY)
    server_context.check_hostname = False
    server_context.verify_mode = ssl.CERT_NONE
    return server_context


def simple_client_sslcontext_stdlib(*, disable_verify=True):
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.check_hostname = False
    if disable_verify:
        client_context.verify_mode = ssl.CERT_NONE
    return client_context


def dummy_ssl_context_stdlib():
    if ssl is None:
        return None
    else:
        return ssl.SSLContext(ssl.PROTOCOL_TLS)
