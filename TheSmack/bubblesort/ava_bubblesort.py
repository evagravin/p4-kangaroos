
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
        self._lst = [str(i) for i in self._lst]
        self._lst.sort()
        lst = [int(i) if i.isdigit() else i for i in self._lst]
        return lst