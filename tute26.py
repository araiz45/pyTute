# Recursion 
# Calling Function into that function
def factorial (n) :
    if(n == 0 or n == 1):
        return 1
    else: 
        return n * factorial(n - 1)

print(factorial(4))


'''
f1 = 0
f2 = 1
f3 = 1
f4 = 2
f5 = 3
'''

def feboncii(n):
    if(n <= 1):
        return n
    return feboncii(n - 1) + feboncii(n - 2)

print(feboncii(33))