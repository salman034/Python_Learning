# variable Scope Introduction

def my_func():
    x = 10
    print('Value inside function:', x)

x = 20

my_func()
print('Value outside function:', x)

# Local variable
def new_func():
    y = 5
#y = 5
new_func()
print(y)
