list2 = [2,4,6,8]

# write a recursive function to sum a list
def sum(list):
    if list  == []:
        return 0
    return list[0] + sum(list[1:])



print(sum(list2))


#Write a recursive function to count the number of items in a list.
def counter(list):
    if (list) == []:
        return 0
    return 1 + (counter(list[1:]))

print(counter(list2))

# write a recursive function to find the maximum in a list
def max(list):
    if len(list) == 2 :
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    #print('submax is ', sub_max)
    return list[0] if list[0] > sub_max else sub_max


print(max(list2))