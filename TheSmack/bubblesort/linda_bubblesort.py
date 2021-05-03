
def bubble(list):
    length = len(list) - 1
    unsorted = True

    while unsorted:
        unsorted = False
        for v in range(0,length):
            if list[v] > list[v + 1]:
                hold = list[v + 1]
                list[v + 1] = list[v]
                list[v] = hold
                unsorted = True
            return list



if __name__ == "__main__":
    print list