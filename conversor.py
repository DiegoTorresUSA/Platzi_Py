pesos = input("Cúantos dinero quieres convertir: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)
print("tienes $ " + dolares + "dólares")
