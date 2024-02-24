# decorators
def Greet(fx):
    def Mfx(*args, **karwargs):
        print("Good Mouring")
        fx(*args, **karwargs)
        print("Good night")
    return Mfx

@Greet
def Hello():
    print("Hello World")
@Greet
def Add(a, b):
    print(a + b)


Hello()
# Greet(Hello)()
Add(3, 5)