# def run():
#     string = input("Digita la frase que quieres validar: ").lower().split()
#     inverso = string[::-1]
#
#     if (string == inverso):
#         print("Es palíndromo")
#         print(inverso)
#     else:
#         print("No es palindromo")
#         print(inverso)

def palindromo(string):
    string = string.replace(' ', '')
    string = string.lower()
    string_inverso = string[::-1]
    if string == string_inverso:
        return True
    else:
        return False

def run():
    string = input("Digita la palabra: ")
    es_palindromo = palindromo(string)
    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")


if __name__ == '__main__':
    run()
