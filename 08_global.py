a = 54 # Global variable
def func1():
    global a
    print (a)
    a = 8 # Local variable
    print (a)

func1()
print (a)