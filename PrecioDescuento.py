# # funcion Calcular descuento en PY
#
# def precioDescuento(precio, descuento):
#     porcentajeDescuento = 100 - descuento
#     precioDescuento = (precio * porcentajeDescuento) / 100
#     print("el valor con el descuento corresponde a:", precioDescuento)
#
# precio = int(input("Digita el precio para calcular el descuento"))
# descuento = int(input("Digita el porcentaje de descuento"))
#
# precioDescuento(precio, descuento)
#
#
# # funcion calcular area, base -- cuadrado
# #const ladoCuadrado = 5;
# #const perimetroCuadrado = ladoCuadrado * 4;
# #const areaCuadrado = ladoCuadrado * ladoCuadrado;
#
# def calculoPerimetroCuadrado(lado):
#     lado = int(input("Digita el lado del cuadrado"))
#     perimetroCuadrado = (lado * 4)
#     print("el perimetro es de: ", perimetroCuadrado, "cm")
#
# calculoPerimetroCuadrado(5)
#
# def calculoAreaCuadrado(lado):
#     lado = int(input("Digita el lado del cuadrado"))
#     areaCuadrado = lado * lado
#     print("el area del cuadrado es: ", areaCuadrado)
# calculoAreaCuadrado(1)
#
#
# # funcion calcular figura Triangulo, base -- cuadrado
# #const areaTriangulo = (baseTriangulo * alturaTriangulo) / 2;
# #const perimetroTriangulo = ladoTriangulo1+ ladoTriangulo2 + baseTriangulo;
#
# def areaTriangulo(base, altura):
#     base = int(input("Digita la base del triangulo"))
#     altura = int(input("Digita la altura del triangulo"))
#     areaTriangulo = (base * altura) / 2
#     return areaTriangulo
#
# print(areaTriangulo(1,2))
#
# def perimetroTriangulo (lado, base):
#     lado =  int(input("Digita el lado del triangulo"))
#     base = int(input("Digita la base del triangulo"))
#     perimetroTriangulo = (lado + lado + base)
#     return  perimetroTriangulo
#
# print(perimetroTriangulo(1,2))


# Figura Circulo - Diametro = radio * 2;, perimetro = diametro * PI, area = radio * radio * PI


def diametroCirculo ():
    radio = float(input("Digita el diametro del circulo"))
    diametro = (radio * radio)
    return diametro

res = print(diametroCirculo())

def perimetroCirculo():
    PI = 3.141516
    diametro = res * PI
    print(diametro)
    perimetro = diametro * PI
    return perimetro

print(perimetroCirculo())

