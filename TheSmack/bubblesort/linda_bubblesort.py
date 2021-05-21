class linda:
    #user will have a list inputted
    def __init__(self):
        self._lst = []

    def addValues(self, values):
        #a for loop that appends the value to self._lst; credit to team member
        for value in values.split(","):
            self._lst.append(int(value))


    # The bubble sort algorithm that orders the list
    def sortingbubble(arr):
        n = len(arr)
        #goes through every array value
        for a in range(n):
            swapped = False
            # the array has a range from 0 to n-a-1. The first value exchanges with the next value when greater
            for b in range(0, n-a-1):
                if arr[b] > arr[b+1] :
                    arr[b], arr[b+1] = arr[b+1], arr[b]
                    swapped = True
            # IF no 2 values are swapped by the loop, then the algorithm breaks;
            if swapped == False:
                break


    def sort(self):
        #calls the function sortingbubble to sort the list
        linda.sortingbubble(self._lst)

        #makes the list empty
        results = []
        #appends the results to a list
        for n in self._lst:
            results.append(str(n))

        return results
