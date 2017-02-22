def binary_search(list,item):
    low = 0
    high = len(list) -1

    while low <= high:
        mid = (low + high)
        print("mid",mid)
        guess = list[mid]
        print("guess", guess)
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_lists = [i for i in range(0,100)]

#my_lists = [1,3,5,7,9]
#print(len(my_lists))
print(binary_search(my_lists, 56))

# O(log n) also known as logtime. Example: BInary Search
# O(n) also known as linear time. Example: Simple search
# O(n* log n) Example: A fast sorting algorith, like quicksort
# O(n2) Example: A slow sorting algorithm like selection sort
# O(n!) Example: A really slow algorithm like the travellign sales person