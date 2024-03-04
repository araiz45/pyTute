# Generators

def myGenerator():
    for i in range(10):
        yield i # Instead of Return


gen = myGenerator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for j in gen:
    print(j)
    # pass



