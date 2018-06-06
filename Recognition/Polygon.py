class Polygon:
    def __init__(self, *args):
        self.points = args

    def __str__(self):
        return ''.join(str(point) for point in self.points)

    def __repr__(self):
        return self.__str__()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'[x={self.x}, y={self.y}]'

    def __repr__(self):
        return self.__str__()
