class linda:

    def __init__(self):
        self._lst = []

    def addValues(self, values):
        for value in values.split(","):
            self._lst.append(int(value))


    def sortingbubble(self):
        length = len(self._lst) - 1
        unsorted = True
    
        while unsorted:
            for element in range(0,length):
                unsorted = False
                if self._lst[element] > self._lst[element + 1]:
                    hold = self._lst[element + 1]
                    self._lst[element + 1] = self._lst[element]
                    self._lst[element] = hold
                else:
                    unsorted = True


