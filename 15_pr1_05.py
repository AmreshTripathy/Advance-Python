num = int(input('Enter a Number: '))

table = [i*num for i in range(1, 11)]
print (table)
with open('table.txt','a') as f:
    f.write(f'Table of No.{num} = {table}\n')

    