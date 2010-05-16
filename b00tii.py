import base.server
import base.buffer
import base.module
import proto.irc
from proto.irc import IRCFunctions

channels = ["#offtopic"]
a = IRCFunctions()
a.connect(("irc.ninthbit.net",6667))
a.user['nick'] = "b00[cb]"
a.identify()


# while a.findBuffer("001") == False:
a.getBuffer()
a.pingPong()
print a._buffer
    


while True:
    print a._buffer
    if "042" in a._buffer[0]:
        for channel in channels:
            a.join(channel)

    a.pingPong()
    a.getBuffer()

