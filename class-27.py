class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius * self.radius

    def circumference(self):
        return 2 * Circle.PI * self.radius
circle1 = Circle(5)
print(f"Circle 1 - Radius: {circle1.radius}")
print(f"Area of Circle 1: {circle1.area()}")
print(f"Circumference of Circle 1: {circle1.circumference()}")

circle2 = Circle(10)
print(f"\nCircle 2 - Radius: {circle2.radius}")
print(f"Area of Circle 2: {circle2.area()}")
print(f"Circumference of Circle 2: {circle2.circumference()}")

