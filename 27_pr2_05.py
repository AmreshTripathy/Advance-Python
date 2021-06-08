from functools import reduce

l = [43,234,534,76,231,435,768,324,276,9,834,23,64]
# s = reduce(lambda a,b: max(a, b), l)
# or
s = reduce(max, l)
print (s)