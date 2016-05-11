from abc import ABC, abstractmethod

class PATTERNExport(ABC):
    def __init__(self, filename):
        super(PATTERNExport, self).__init__()
        self._filename = filename

    @staticmethod
    def decor(func):
        def wrapper(*args):
            print(str(args[0]))
            return func(*args)
        return wrapper

    @abstractmethod
    def export_data(self, data):
        return

    def __repr__(self):
        return "%r" % self.__class__.__name__

    def __str__(self):
        return "--- EXPORT TO %s FORMAT: %s! ---" % (repr(self), self._filename)
