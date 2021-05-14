class bubble:
    def __init__(self):
        #inputted list from user
        self._lst = []

        #list of integers to be sorted
        self._lstnum = []

        #list of strings to be sorted
        self._lststr = []

    def addValues(self, values):
        for value in values.split(","):
            #if value is an integer append to self._lstnum
            if value.isdigit():
                self._lstnum.append(int(value))
            else:
                #otherwise append to self._lststr
                self._lststr.append(value)
            self._lst.append(str(value))

    def sort(self):
        #calls function bubbleSort to sort each list
        bubble.bubbleSort(self._lstnum)
        bubble.bubbleSort(self._lststr)

        #empty list
        results = []
        #append sorted results from both lists to one list
        for n in self._lstnum:
            results.append(str(n))
        for s in self._lststr:
            results.append(s)
        return results

    def getList(self):
        #get list that user inputted
        s = ', '
        return s.join(str(value) for value in self._lst)


    def bubbleSort(arr):
        #actual sorting algorithm
        l = len(arr)
        for i in range(l):
            for j in range(0, l-i-1):
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]

