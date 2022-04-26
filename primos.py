def esPrimo (numero):
    contador = 0
    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % 2 == 0:
            contador += 1
        if contador == 0:
            return True
        else:
            return False



def run():
    numero = int(input("Digita el numero que quieres evaluar"))
    if esPrimo(numero):
        print("El numero es primo")
    else:
        print("El numero no es primo")



if __name__ == '__main__':
    run()