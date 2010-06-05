from base.server import Server

class IRCServer(Server):
    channels = []
    def __init__(self, server, port):
        self.connect((server, port))
