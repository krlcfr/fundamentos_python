print("--- DESARROLLADOR DE MECÁNICAS DE JUEGO ---")

# 1. Puntaje Total
print("\n1. Calcular Puntaje Total")
n1 = int(input("Puntos nivel 1: "))
n2 = int(input("Puntos nivel 2: "))
n3 = int(input("Puntos nivel 3: "))
print("Total:", n1 + n2 + n3)

# 2. Tiempo en Segundos
print("\n2. Tiempo Total en Segundos")
h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))
print("Total Segundos:", (h * 3600) + (m * 60) + s)

# 3. Daño Total
print("\n3. Daño Total Causado")
d1 = float(input("Ataque 1: "))
d2 = float(input("Ataque 2: "))
d3 = float(input("Ataque 3: "))
print("Daño Total:", d1 + d2 + d3)

# 5. Porcentaje de Vida
print("\n5. Porcentaje de Vida")
v_max = float(input("Vida Máxima: "))
v_act = float(input("Vida Actual: "))
print("Porcentaje:", (v_act / v_max) * 100, "%")

# 7. Velocidad Promedio
print("\n7. Velocidad Promedio")
dist = float(input("Distancia recorrida (m): "))
tiempo = float(input("Tiempo tomado (s): "))
print("Velocidad:", dist / tiempo, "m/s")

# 11. Daño Crítico
print("\n11. Daño Crítico")
base = float(input("Daño base: "))
mult = float(input("Multiplicador crítico (ej: 1.5): "))
print("Daño Crítico:", base * mult)

# 12. Conversión de Minutos a Horas/Minutos
print("\n12. Tiempo en Horas y Minutos")
t_min = int(input("Total minutos jugados: "))
print("Resultado:", t_min // 60, "horas y", t_min % 60, "minutos")
