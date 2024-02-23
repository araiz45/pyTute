# Map, filter and Reduce 
# def cube(x):
#     return x * x * x

l = [3, 2, 4, 2, 4, 33]
# newl = []
# for item in l:
#     newl.append(cube(item))

newl = list(map(lambda x: x * x * x, l))
print(newl)

# Filter 
def filterFunction(a):
    return a < 4
newnewl = filter(filterFunction, l)
print(list(newnewl))

