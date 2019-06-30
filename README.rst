bioopenssl
==========

If you use Python's builtin ssl module for very long, you'll soon start to
miss the OpenSSL features that aren't exposed in the standard library.

The idea of this module is to copy Python's default `asyncio.sslproto`,
replacing all calls to `ssl` with equivalent calls to pyOpenSSL's 
`OpenSSL.SSL` module. If this works, then it will be possible to do
proper SSL in asyncio, for example, a server with OSCP stapling.