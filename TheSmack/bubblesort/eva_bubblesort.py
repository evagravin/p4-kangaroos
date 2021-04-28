def bubble_sort(unsorted_list):  # defines the function and passes in the parameter unsorted_list which is the list
    length = len(unsorted_list)  # sets a variable called length to equal the length of the list that gets passed in
    for e in range(length - 1):  # iterates through the length of the list - 1 since that is how many times is needed
        for f in range(length - 1 - e):  # the last element will already be sorted so iterates through length - 1 - e
            if unsorted_list[f] > unsorted_list[f + 1]:  # if the element that comes first is bigger than the next...
                right = unsorted_list[f]  # the variable "right" gets set to that number
                unsorted_list[f] = unsorted_list[f + 1]  # the bigger number takes the place of the right-most index
                unsorted_list[f + 1] = right  # it now assigns the number on the right to be the "right" variable
    return unsorted_list  # once the steps are completed for the whole list, it returns the new list which is in order

sorted_list = bubble_sort([1,4,87,54,0,98])

print(sorted_list)