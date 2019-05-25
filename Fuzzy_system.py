import member_functions as mf


class fuzzy_system:
    def __init__(self, rules, inVariables, outVariable):
        self.rules = rules
        self.inVariables = inVariables
        self.outVariables = outVariable

    def Apply(self):
        trunc = self.Mandani()
        return self.Maximum(trunc)

    # metodos de fusificacion
    def Mandani(self):
        trunc = []
        for rule in self.rules:
            rule_ev = self.evaluate_rule(rule.condition)
            caract, variable = rule.consecuence.pairs
            trunc.append(caract.functions[variable.name].truncate(rule_ev))

        return trunc

    # metodos de desfusificacion
    
    def Maximum(self, trunc):  # todo ver si el la x o la y
        # metodo del primer maximo
        assign = True
        for i in range(0, len(trunc)):
            if trunc[i].points[0].x == trunc[i].points[1].x:
                continue

            if assign:
                max_pos = i
                max_value = trunc[i].get_max_point().y
                assign = False
                continue

            if max_value < trunc[i].get_max_point().y:
                max_value = trunc[i].get_max_point().y
                max_pos = i

        return trunc[max_pos].get_max_point().x

    def evaluate_rule(self, condicion):
        pairs = condicion.pairs
        logic_op = condicion.logic_op
        aux = 0
        for i in range(0, len(pairs)):
            caract, variable = pairs[i]
            value = caract.evaluate(variable.name)
            if i == 0:
                aux = value
            else:
                if logic_op[i - 1] is 'and':
                    if aux > value:
                        aux = value

                if logic_op[i - 1] is 'or':
                    if aux < value:
                        aux = value

        return aux
