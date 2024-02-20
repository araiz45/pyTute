# Try Except using error handling
a = input("Enter Number: ")
print(f"Multiplication table of {a} is ")
try:
    for i in range(1, 11):
        print(f"\t |{int(a)} X {int(i)} = {int(a) * i}|")
except Exception as e:
    print(e)


print("Mein aik Joker hon")

# Handling Specific Error
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print('Error has been handled')
# Handling Multiple Error
try:
    num = int(input("Enter an integer: "))
    a = [3, 2]
    print(a[num])
except ValueError:
    print('Error has been handled')
except IndexError:
    print("Error of Index")