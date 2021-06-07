a = float(input('Enter the No.1: '))
b = float(input('Enter the No.2: '))
try:
    c = a/b
    print (c)
except ZeroDivisionError:
    print ('infinite')
except ValueError:
    print ('Give a valid value')
