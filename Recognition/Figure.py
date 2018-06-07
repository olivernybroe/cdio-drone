class Polygon:
    def __init__(self, *args):
        self.points = args

    def __str__(self):
        return f'Polygon['+", ".join(str(point) for point in self.points)+']'

    def __repr__(self):
        return self.__str__()


class Ellipse:
    def __init__(self, center, minLength, maxLength, angle):
        self.center = center
        self.minLength = minLength
        self.maxLength = maxLength
        self.angle = angle

    def __str__(self):
        return f'Ellipse[center={str(self.center)}, ' \
               f'min={self.minLength:.2f}, max={self.maxLength:.2f}, ' \
               f'angle={self.angle:.2f}]'

    def __repr__(self):
        return self.__str__()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'[x={self.x:.2f}, y={self.y:.2f}]'

    def __repr__(self):
        return self.__str__()
