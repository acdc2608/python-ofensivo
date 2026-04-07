from functools import reduce

# Funciones lambda

mi_funcion = lambda: "Hola mundo"
cuadrado_numero = lambda x: x ** 2
suma = lambda x, y: x + y

numeros = [1,2,3,4,5,6]

print(cuadrado_numero(5))
print(suma(36,24))

cuadrados = list(map(lambda x: x ** 2, numeros))
even_numbers = list(filter(lambda num: num % 2 == 0, numeros))
total = reduce(lambda accum, elem: accum * elem, numeros)
print(cuadrados)
print(even_numbers)
print(total)