from functions import square


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def squarePoint(self):
        print(square(self.x))


p = Point(3, 5)

print(p.x)
print(p.y)

p.squarePoint()

print(p.x)
print(p.y)
