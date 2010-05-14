import proto.irc
import base.server

class Buffer():
    def readBuffer():
        try: #make sure you put add the except, or remove this try. i have it msg a channel when it errors, or print the error.
            self.send('\r\n') #makes sure the connection is still alive, but doesnt actually send anything..
            self.data = self.extra+self.recv(1024) #make sure self.extra is pre-set to ''
            self.data = self.data.replace("\r",'').split("\n")
            self.extra = self.data.pop()
        except socket.error:
            sock = ''
            self.close()
            exit()
        for self.line in self.data:
            if self.line != '':
                self.line = self.line.split(" ")
        return line
 #self.line[0] would be the first word of the line being sent from the server.

