import random


def pass_generator():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                  'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['/', '*', '-', '+', '!', '#', '$', '%', '&', '(']

    caracteres = mayusculas + minusculas + numeros + simbolos
    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = ''.join(password)
    return password


def run():
    password = pass_generator()
    print("tu nuevo password es: " + password)


if __name__ == '__main__':
    run()