import base.server
import base.buffer
from base.server import Server
from base.buffer import Buffer
class IRCFunctions(Server,Buffer): pass    

class PingPong(IRCFunctions):
    def PingPong(self):
        if self.ReadBuffer()[0] == 'PING':
            self.ReadBuffer()[0].split(':')
            self.send('PONG :' + self.ReadBuffer()[0].pop())
