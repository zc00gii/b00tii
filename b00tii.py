import base.server
import base.buffer
import base.module
import proto.irc
from proto.irc import IRCFunctions

channels = ["#offtopic"]
a = IRCFunctions()
a.connect(("irc.ninthbit.net",6667))
a.identify()

while a.findBuffer("001") == False:
    a.getBuffer()
    a.pingPong()
    print a._buffer
for x in range(len(channels)):
    a.join(channels[x])

while True:
    a.pingPong()
    a.getBuffer()
    print a._buffer

