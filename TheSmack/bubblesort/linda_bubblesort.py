mylist = []

def sortingbubble(unList):
    length = len(unList) - 1
    unsorted = True

    while unsorted:
        for element in range(0,length):
            unsorted = False
            if unList[element] > unList[element + 1]:
                hold = unList[element + 1]
                unList[element + 1] = unList[element]
                unList[element] = hold
                print (unList)
            else:
                unsorted = True

print (sortingbubble(mylist))


#make 2 varibales in front end in jinja, set default values for the list 
