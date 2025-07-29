import math
#task5
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, value):
        if self.x==value.x and self.y==value.y:
            return True
        else:
            return False
    
    def __str__(self):
        return f"{self.x}, ({self.y})"
    
    def eucl_distance_to_point(self, value):
        return math.sqrt((self.x-value.x)**2+(self.y-value.y)**2)
    
class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return f"<{self.x}, {self.y}>"
    
    def __add__(self, value):
        return Vector(self.x+value.x, self.y+value.y)
    
point1 = Point(10,5)  
point2= Point(4,8)
point3= Point(10,5)

print(f"point1 is equal to point2 {point1.__eq__(point2)}")
print(f"point1 is equal to point3 {point1.__eq__(point3)}")
print(f"point2 is equal to point3 {point2.__eq__(point3)}")

print(f"point1 is {point1}")
print(f"point2 is {point2}")
print(f"point3 is {point3}")

print(f"Euclidean distance between point 1 and 2 is: {point1.eucl_distance_to_point(point2)}")
print(f"Euclidean distance between point 1 and 3 is: {point1.eucl_distance_to_point(point3)}")
print(f"Euclidean distance between point 2 and 3 is: {point2.eucl_distance_to_point(point3)}")

vector1 = Vector(5,10)
vector2 = Vector(4,8)

print(f"vector1 {vector1}")
print(f"vector2 {vector2}")

print(f"vectors sum is {vector1.__add__(vector2)}")