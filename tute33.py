# Finally Clause
def multiPle():
    try:
        l = [3, 23, 5, 23, 5]
        i = int(input("Enter the value of index: "))
        print(l[i])
        return 1
    except Exception as e:
        print("Some error occured")
        return 0
    finally:
        print("I always executed")

x = multiPle()
print(x)