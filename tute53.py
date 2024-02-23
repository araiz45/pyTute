# lamda Functions
# Traditionally:
# def double(x):
#     return x * 2
# Alternatively
# lamda functions
double = lambda x: x * 3
quadPos = lambda x, y: (x + y) / 2
print(double(4))
print(quadPos(3, 2))

def appl(fx, value):
    return 6 + fx(value, 4)

print(appl(quadPos, 5))