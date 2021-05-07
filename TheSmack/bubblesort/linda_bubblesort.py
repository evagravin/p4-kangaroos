class linda:

    def __init__(self):
        self._lst = []

    def addValues(self, values):
        for value in values.split(","):
            self._lst.append(int(value))


    def sortingbubble(self):
        length = len(self) - 1
        unsorted = True
    
        while unsorted:
            for element in range(0,length):
                unsorted = False
                if self[element] > self[element + 1]:
                    hold = self[element + 1]
                    self[element + 1] = self[element]
                    self[element] = hold
                    print (self)
                else:
                    unsorted = True

    print (sortingbubble(self))
    
     
