while (True):
    print ('Press Q to quit')
    a = input('Enter a Number: ')
    if (a == 'q'):
        break
    try:
        print ('Trying...')
        a = int(a)
        if (a > 6):
            print ('You Enter a number greater than 6')
    except Exception as e:
        print (f'Your input resulted in an error! {e}')

print ('Thank You for playing this game')