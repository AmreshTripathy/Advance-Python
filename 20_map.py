def square(num):
    return num * num

l = [1, 2, 4]
# method 1
l2 = []
for i in l:
    l2.append(square(i))
print (l2)

# method 2
print (list(map(square, l)))