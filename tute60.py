# Getter & Setter

class MyClass:
    def __init__(self, value):
        self._value = value

    def Show(self):
        print(f"Value is {self._value}")

    @property
    def TenValue(self):
        return 10 * self._value
    
    @TenValue.setter
    def TenValue(self, newValue):
        self._value = newValue / 10


obj = MyClass(33)
obj.TenValue = 44
print(obj.TenValue)
obj.Show()