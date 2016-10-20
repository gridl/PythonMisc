# from collections import defaultdict
#
# sentence = "the red for jumped over the fence and ran to the zoo for food"
# words = sentence.split(' ')
# d = defaultdict(int)
# for word in words:
#     d[word] += 1
# print(d)


# grab the account number and keep track of the payment value for each account number
# from collections import defaultdict
# my_list = [(1234,100.23), (345,10.45), (1234,75.00), (345,222.66), (678,300.25),(1234,35.67)]
#
# d = defaultdict(list)
# for acct_num, value in my_list:
#     d[acct_num].append(value)
# print(d)

# using a lambda as default factory
from collections import defaultdict
animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'
print(animal['Nick'])
print(animal)