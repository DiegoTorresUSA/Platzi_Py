# hola 3 -> hola hola hola
# Facundo 2 Facundo Facundo


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "solo puedas utilizar cadenas"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10(5))

if __name__ == '__main__':
    run()