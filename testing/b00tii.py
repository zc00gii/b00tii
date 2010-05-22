import base.server
import base.module
import base.buffer
import base.events
import proto.irc.functions
import proto.irc.events
#import proto.irc.server
from proto.irc.functions import IRCFunctions
channels = ["#1ntrusion"]
a = IRCFunctions()
a.connect(("irc.prison.net",6667))
a.user['nick'] = "b00tii"
a.identify()
a.loop()

#a.getBuffer()
#a.pingPong()
print a.buffer
    


while True:
    print a.buffer
    if "72" in a.buffer[0]:
        for channel in channels:
            a.join(channel)
    if a.buffer[1].startswith('~'):
        a.message('#1ntrusion', a.buffer[1].replace('~',''))
    a.loop()

