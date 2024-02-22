# Seek and tell 
with open('myfile2.txt', 'r')as f:
    print(type(f))
    # Move 10 bytes in the file
    f.seek(10)
    # Read the next 5 bytes
    print(f.tell())
    data = f.read(10)
    print(data)

with open('sample.txt', 'w') as f:
    f.write("Hello world this is araiz")
    f.truncate(5)
with open('sample.txt', 'r') as f:
    print(f.read())