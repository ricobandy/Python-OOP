class Point:
    # Constructor
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # Defining instance methods
    def sqSum(self):
        return (self.x*self.x + self.y*self.y + self.z*self.z)

point = Point(1,3,5)
print(point.sqSum())