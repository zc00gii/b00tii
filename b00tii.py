import base.server
import base.buffer
import base.module
import proto.irc
from proto.irc import IRCFunctions

a = IRCFunctions()
a.connect(("irc.ninthbit.net",6667))
a.identify()
a.getBuffer
while a.findBuffer("001") == False:
    a.pingPong()
    a.getBuffer()
    a.identify()
    a.send("USER b00tii * * : b00tii")
    a.send("NICK b00tii")

a.join("#offtopic")
while True:
    a.pingPong()
    a.getBuffer()
    print a._buffer
