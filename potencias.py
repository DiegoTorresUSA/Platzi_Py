def run():
    LIMITE = 1000
    potencia = 0
    valor = 2**potencia

    while valor < LIMITE:
        print(valor)
        #res = valor ** potencia
        potencia += 1
        valor = 2**potencia


if __name__ == '__main__':
    run()