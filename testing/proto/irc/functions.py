import socket
import base.server
import base.buffer
from proto.irc.server import IRCServer
from base.buffer import Buffer


class IRCFunctions(Buffer):
    user = {"name" : "b00ti", "ident" : "b00tii",\
            "pass": "secret", "nick" : "b00tii"} 
                                       # contains nick, (real)name, 
                                       # ident, and pass(NickServ)
    server = {}
    def send(self, whatToSend, server):
        print "SENDING: " + whatToSend
        server.send(whatToSend + "\r\n")
	
    def message(self, recvr, message):
        self.send("PRIVMSG " + recvr + " :" + message)

    def identify(self, ident = "b00tii",  name = "b00tii",):  
        self.send("USER " + self.user["ident"] + " * * : " + self.user["name"])
        self.send("NICK " + self.user["nick"])

    def nick(self, nick = user["nick"]):
        if nick != self.user["nick"]:
            self.user["nick"] = nick
        self.send("NICK " + self.user["nick"])

    def pingPong(self):
        if self.findBuffer('PING'):
            self.send("PONG " + self.buffer.split('PING ')[1])
        #for thing in self.buffer:
        #    print ">>>> " + thing
        
    def ctcp(self, recvr, message, upper = True):
        if upper == True:
            self.message(recvr, "\001" + message.upper() + "\001")
        elif upper == False:
            self.message(recvr, "\001" + message + "\001")
    def action(self, recvr, message):
        self.ctcp(recvr, "ACTION " + message, False)
    def join(self, channel):
        self.send("JOIN " + channel)
    def part(self, channel, reason = ""):
        self.send("PART " + channel + " :" + reason)
    def kick(self, channel, usr, reason=""):
        self.send("KICK ", channel + " " + usr + " :" + reason)
    def mode(self, channel, mode, args):
        self.send("MODE ", channel + " " + mode + " " + args)
    def topic(self, channel, tpc):
        self.send("TOPIC " + channel + " :" + tpc)
    def loop(self):
        try:
            self.getBuffer()
            self.pingPong()
        except (KeyboardInterrupt, socket.error):
            self.close()
