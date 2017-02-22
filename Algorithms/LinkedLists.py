# Linked lists are great if you're going to read all the items one at a time, but if you are going to keep jumping around, linkedlists are terrible
# Lists are better if you want to insert elements into the middle
# Lists are better for deletion. Change what the previous elements points to.
# Arrays are better for readng as they are sequential but LinkedLists are better for inserting and deleting.
# LinkedLists can only do sequential access. Arrays are good for random access.


""" Selection Sort """


def findSmallest(arr):
    smallest = arr[0]  # stores the smallest value
    smallest_index = 0  # stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
        return smallest_index


def selectionSort(arr):  # sorts an array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)  # finds the smallest in the array and adds it to the new array
        newArr.append(arr.pop(smallest))
    return newArr


selectionSort([5,  2, 10])
