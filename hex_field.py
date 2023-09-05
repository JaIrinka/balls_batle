from math import pi as PI, cos, sin, sqrt


def hex_field(canvas, size, max_x, mav_y):
    hexagons = []
    for center in get_center(size, max_x, mav_y):
        hexagon = make_hexagon(center, size)
        points = []
        for p in hexagon:
            points.extend(p.get_coords())
        hexagons.append(canvas.create_polygon(
            *points, outline="blue", fill="orange", width=1
        ))
    return hexagons


def get_center(size, max_x, mav_y):
    top_offset = sqrt(3)/2 * size
    r = 0
    while top_offset <= mav_y:
        if not r:
            left_offset = size
            r = 1
        else:
            left_offset = 0
            r = 0
        while left_offset <= max_x:
            center = Point(left_offset, top_offset)
            left_offset += size*2
            yield center
        top_offset += sqrt(3) * size


def make_hexagon(center, size):
    hexagon = []
    for j in range(6):
        hexagon.append(hex_corner(center, size, j))
    return hexagon


def hex_corner(center, size, i):
    angle_deg = 60 * i + 30
    angle_rad = PI / 180 * angle_deg
    return Point(center.x + size * cos(angle_rad), center.y + size * sin(angle_rad))


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

    # def __abs__(self):
    #     return hypot(self.x, self.y)

    # def __bool__(self):
    #     return bool(abs(self))

    # def __add__(self, other):
    #     x = self.x + other.x
    #     y = self.y + other.y
    #     return Point(x, y)

    # def __mul__(self, scalar):
    #     return Point(self.x * scalar, self.y * scalar)

    def get_coords(self):
        return self.x, self.y
