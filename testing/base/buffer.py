import socket
class Buffer():
    buffer = []
    extra = ['']
    def readBuffer(self):
        try:
            line = ''
            data = self.extra[0] + self.recv(1024)
#            data = data.replace('\r', "")
            self.extra.pop(0)
            for x in range(len(data.split('\n'))):
                self.extra.append(data.split('\n')[x] + '\n')
            line = data.split('\n')[0] + '\n'
        except socket.error:
            self.close
        return line

    def findBuffer(self, line):
        if self.buffer.find(line) == 0:
                return True
        return False
        
    def getBuffer(self):
        self.buffer = self.readBuffer()
