
class bubble:
    def __init__(self):
        self._lst = []
        self._lstnum = []
        self._lststr = []

    def addValues(self, values):
        for value in values.split(","):
            if value.isdigit():
                self._lstnum.append(int(value))
            else:
                self._lststr.append(value)
            self._lst.append(str(value))

    def getList(self):
        s = ', '
        return s.join(str(value) for value in self._lst)


    def sort(self):
        bubbleSort(self._lstnum)
        bubbleSort(self._lststr)

        results = []
        for n in self._lstnum:
            results.append(str(n))
        for s in self._lststr:
            results.append(s)
        return results

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
