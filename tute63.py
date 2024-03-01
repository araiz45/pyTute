# Strict methods

class Math:
    def __init__(self, num):
        self.num = num

    def addTwoNum(self, n):
        return self.num + n
    
    @staticmethod
    def add(n1, n2):
        return n1 + n2
    

a = Math(4)
print(a.addTwoNum(3))
print(Math.add(4, 2))
# print(Math.addTwoNum(4, 2))
print(a.add(4, 3))