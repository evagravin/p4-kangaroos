class linda:

    def __init__(self):
        self._lst = []

    def addValues(self, values):
        for value in values.split(","):
            self._lst.append(int(value))


    # An optimized version of Bubble Sort
    def sortingbubble(arr):
        n = len(arr)
        # Traverse through all array elements
        for i in range(n):
            swapped = False
            # Last i elements are already
            #  in place
            for j in range(0, n-i-1):
                # traverse the array from 0 to
                # n-i-1. Swap if the element
                # found is greater than the
                # next element
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            # IF no two elements were swapped
            # by inner loop, then break
            if swapped == False:
                break

    def sort(self):
        linda.sortingbubble(self._lst)

        results = []
        for n in self._lst:
            results.append(str(n))

        return results
