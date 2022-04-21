menu = """
    Bienvenido al conversor de monedas 🪙
    
    1 - a Pesos colombianos
    2 - a Pesos argentinos
    3 - a Pesos Mexicanos
    
    Elige una opción: 
"""

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Cúantos dinero quieres convertir: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $ " + dolares + "dólares")
elif opcion == 2:
    pesos = input("Cúantos dinero quieres convertir: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $ " + dolares + "dólares")
elif opcion == 3:
    pass
else:
    print("Digita una opcion valida")