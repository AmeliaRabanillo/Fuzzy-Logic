from Rule import caracteristic
from Rule import condition
from Rule import rule
from utils import point
from Fuzzy_system import fuzzy_system

# Las funciones de pertenencia estan graficadas en el informe

# Ejemplo 1
# R1 aire = frio      => velocidad = parada
# R2 aire = fresco    => velocidad = lenta
# R3 aire = correcto  => velocidad = media
# R4 aire = calido    => velocidad = rapida
# R5 aire = caliente  => velocidad = maxima

# Funciones de Pertenencia
aire = caracteristic("aire")
aire_frio = aire.add_regular("frio", [point(12, 1), point(15, 0)])
aire_fresco = aire.add_trapezoidal("fresco", [point(12, 0), point(15, 1), point(18, 1), point(22, 0)])
aire_correcto = aire.add_trapezoidal("correcto", [point(18, 0), point(22, 1), point(25, 1), point(27, 0)])
aire_calido = aire.add_trapezoidal("calido", [point(25, 0), point(27, 1), point(30, 1), point(32, 0)])
aire_caliente = aire.add_regular("caliente", [point(30, 0), point(32, 1)])

velocidad = caracteristic("velocidad")
velocidad_parada = velocidad.add_regular("parada", [point(0, 1), point(1, 0)])
velocidad_lenta = velocidad.add_trapezoidal("lenta", [point(0, 0), point(1, 1), point(2, 1), point(3, 0)])
velocidad_media = velocidad.add_trapezoidal("media", [point(1, 0), point(2, 1), point(3, 1), point(4, 0)])
velocidad_rapida = velocidad.add_trapezoidal("rapida", [point(3, 0), point(4, 1), point(5, 1), point(6, 0)])
velocidad_maxima = velocidad.add_regular("maxima", [point(5, 0), point(6, 1)])

# reglas
condition1 = condition([(aire, aire_frio)], [])
consecuence1 = condition((velocidad, velocidad_parada))
rule1 = rule(condition1, consecuence1)

condition2 = condition([(aire, aire_fresco)], [])
consecuence2 = condition((velocidad, velocidad_lenta))
rule2 = rule(condition2, consecuence2)

condition3 = condition([(aire, aire_correcto)], [])
consecuence3 = condition((velocidad, velocidad_media))
rule3 = rule(condition3, consecuence3)

condition4 = condition([(aire, aire_calido)], [])
consecuence4 = condition((velocidad, velocidad_rapida))
rule4 = rule(condition4, consecuence4)

condition5 = condition([(aire, aire_caliente)], [])
consecuence5 = condition((velocidad, velocidad_maxima))
rule5 = rule(condition5, consecuence5)

# sistema
fs = fuzzy_system([rule1, rule2, rule3, rule4, rule5], [aire], velocidad)

# Pruebas
print('Ejemplo#1')
aire.set_value(0)
print('Temperatura del aire: 0, velocidad: ' + str(fs.Apply()))

aire.set_value(15)
print('Temperatura del aire: 15, velocidad: ' + str(fs.Apply()))

aire.set_value(25)
print('Temperatura del aire: 25, velocidad: ' + str(fs.Apply()))

aire.set_value(30)
print('Temperatura del aire: 30, velocidad: ' + str(fs.Apply()))

aire.set_value(45)
print('Temperatura del aire: 45, velocidad: ' + str(fs.Apply()))

# Ejemplo2
# R1 servicio = pobre     AND comida = mala         => propina = poca
# R2 servicio = bueno     AND comida = regular      => propina = promedio
# R3 servicio = excelente OR  comida = deliciosa    => propina = generosa

# Funciones de Pertenencia
servicio = caracteristic("servicio")
servicio_pobre = servicio.add_regular("pobre", [point(3, 1), point(4, 0)])
servicio_bueno = servicio.add_trapezoidal("bueno", [point(3, 0), point(4, 1), point(7, 1), point(8, 0)])
servicio_excelente = servicio.add_regular("excelente", [point(7, 0), point(8, 1)])

comida = caracteristic("comida")
comida_mala = comida.add_regular("mala", [point(3, 1), point(4, 0)])
comida_regular = comida.add_trapezoidal("regular", [point(3, 0), point(4, 1), point(7, 1), point(8, 0)])
comida_deliciosa = comida.add_regular("deliciosa", [point(7, 0), point(8, 1)])

propina = caracteristic("propina")
propina_poca = propina.add_regular("poca", [point(15, 1), point(20, 0)])
propina_promedio = propina.add_trapezoidal("promedio", [point(15, 0), point(20, 1), point(45, 1), point(50, 0)])
propina_generosa = propina.add_regular("generosa", [point(45, 0), point(50, 1)])

# Reglas
condition1 = condition([(servicio, servicio_pobre), (comida, comida_mala)], ['and'])
consecuence1 = condition((propina, propina_poca), [])
rule1 = rule(condition1, consecuence1)

condition2 = condition([(servicio, servicio_bueno), (comida, comida_regular)], ['and'])
consecuence2 = condition((propina, propina_promedio), [])
rule2 = rule(condition2, consecuence2)

condition3 = condition([(servicio, servicio_excelente), (comida, comida_deliciosa)], ['or'])
consecuence3 = condition((propina, propina_generosa), [])
rule3 = rule(condition3, consecuence3)

# sistema
fs = fuzzy_system([rule1, rule2, rule3], [servicio, comida], propina)

# pruebas
print()#todo debug xq da mal
print('Ejemplo#2')
servicio.set_value(3.5)
comida.set_value(3)
print("Sevicio: 3.5, comida: 3 => propina: " + str(fs.Apply()))

servicio.set_value(5)
comida.set_value(4)
print("Sevicio: 5, comida: 4 => propina: " + str(fs.Apply()))

servicio.set_value(4)
comida.set_value(8)
print("Sevicio: 4, comida: 8 => propina: " + str(fs.Apply()))

servicio.set_value(9)
comida.set_value(5)
print("Sevicio: 9, comida: 5 => propina: " + str(fs.Apply()))
