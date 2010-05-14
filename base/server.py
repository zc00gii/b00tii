import socket
from socket import SocketType

class Server(SocketType):
    def socketInit(self, family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, _sock=None):
        if _sock is None:
            _sock = socket._realsocket(family, type, proto)
        self._sock = _sock
        for method in socket._delegate_methods:
            setattr(self, method, getattr(_sock, method))

