import string


# se coloca el : para dejarlo tipado, mas claro y definimos que la funcion devuelve un bool
# el replace, reemplaza los espacios que hayan en el string
# con el modulo mypy podemos ver los errrores de tipado --check-untyped-defs
# :: permite darle la vuelta al string

def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    print(is_palindrome("1000"))

if __name__ == '__main__':
    run()
