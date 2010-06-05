import base.server
import base.module
import base.buffer
import base.events
import proto.irc.functions
import proto.irc.events
#import proto.irc.server
from proto.irc.functions import IRCFunctions
channels = ["#botters"]
a = IRCFunctions()
a.connect(("irc.freenode.net",6667))
a.user['nick'] = "b00tii"
a.loop()

#a.getBuffer()
#a.pingPong()
print a.buffer
a.identify()

while True:
    print a.buffer
    if a.findBuffer('001'):
        for channel in channels:
            a.join(channel)
#    if a.buffer.startswith('~'):
#        a.message('#1ntrusion', a.buffer[1].replace('~',''))
    a.loop()

