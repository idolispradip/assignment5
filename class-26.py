class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

rect1 = Rectangle(10, 5)
print(f"Rectangle 1 - Length: {rect1.length}, Breadth: {rect1.breadth}")
print(f"Area of Rectangle 1: {rect1.area()}")
print(f"Perimeter of Rectangle 1: {rect1.perimeter()}")

rect2 = Rectangle(15, 7)
print(f"\nRectangle 2 - Length: {rect2.length}, Breadth: {rect2.breadth}")
print(f"Area of Rectangle 2: {rect2.area()}")
print(f"Perimeter of Rectangle 2: {rect2.perimeter()}")