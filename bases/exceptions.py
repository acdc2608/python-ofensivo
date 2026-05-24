
try:
    num = 5 / 0
except ZeroDivisionError:
    print("No se puede dividir un numero entre 0")
else:
    print(f"El resultado es: {num}")
try:
    texto = "Hola" / 3
except TypeError, ValueError:
    print("Solo es posible dividir numeros")
finally:
    print("Esto siempre se va a ejecutar")


x = -2

if x < 0:
    raise Exception("No se pueden usar numeros negativos")