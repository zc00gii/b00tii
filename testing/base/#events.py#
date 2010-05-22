def doNothing(): pass

class EventHandler:
    events= {}

    def hookEvent(self, name, onWhat, doFunction = doNothing):
        self.events[name] = Event(onWhat, doFunction)
    def unhookEvent(self, name):
        del self.events[name]
    def rehookEvent(self, name, onWhat, doFunction = doNothing):
        del self.events[name]
        self.events[name] = Event(onWhat, doFunction)
    def handleEvents(self):
        for name in self.events.keys():
            if self.events[name].when():
                self.events[name].function()

class Event:
    def when(): pass
    def function(): pass
    def  __init__(self, onWhat, doFunction=doNothing):
        self.when = onWhat
        self.function = doFunction
