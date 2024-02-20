# Dictionaries Method
ep = {
    12:33,
    334:23,
    232:60,
}
ep2 = {
    222: 32,
    566: 22,
}

# Update 
ep.update(ep2)
print(ep)
# pop - for remove
ep.pop(222)
print(ep)
# popitem - for remove last item
ep.popitem()
print(ep)
# Clear - Empty dictionary
ep.clear()
print(ep)
# empty dictionary
empt = {}
print(empt)
# del - delete dictionary
del ep
# print(ep)
del ep2[222]
print(ep2)