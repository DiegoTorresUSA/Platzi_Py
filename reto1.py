
def suma_decorator(f):
    def mensaje(a: int, b:int) -> int:
        print("la funcion mensaje ha sido llamada")
        return f(a, b)
    return mensaje

@suma_decorator
def suma(a, b):
    return a + b

print(suma(5,8))



