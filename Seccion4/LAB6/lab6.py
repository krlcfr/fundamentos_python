kilometers = 12.25
miles = 7.38

# Para convertir millas a kilómetros, multiplicamos por 1.61
miles_to_kilometers = miles * 1.61

# Para convertir kilómetros a millas, dividimos por 1.61
kilometers_to_miles = kilometers / 1.61

# Imprimimos los resultados. 
# round(valor, 2) nos asegura que solo se vean dos números después del punto decimal.
print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
