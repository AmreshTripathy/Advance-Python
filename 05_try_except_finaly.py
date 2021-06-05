try:
    i = int(input('Enter a Number: '))
    a = 1/i
    print (a)
except Exception:
    print ('There is an exception!')
    exit()
finally:
    print ('We are Done!')
    
print ('Thanks for using this program')
