def es_primo(numero: int):
    for i in range(1, numero+1):
        if numero == 0 or numero == "":
            return False
        elif numero % 2 == 0:
            return True
        else:
            return False
    

def run():
    numero = int(input('digita el numero que quieres evaluar'))
    if es_primo(numero):
         print("El numero es primo")
    else:
         print("El numero no es primo")


if __name__ == '__main__':
    run()
