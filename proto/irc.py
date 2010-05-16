import base.server
import base.buffer
from base.server import Server
from base.buffer import Buffer


class IRCFunctions(Server,Buffer):
    user = {"name" : "b00ti", "ident" : "b00tii",\
            "pass": "secret", "nick" : "b00tii"} 
                                       # contains nick, (real)name, 
                                       # ident, and pass(NickServ)
    server = dict() # contains addr(ess) and port
	
    def sendraw(self, whatToSend):
        print "SENDING: " + whatToSend
        self.send(whatToSend + "\r\n")
	
    def message(self, recvr, message):
        self.sendraw("PRIVMSG " + recvr + " :" + message)

    def identify(self, ident = "b00tii",  name = "b00tii",):  
        self.sendraw("USER " + self.user["ident"] + " * * : " + self.user["name"])
        self.sendraw("NICK " + self.user["nick"])

    def nick(self, nick = user["nick"]):
        if nick != self.user["nick"]:
            self.user["nick"] = nick
        self.sendraw("NICK " + self.user["nick"])

    def pingPong(self):
        if self._buffer[0].startswith("PING"):
            self.sendraw("PONG " + self._buffer[0][6:])
        #for thing in self._buffer:
        #    print ">>>> " + thing
        
    def ctcp(self, recvr, message, upper = True):
        if upper == True:
            self.message(recvr, "\001" + message.upper() + "\001")
        elif upper == False:
            self.message(recvr, "\001" + message + "\001")
    def action(self, recvr, message):
        self.ctcp(recvr, "ACTION " + message, False)
    def join(self, channel):
        self.sendraw("JOIN " + channel)
    def part(self, channel, reason = ""):
        self.sendraw("PART " + channel + " :" + reason)
    def kick(self, channel, usr, reason=""):
        self.sendraw("KICK ", channel + " " + usr + " :" + reason)
    def mode(self, channel, mode, args):
        self.sendraw("MODE ", channel + " " + mode + " " + args)
    def topic(self, channel, tpc):
        self.sendraw("TOPIC " + channel + " :" + tpc)
    def loop(self):
        try:
            self.getBuffer()
            self.pingPong()
        except KeyboardInterrupt:
            self.close()
