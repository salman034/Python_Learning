# Default Arguments

def greet(name, msg = 'Good morning'):
    print('Hey', name + ', ' + msg)

greet('Salman')
greet('Pasha')

#Key Arguments

def greeting(name, msg):
    print('Hey', name + ', ' + msg)

greeting(msg = 'whats up', name = 'Khan')


# Arbitrary Arguments

def func(*names):
    print(names)
func('Salman', 'kumar', 'Pasha')

