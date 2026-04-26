
# Deben tener valores unicos

mi_conjunto = {1, 2, 3, 4, 5}
mi_conjunto.update({6, 7, 8})
mi_conjunto.add(9)
mi_conjunto.discard(4) # no lanza error si el elemento no existe
print(mi_conjunto)

mi_segundo_conjunto = {6, 7, 8, 9, 10}
# Interseccion: elementos que estan en ambos conjuntos
interseccion = mi_conjunto.intersection(mi_segundo_conjunto)
print(interseccion)

# Union: elementos que estan en al menos uno de los conjuntos
union = mi_conjunto.union(mi_segundo_conjunto)
print(union)

print(mi_conjunto.issubset(union))

valores_totales = [4, 10, 15, 20, 25, 30, 2, 3, 4, 2, 4,2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 30, 40]
no_repeat = set(valores_totales)
print(no_repeat)

numeros = set(range(10000))
print(123497 in numeros)

usuarios_facebook = {"juan", "maria", "pedro", "lucia"}
usuarios_instagram = {"maria", "lucia", "ana", "carlos"}

ambas_redes = usuarios_facebook.intersection(usuarios_instagram)
print(ambas_redes)

todos_usuarios = usuarios_facebook.union(usuarios_instagram)
print(todos_usuarios)

diferentes_redes = usuarios_facebook.difference(usuarios_instagram)
print(diferentes_redes)

diferencia_completa = usuarios_facebook.symmetric_difference(usuarios_instagram)
print(diferencia_completa)