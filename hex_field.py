from math import pi as PI, cos, sin, sqrt
from configure import WIDTH, HEIGHT


class HexField:
    def __init__(self, canvas, size=10):
        self.size = size
        self.canvas = canvas

    def field(self):
        hexagons = []
        for center in self.get_center():
            hexagon = self.make_hexagon(center)
            points = []
            for p in hexagon:
                points.extend(p.get_coords())
            hexagons.append(self.canvas.create_polygon(
                *points, fill="orange", width=0, outline="black"
            ))
        return hexagons


    def get_center(self):
        top_offset = sqrt(3)/2 * self.size
        r = 0
        while top_offset < HEIGHT + 2*self.size:
            if not r:
                left_offset = sqrt(3)/2 * self.size
                r = 1
            else:
                left_offset = 0
                r = 0
            while left_offset < WIDTH + 2*self.size:
                center = Point(left_offset, top_offset)
                left_offset += sqrt(3) * self.size
                yield center
            top_offset += sqrt(3)/4 * self.size + self.size 


    def make_hexagon(self, center):
        hexagon = []
        for j in range(6):
            hexagon.append(self.hex_corner(center, j))
        return hexagon


    def hex_corner(self, center, i):
        angle_deg = 60 * i + 30
        angle_rad = PI / 180 * angle_deg
        return Point(center.x + self.size * cos(angle_rad), center.y + self.size * sin(angle_rad))

class SquareField:
    def __init__(self, canvas, size=15):
        self.size = size
        self.canvas = canvas

    def field(self):
        squares = []
        for square in self.make_squares():
            points = []
            for p in square:
                points.extend(p.get_coords())
            squares.append(self.canvas.create_rectangle(
                *points, fill="orange", width=0, outline="black"
            ))
        return squares


    def get_lt(self):
        top_offset = sqrt(3)/2 * self.size
        r = 0
        while top_offset < HEIGHT + 2*self.size:
            if not r:
                left_offset = sqrt(3)/2 * self.size
                r = 1
            else:
                left_offset = 0
                r = 0
            while left_offset < WIDTH + 2*self.size:
                center = Point(left_offset, top_offset)
                left_offset += sqrt(3) * self.size
                yield center
            top_offset += sqrt(3)/4 * self.size + self.size 


    def make_squares(self):
        top_offset = 0
        while top_offset < HEIGHT + self.size:
            left_offset = 0
            while left_offset < WIDTH + self.size:
                lt = Point(left_offset, top_offset)
                rb = Point(left_offset + self.size, top_offset + self.size)
                left_offset += self.size
                yield [lt, rb]
            top_offset += self.size

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

    def get_coords(self):
        return self.x, self.y
