
ip_address = "192.168.1.34"
port = 80
score = 9.2

# Emprimir tipos de dato
print(type(ip_address))
print(type(port))
print(type(score))

# Type casting
score_to_int = int(score)

print(score_to_int)
print(type(score_to_int))

my_ports = []
my_ports.append(22)
my_ports.append(80)
my_ports.append(433)

for port in my_ports:
    print(f"Port: {port}")

print(f"La lista tiene {len(my_ports)} puertos")
my_local_ports = [8080, 80, 1433]

#  Formas de agregar elementos
my_local_ports.extend([74,23])
my_local_ports += [24,42]

my_local_ports_ordered = sorted(my_local_ports)
del my_local_ports_ordered[0]

print(f"Mis puertos locales:")
for port in my_local_ports_ordered:
    print(f"Puerto local: {port}")

print(f"La lista de puertos locales tiene: {len(my_local_ports)} elementos!")

slicing = my_local_ports_ordered[:4]
print(f"Primeros elementos en la lista: ")
for elem in slicing:
    print(elem)

slicing.insert(2, 9)
print(slicing)

puertos_objetivo = [13,52,1,5,67,23, 26, 64,67,80,1433, 34,12,25,26,56,11,20]
primera_aparicion = puertos_objetivo.index(23)
indices_repetidos = [ idx for idx, elem in enumerate(puertos_objetivo) if elem == 26]
print(f"Indices donde aparece el numero 26: {indices_repetidos}")
puertos_obj_set = set(puertos_objetivo)
print(f"Puertos objetivo sin duplicados: {puertos_obj_set}")
print(f"Puertos objetivo ordenados sin duplicados: {sorted(puertos_obj_set)}")

print(f"El puerto mayor es: {max(puertos_obj_set)}")
print(f"El puerto menor es: {min(puertos_obj_set)}")

calificaciones = [10, 9.8, 8.9, 7.9, 9.2, 9, 8.6, 7, 8, 9.6, 10]
promedio = sum(calificaciones) / len(calificaciones)
print(f"El promedio es: {round(promedio, 2)}")

print("\nFin del programa!\n")