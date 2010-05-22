import socket
class Buffer():
    buffer = []
    extra = ['']
    data = ''
    def readBuffer(self):
        try:
            data = extra[0] + self.recv(1024)
            data = data.replace('\r', "")
            extra.pop(0)
            for x in range(len(data.split('\n'))):
                extra.append(data.split('\n')[x])
            line = data.split('\n')[0]
        except socket.error:
            self.close
        return line

    def findBuffer(self, line):
        x = 0
        for x in range(len(self.buffer)):
            if self.buffer[x].find(line) == 0:
                return True
                break
        return False
        
    def getBuffer(self):
        self.buffer = self.readBuffer()
