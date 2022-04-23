def conversor_monedaPesos(tipo_pesos, valor_dolar):
    valor = input("Cúantos dinero " + tipo_pesos + " quieres convertir: ")
    valor = float(valor)
    dolares = valor / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $ " + dolares + "dólares")


menu = """
    Bienvenido al conversor de monedas 🪙
    
    1 - a Pesos colombianos
    2 - a Pesos argentinos
    3 - a Pesos Mexicanos
    
    Elige una opción: 
"""
opcion = int(input(menu))

if opcion == 1:
    conversor_monedaPesos("Colombianos", 3875)
elif opcion == 2:
    conversor_monedaPesos("argentinos", 60)
elif opcion == 3:
    pass
else:
    print("Digita una opcion valida")