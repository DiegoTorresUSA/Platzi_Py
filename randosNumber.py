import random

# listas = [], tuplas = (), diccionarios = {}

def run():
    num_adivina = random.randint(1, 100)
    num_usuario = int(input("Escoge un número entre 1 y 100: "))

    while num_usuario != num_adivina:
        if num_usuario > num_adivina:
            num_usuario = int(input("Elige uno mas pequeño"))
        else:
            num_usuario = int(input("Elige uno mas grande"))
    print("Felicitaciones Ganaste")
# print(random.randint(1, 100))


if __name__ == '__main__':
    run()
