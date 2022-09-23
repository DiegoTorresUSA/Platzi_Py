from datetime import datetime

# el metodo .total_seconds nos da los segundos que han pasado
# el _ nos sirve, cuando solo queremos hacer el ciclo, sin importar que hay en el ciclo

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass


@execution_time
def saludo(nombre = "Cesar"):
    print("Hola " + nombre)


@execution_time
def suma(a: int, b: int) -> int:
    return a + b

random_func()
saludo("FAcundo")
suma(5, 5)







