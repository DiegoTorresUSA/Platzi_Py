def make_division_by(x):
    '''this closure returns a function that returns the division of a X number by n'''
    def divisor(n):
        if n == 0:
            print("No puedes dividir por cero")
        else:
            return n / x
    return divisor

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print((division_by_5(100)))
    division_by_18 =make_division_by(18)
    print(division_by_18(54))


if __name__ == '__main__':
    run()