class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
    
    def volume(self):
        return self.width * self.height * self.depth
    
    def surface_area(self):
        return 2 * (self.width * self.height + self.height * self.depth + self.depth * self.width)

def main():
    try:
        # Create first box
        box1 = Box(2, 3, 4)
        print(f"Box 1 - Width: {box1.width}, Height: {box1.height}, Depth: {box1.depth}")
        print(f"Volume of Box 1: {box1.volume()}")
        print(f"Surface Area of Box 1: {box1.surface_area()}")
    except Exception as e:
        print(f"An error occurred while processing Box 1: {e}")

    try:
        # Create second box
        box2 = Box(5, 6, 7)
        print(f"Box 2 - Width: {box2.width}, Height: {box2.height}, Depth: {box2.depth}")
        print(f"Volume of Box 2: {box2.volume()}")
        print(f"Surface Area of Box 2: {box2.surface_area()}")
    except Exception as e:
        print(f"An error occurred while processing Box 2: {e}")

if __name__ == "__main__":
    main()

