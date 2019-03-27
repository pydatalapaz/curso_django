from ejemplo_uno import get_number

english_unit = {
    '1': 'One',
    '2': 'Two',
    '3': 'Tree',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
}

english_decimals = {
    '10': 'Ten',
    '11': 'Eleven',
    '15': 'FifTeen',
    '13': 'thirteen',
    '12': 'Twelve',
    '20': 'Twenty',
    '30': 'Thirty',
    '40': 'Forty',
    '50': 'Fifty',
    '60': 'Sixty',
    '70': 'Seventy',
    '80': 'Eighty',
    '90': 'Ninety',
}


roman_unit = {
    '1': 'I',
    '5': 'V',
    '10': 'X',
    '50': 'L',
    '100': 'C',
}


def numbert_to_english(numero):
    if len(numero) == 1:
        return english_unit[numero]

    if len(numero) == 2:
        if numero in english_decimals:
            return english_decimals[numero]
        else:
            if numero[0] == '1':
                return english_unit[numero[1]] + 'teen'
            else:
                return english_decimals[numero[0] + '0'] + ' ' + english_unit[numero[1]]


def digit_to_roman(numero, base=1):
    if numero == 0:
        return ''
    if numero == 1:
        return roman_unit[str(numero * base)]
    if 1 < numero <= 3:
        res = ''
        for i in range(numero):
            res += digit_to_roman(1, base)
        return res
    if numero == 4:
        return roman_unit[str(1 * base)] + roman_unit[str((numero + 1) * base)]
    if 4 < numero <= 8:
        return roman_unit[str(5 * base)] + digit_to_roman(numero - 5, base)
    if numero == 9:
        return roman_unit[str(1 * base)] + roman_unit[str((numero + 1) * base)]


def number_to_roman(number):
    base = int((10 ** len(number)) / 10)
    response = ''
    for i in number:
        response += digit_to_roman(int(i), base)
        base = int(base / 10)

    return response


if __name__ == '__main__':
    val_uno = input('Indtroduca el Prime Valor: ')
    val_dos = input('Indtroduca el Prime Valor: ')

    if len(val_uno) > 1 or len(val_dos) > 1:
        raise ValueError('Solo numeros de uno a dos')

    resultado_suma = int(val_uno) + int(val_dos)
    resultado_producto = int(val_uno) * int(val_dos)

    print('La Suma es {}, y el Producto es {}'.format(resultado_suma, resultado_producto))
    print('La Suma en romano es: {}'.format(number_to_roman(str(resultado_suma))))
    print('El Producto en Spanish es: {}'.format(get_number(str(resultado_producto))))
    print('El Producto en English es: {}'.format(numbert_to_english(str(resultado_producto))))
