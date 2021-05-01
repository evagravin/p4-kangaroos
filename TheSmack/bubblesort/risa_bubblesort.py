def bubblesort(mynumlist):  # defines the function bubblesort and passes the parameter, mynumlist, which is also the list
    num_length = len(mynumlist) - 1
    sorted = False

    while not sorted:
        sorted = True
        for a in range(0, num_length):
            if mynumlist[a] > mynumlist[a + 1]:
                sorted = False
                mynumlist[a], mynumlist[a + 1] = mynumlist[a + 1], mynumlist[a]
    return mynumlist


list_sorted = bubblesort([2, 4, 6, 5, 3, 2, 7, 6, 9, 22, 6])

print(list_sorted)
