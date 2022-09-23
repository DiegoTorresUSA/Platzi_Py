def operaciones(op):
    operacion = int(input("escribe la opcion"))
    def suma(a: int, b:int)->int:
        return a + b

    def resta(a: int, b: int)->int:
        return a -b

    if operacion == 1:
        return suma
    elif operacion == 2:
        return resta

funtion_suma = operaciones(1)
print(funtion_suma(5,5))

function_resta = operaciones(2)
print(function_resta(5,5))