a = [3, 4, 8, 7, 90]
# b = []

# for index, item in enumerate(a):
#     if(item % 2 == 0):
#         # print (f'index: {index}, Even No.: {item}')
#         b.append(item)
# print (b)

# shortcut to write the same or called as List comprehension
b = [i for i in a if i%2==0]
print (b)
# also you can make set and dictionary comprehension
# Set Comprehension
s = {1, 4, 2, 3, 4, 2}
t = {i for i in s}
print (t) 