import base.server
import base.buffer
import base.module
import proto.irc
from proto.irc import IRCFunctions


channels = ["#offtopic"]
a = IRCFunctions()
a.connect(("irc.ninthbit.net",6667))
a.user['nick'] = "b00tii"
a.identify()
a.loop()
#a.getBuffer()
#a.pingPong()
print a._buffer
    


while True:
    print a._buffer
    if "001" or "042" in a._buffer[0]:
        for channel in channels:
            a.join(channel)
#    a.getBuffer()
#    a.pingPong()
    a.loop()
