from math import comb

# Función para calcular el número de diagonales de cualquier polígono
calcular_diagonales = lambda n: comb(n, 2) - n

# Función para calcular la medida total de todos los ángulos interiores de cualquier polígono
calcular_angulos_interiores = lambda n: (n - 2) * 180

# Función para calcular la medida de los ángulos exteriores de un polígono regular
calcular_angulos_exteriores = lambda n: 360 / n
#no le vi mucho uso de programacion funcional en mi tp