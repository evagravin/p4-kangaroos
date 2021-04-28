def bubblesort(mynumlist):
    indexing_length = len(mynumlist) -1
    sorted = False

    while not sorted:
        sorted = True
        for a in range(0, indexing_length):
            if mynumlist[a] > mynumlist[a+1]:
                sorted = False
                mynumlist[a], mynumlist[a+1] = mynumlist[a+1], mynumlist[a]
    return mynumlist

    list_sorted = bubblesort([2, 4, 6, 5, 3, 2, 7, 6, 9, 22, 6])

    print(list_sorted)




