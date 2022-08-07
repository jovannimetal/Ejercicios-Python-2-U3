import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))
        
    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        perim = 0.0
        for i in range(len(self.__vertices)):
            perim += self.__vertices[i].distance_from_point(self.__vertices[(i+1)%3])
        return perim

if __name__ == "__main__":
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())