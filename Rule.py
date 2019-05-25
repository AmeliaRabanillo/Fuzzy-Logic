import member_functions as mf
from utils import variable


class caracteristic:  # por ejemplo servicio y las funciones serian bueno, regular, malo
    def __init__(self, nombre):
        self.nombre = nombre
        self.functions = {}  # dictionary for functions
        self.value = 0

    def add_triangle(self, name, points):
        self.functions[name] = mf.triangle(points)
        return variable(name)

    def add_trapezoidal(self, name, points):
        self.functions[name] = mf.trapezoidal(points)
        return variable(name)

    def add_polinomial(self, name, coeficients):
        self.functions[name] = mf.polinomial(coeficients)
        return variable(name)

    def add_regular(self, name, points):
        self.functions[name] = mf.regular(points)
        return variable(name)

    def set_value(self, n):
        self.value = n

    def evaluate(self, name):
        return self.functions[name].evaluate(self.value)


class rule:  # por ejemplo si el servicio es bueno y la comida es regular => la propina es buena
    def __init__(self, condition, consecuence):
        self.condition = condition
        self.consecuence = consecuence


class condition:  # por ejemplo si el servicio es bueno y la comida regular
    def __init__(self, pairs, logic_op=[]):  # los pares serian (servicio, bueno), (comida,regular) y los logicOp [and]
        self.pairs = pairs
        self.logic_op = logic_op
