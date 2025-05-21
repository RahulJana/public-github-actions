class Triangle:
    def __init__(self, base, height):
        if base < 1 or height < 1:
            raise ValueError("The base and height must be greater than 0")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self, side1, side2):
        return self.base + side1 + side2
    
    def is_equilateral(self, side1, side2):
        return self.base == side1 == side2
    
    def is_isosceles(self, side1, side2):
        return self.base == side1 or self.base == side2