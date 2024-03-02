# Method Overriding
class Shape:
    def __init__(self, y, x):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area (self):
        return 3.142 * super().area()


a = Shape(33, 44)
b = Circle(3)
print(b.area())
    