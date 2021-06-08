# Filter Syntax: list(filter(function, list))

# def greater_than_5(num):
#     if num > 5:
#         return True
#     else:
#         return False

# or in lambda 

greater_than_5 = lambda num: num>5    
l = [1,2,3,4,5,6,5,65,32,4,55,97,1,10]
print (list(filter(greater_than_5, l)))
