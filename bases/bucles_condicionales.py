
for num in range(5):
    print(num)

names = ["S4vitar", "Marcelo", "Hack4u"]
for idx, name in enumerate(names):
    print(f"{idx + 1}> {name}")

condition = 1
while condition < 5:
    print(condition)
    condition += 1

frutas = {
    'manzanas': 5,
    'fresas': 4,
    'kiwi': 6
    }

for fruta, cant in frutas.items():
    print(f"Hay {cant} {fruta} disponibles")

my_list = [[1,2,3], [4,5,6], [7,8,9]]

for elem in my_list:
    for sub_elem in elem:
        print(sub_elem)


edad = 18
nacionalidad = "Mexicana"
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
msj_nacionalidad = ""
if edad >= 18 and nacionalidad == 'Mexicana':
    msj_nacionalidad = "Puedes votar dentro de Mexico"
else:
    msj_nacionalidad = "No puedes votar!"

esta_presente = True if 'Hack4u' in names else False

if esta_presente:
    print(mensaje)
    print(msj_nacionalidad)

numbers_list = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = [num for num in numbers_list if num % 2 != 0]
print(odd_numbers)
todos_son_pares = True

for num in numbers_list:
    if num % 2 != 0:
        todos_son_pares = False
        break

if todos_son_pares:
    print("Todos los valores son pares!")
else:
    print("Hay valores inpares")