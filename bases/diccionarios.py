mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")
    
cuadrados = {x: x**2 for x in range(1, 6)}
print(cuadrados)

print(mi_diccionario.get("nombre", "Desconocido"))

mi_diccionario2 = {
    "nombre": "María",
    "edad": 25,
    "ciudad": "Barcelona"
}

mi_diccionario.update(mi_diccionario2)
print(mi_diccionario)

my_dict = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "Valencia",
    "hobbies": ["fútbol", "música", "viajar"],
    "trabajo": {
        "empresa": "Tech Solutions",
        "puesto": "Desarrollador"
    }
}

print(my_dict["hobbies"][1])
print(my_dict["trabajo"]["empresa"])