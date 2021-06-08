l = [1,2,44,34,54,56,5,45,25,23,98,505,90]
# five = lambda a: a%5==0
# s = list(filter(five, l))
# or
s = list(filter(lambda a: a%5==0, l))
print (s)
