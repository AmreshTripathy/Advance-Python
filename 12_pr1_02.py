list1 = [2, 4, 7, 6, 9, 10, 12,32, 23,32,9]
for index,item in enumerate(list1):
    if (index == 2 or index == 4 or index == 6):
        print (f'Element: {index+1}, item: {item}')