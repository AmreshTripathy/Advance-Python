# We could use f'' string but it is lunched after version 3.5
# So before f'' string developers are used format specifier.
name = 'Amresh'
channel = 'TechieDuo'
# a = f'Good morning, {name}'
# a = 'Good morning, {}\nWelcome to {}, Chief'.format(name, channel)
# customize the position
a = 'Good morning, {1}\nWelcome to {0}, Chief'.format(name, channel)
print (a)