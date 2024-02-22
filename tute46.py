# Global / Local Variable
x = 4

def helloFunc():
    global x
    global y
    y = 33
    x = 5
    print('The local variable is' , x)

print('The Global variable is', x)
helloFunc()
# x = 10
print('The Global variable after re-assigning is', x)
print('The Global variable after re-assigning is', y)