
class bubble:
    def __init__(self):
        self._lst = []

    def bubble_sort(self):
        self._lst = [str(i) for i in self._lst]
        self._lst.sort()
        self._lst = [int(i) if i.isdigit() else i for i in self._lst]
        return self._lst

