from base.events import Event, EventHandler
from base.buffer import Buffer

class IRCEvents(Event):
    handler = EventHandler()
    def __init__(self):
        self.handler.events = { "privmsg" : Event(privmsg), "part" : Event(part),
               "quit" : Event(quit), "join" : Event(join),
               "kick" : Event(kick), "mode" : Event(mode),
               "topic" : Event(topic) }

    def privmsg(self, message = False):
        if buffer[0].startswith(':PRIVMSG'):
            if message != False:
                if buffer[1].startswith(message):
                    return True
                return False
            return True
        return False

    def part(self):
        if buffer[0].startswith(':PART'):
            return True
        return False

    def join(self):
        if buffer[0].startswith(':JOIN'):
            return True
        return False

    def mode(self, mode = None):
        pass

    def topic(self):
        if buffer[0].startswith(':TOPIC'):
            return True
        return False
    def kick(self):
        if buffer[0].startswith(':KICK'):
            return True
        return False
    def raw(self, rawdata):
        if buffer[0].startswith(rawdata):
            return True
        return False

