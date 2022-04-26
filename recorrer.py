def run():
    string = input("Digita la cadena de caracteres").split()

    for letra in string:
        print(letra.upper())



if __name__ == '__main__':
    run()