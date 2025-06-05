from functools import reduce


def sum(a, b):
    return a+b


print(sum(5, 6))

# Concatenation of list
list1 = [5, 6]
list2 = [7, 8]
list3 = list1+list2


print(list3)

# MAP function :iT IS USED TO APPLY FUNCTION TO EACH ITERABLES i.e it maps function to each iterables mentioned in the list
d = list(map(sum, list1, list2))


print(d)

# FILTER FUNCTION :it is used for filtering iterables on the basis of given function
# SYNTAX FOR FILTER FUNCTION :

# FILTER(FUCNTION,ITERABLES)

list1 = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, list1))
print(result)

# REDUCE FUNCTION : it is used to apply a fucntion in all iterables and return a single value
# SYNTAX FOR REDUCE function
LIST1 = [1, 2, 3, 4]
result = reduce(lambda a, b: a+b, LIST1)
print(result)
