"""
Написать 12 функций по переводу:
Дюймы в сантиметры, Сантиметры в дюймы,
Мили в километры, Километры в мили,
Фунты в килограммы, Килограммы в фунты,
Унции в граммы, Граммы в унции, Галлон в литры,
Литры в галлоны, Пинты в литры, Литры в пинты.
"""


def inch_to_cm(numb):
    result = numb * 2.54
    return result


def cm_to_inch(numb):
    result = numb * 0.393701
    return result


def miles_to_km(numb):
    result = numb * 1.60934
    return result


def km_to_miles(numb):
    result = numb * 0.621371
    return result


def pounds_to_kg(numb):
    result = numb * 0.453592
    return result


def kg_to_pounds(numb):
    result = numb * 2.20462
    return result


def ounce_to_gr(numb):
    result = numb * 28.3495
    return result


def gr_to_ounce(numb):
    result = numb * 0.035274
    return result


def gallon_to_litre(numb):
    result = numb * 3.78541
    return result


def litre_to_gallon(numb):
    result = numb * 0.264172
    return result


def pint_to_litre(numb):
    result = numb * 0.473176
    return result


def litre_to_pint(numb):
    result = numb * 2.11338
    return result


def main():
    print((litre_to_gallon(120)))


if __name__ == '__main__':
    main()
