def bubblesort(mynumlist):
    num_length = len(mynumlist) - 1
    numsort = False

    while not numsort:
        numsort = True
        for a in range(0, num_length):
            if mynumlist[a] > mynumlist[a + 1]:
                numsort = False
                mynumlist[a], mynumlist[a + 1] = mynumlist[a + 1], mynumlist[a]
    return mynumlist


list_sorted = bubblesort([2, 4, 6, 5, 3, 2, 7, 6, 9, 22, 6])

print(list_sorted)
