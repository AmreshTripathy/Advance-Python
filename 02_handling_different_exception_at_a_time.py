try:
    a = int(input('Enter a Number: '))
    c = 1 / a
    print (c)

except ValueError as e:
    print ('Please Enter a valid value')
    # print (e)

except ZeroDivisionError as e:
    print ('Number must be greater than 0 not equal to 0')
    # print (e)

print ('Thanks for using this code')
