# def run():
#     for contador in range(1000):
#         if contador % 2:
#             continue
#         print(contador)

# def run():
#     string = input("Digita tu nombre")
#     for letra in string:
#          if letra == 'o':
#              print(letra)
#              print("Paramos en la letra O")
#              break
#          else:
#              print(letra)

def run():
    adivina = int(input("Adivina el numero"))
    valor = 5
    while adivina != valor:
        print("Sigue intentando")
        adivina = int(input("Adivina el numero"))
    print("felicitaciones Ganaste!!!")



if __name__ == '__main__':
    run()