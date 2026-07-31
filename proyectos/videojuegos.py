
juegos = ["Super Mario Bros", "Zelda", "Cyberpunk 2077", "Final Fantasy"]
tope_ventas = 500
# Generos
generos = {
    "Super Mario Bros": "Aventura",
    "Zelda": "Aventura",
    "Cyberpunk 2077": "Rol",
    "Final Fantasy": "Rol"
}

ventas_y_stock = {
    "Super Mario Bros": (400, 200),
    "Zelda": (600, 20),
    "Cyberpunk 2077": (60, 120),
    "Final Fantasy": (924, 3)
}

clientes = {
    "Super Mario Bros": {"Alexis","Isabel","Irma", "Delfino"},
    "Zelda": {"Alexis","Isabel","Carlitos"},
    "Cyberpunk 2077": {"Alexis","Isabel","Angel"},
    "Final Fantasy": {"Alexis","Isabel"},
}

mi_juego = "Super Mario Bros"

def sumario(juego):
    # Sumario
    print(f"[i] Resumen del juego {juego}\n")
    print(f"\t[+] Genero del juego: {generos[juego]}")
    print(f"\t[+] Total de ventas para este juego: {ventas_y_stock[juego][0]}")
    print(f"\t[+] Total de stock para este juego: {ventas_y_stock[juego][1]}")
    print(f"\t[+] Clientes que han adquirido este juego: {', '.join(clientes[juego])}")
    print("\n")

for juego in juegos:
    if ventas_y_stock[juego][0] > tope_ventas:
        sumario(juego)

ventas_totales = lambda: sum(ventas for juego, (ventas, _ ) in ventas_y_stock.items() if ventas_y_stock[juego][0] > tope_ventas )

print(f"\n[+] El total de ventas de todos los productos ha sido de {ventas_totales()} productos.")



