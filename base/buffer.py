import socket
class Buffer():
    _buffer = []
    def readBuffer(self):
        data = ''
        extra = [""]
        line = [""]
        try:
            data = extra[0] + self.recv(1024)
            data = data.replace('\r', "")
            extra.pop(0)
            for x in range(len(data.split('\n'))):
                extra.append(data.split('\n')[x])
            data = data.split('\n')[0]
            line = data.split(':')
            line = [':'.join(line[:2]), ':'.join(line[2:])]
        except socket.error:
            self.close
        return line
    def findBuffer(self, line):
        x = 0
        for x in range(len(self._buffer)):
            if self._buffer[x].find(line) == 0:
                return True
                break
        return False
        
    def getBuffer(self):
        self._buffer = self.readBuffer()
