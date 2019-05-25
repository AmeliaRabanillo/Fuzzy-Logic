class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Polygon:
    def __init__(self, points):
        self.points = points


def slope(p1, p2):  # calcular la pendiente dados dos puntos
    f = float(p1.y - p2.y) / float(p1.x - p2.x)
    return (p1.y - p2.y) / (p1.x - p2.x)


def trace(m, p):  # calcular la traza dados la pendiente y un punto
    return p.y - m * p.x


class variable:
    def __init__(self, name):
        self.name = name
