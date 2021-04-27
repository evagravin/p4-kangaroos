
class bubble:
    def __init__(self):
        self._lst = []

    def addValues(self, values):
        for value in values.split(","):
            self._lst.append(str(value))

    def getList(self):
        s = ','
        return s.join(str(value) for value in self._lst)

    def sort(self):
        sorted(self._lst)

