import random

numero = random.randint(1, 100)

unidades = {
    "1": "Uno",
    "2": "Dos",
    "3": "Tres",
    "4": "Cuatro",
    "5": "Cinco",
    "6": "Seis",
    "7": "Siete",
    "8": "Ocho",
    "9": "Nueve",
}

decenas = {
    "10": "Diez",
    "11": "Once",
    "12": "Doce",
    "13": "Trece",
    "14": "Catorce",
    "15": "Quine",
    "20": "Veinte",
    "30": "Treinta",
    "40": "Cuarenta",
    "50": "Cincuenta",
    "60": "Sesenta",
    "70": "Setenta",
    "80": "Ochenta",
    "90": "Noventa",
}


def get_number(valor):
    if len(valor) == 1:
        return unidades[valor[0]]

    if len(valor) == 2:
        if valor[0:2] in decenas:
            return decenas[valor[0:2]]
        else:
            return decenas[valor[0] + '0'] + ' y ' + unidades[valor[1]]
    return 'Cien'


if __name__ == '__main__':
    print(numero)
    print(get_number(str(numero)))
