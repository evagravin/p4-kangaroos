def bubblesort(mylist):
    indexing_length = len(mylist) -1
    sorted = False

    while not sorted:
        sorted = True
        for a in range(0, indexing_length):
            if mylist[a] > mylist[a+1]:
                sorted = False
                mylist[a], mylist[a+1] = mylist[a+1], mylist[a]
    return mylist

    print (bubblesort([2,4,6,5,3,2,7,6,9,22,6]))