from functools import reduce

sum = lambda a,b: a+b
l = [2,6,43,7,3,98]
val = reduce(sum, l)
print (val)