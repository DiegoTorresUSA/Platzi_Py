def divisors(num):
    divisors = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input("Digita un numero: "))
        if num < 0:
            raise ValueError('No es posible un numero negativo')
        print(divisors(num))
    except ValueError as ex:
        print(ex.args)


    # try:
    #     try:
    #         num = int(input("Digita un numero: "))
    #         print(divisors(num))
    #     except TypeError:
    #         print("Debes ingresar un numero positivo")
    # except ValueError:
    #     print("Debes ingresar un entero")


if __name__ == '__main__':
    run()