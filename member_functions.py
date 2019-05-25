from utils import slope, trace, point


class triangle:
    def __init__(self, points):  # asumo que los puntos estan ordenados por x de menor a mayor
        self.points = points
        if len(points) != 3:
            print("Triangle must have 3 points")

    def truncate(self, y):  # trunca el triangulo con una recta parametro que es paralela a x
        if y >= self.points[1].y:  # significa que la recta esta por encima del triangulo y no lo trunca
            return triangle(self.points)

        mr1 = slope(self.points[0], self.points[1])  # pendiente de los dos primero puntos del triangulo
        mr2 = slope(self.points[1], self.points[2])  # pendiente de los dos segundos puntos del triangulo

        nr1 = trace(mr1, self.points[0])  # traza de la recta fromada por los 2 primeros puntos del triangulo
        nr2 = trace(mr2, self.points[1])  # traza de la recta fromada por los 2 segundos puntos del triangulo

        x1 = (y - nr1) / mr1  # x del punto de interseccion con la primera recta
        x2 = (y - nr2) / mr1  # x del punto de interseccion con la segunda recta

        return trapezoidal([self.points[0], point(x1, y), point(x2, y), self.points[2]])

    def evaluate(self, x):
        if x <= self.points[0].x or x >= self.points[2].x:
            return 0

        if x <= self.points[1].x:
            m = slope(self.points[0], self.points[1])
            n = trace(m, self.points[1])
        else:
            m = slope(self.points[1], self.points[2])
            n = trace(m, self.points[1])

        return m * x - n

    def get_max_point(self):
        return self.points[1]


class trapezoidal:
    def __init__(self, points):
        self.points = points

        if len(points) != 4:
            print("Trapezium must have four points")

        if points[1].y != points[2].y:
            print("Two points of a trapezium must have the same 'y'")

    def truncate(self, y):  # trunca el trapecio con la recta que se le pasa como parametro que es paralela a x
        if y >= self.points[1].y:
            # significa que la recta esta por encima del trapecio
            return trapezoidal(self.points)

        mr1 = slope(self.points[0], self.points[1])  # pendiente de los dos primero puntos del trapecio
        mr2 = slope(self.points[2], self.points[3])  # pendiente de los dos ultimos puntos del trapecio

        nr1 = trace(mr1, self.points[0])  # traza de la recta formada por los 2 primeros del trapecio
        nr2 = trace(mr2, self.points[2])  # traza de la recta formada por los 2 ultimos del trapecio

        x1 = (y - nr1) / mr1  # x del punto de interseccion con la primera recta
        x2 = (y - nr2) / mr2  # x del punto de interseccion con la segunda recta

        return trapezoidal([self.points[0], point(x1, y), point(x2, y), self.points[3]])

    def evaluate(self, x):
        if x <= self.points[0].x or x >= self.points[3].x:
            return 0

        if x >= self.points[1].x and x <= self.points[2].x:
            return 1

        if x > self.points[0].x and x < self.points[1].x:
            m = slope(self.points[0], self.points[1])
            n = trace(m, self.points[0])
        else:
            m = slope(self.points[2], self.points[3])
            n = trace(m, self.points[2])

        return m * x - n

    def get_max_point(self):
        return self.points[1]


class regular:  # todo ver que nombr le pongo a esto, estas son las que son la mitad de un trapecio
    def __init__(self, points):
        self.points = points

        if len(points) != 2:
            print("Regular function must have two points")

    def truncate(self, y):  # si la recta esta por encima de la funcion
        m = slope(self.points[0], self.points[1])
        if (m > 0 and y >= self.points[1].y) or (m < 0 and y >= self.points[0].y):
            return regular(self.points)

        m = slope(self.points[0], self.points[1])
        n = trace(m, self.points[0])

        x = (y - n) / m

        if m > 0:
            return regular([self.points[0], point(x, y)])

        return regular([point(x, y), self.points[1]])


        # todo poner el truncate en un mtod aparte poque me parece que es lo mismo para todso

    def evaluate(self, x):
        m = slope(self.points[0], self.points[1])
        if x <= self.points[0].x:
            if m > 0:
                return 0
            return 1

        if x >= self.points[1].x:
            if m > 0:
                return 1
            return 0

        m = slope(self.points[0], self.points[1])
        n = trace(m, self.points[0])

        return m * x + n

    def get_max_point(self):
        m = slope(self.points[0], self.points[1])
        if m > 0:
            return self.points[1]

        return self.points[0]
