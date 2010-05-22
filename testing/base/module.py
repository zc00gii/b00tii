class Module():
    modules = dict()

    def reloadModule(self,name):
        reload(self.modules[name])

    def loadModule(self,name):
        if name not in globals().keys():
            try:
                self.modules[name] = __import__(name)
            except ImportError:
                print 'Module does not exist'

    def unloadModule(self, name):
        self.modules.pop(name)
        globals().pop(name)
