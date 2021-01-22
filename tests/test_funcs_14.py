"""
Написать 12 функций по переводу:
Дюймы в сантиметры, Сантиметры в дюймы,
Мили в километры, Километры в мили,
Фунты в килограммы, Килограммы в фунты,
Унции в граммы, Граммы в унции, Галлон в литры,
Литры в галлоны, Пинты в литры, Литры в пинты.
"""

from funcs.funcs_14 import inch_to_cm, cm_to_inch,\
                           miles_to_km, km_to_miles,\
                           pounds_to_kg, kg_to_pounds,\
                           ounce_to_gr, gr_to_ounce,\
                           gallon_to_litre, litre_to_gallon,\
                           pint_to_litre, litre_to_pint


def test_inch():
    result = inch_to_cm(1)
    assert result == 2.54
    result = cm_to_inch(1)
    assert result == 0.393701


def test_miles():
    result = miles_to_km(1)
    assert result == 1.60934
    result = km_to_miles(1)
    assert result == 0.621371


def test_pounds():
    result = pounds_to_kg(1)
    assert result == 0.453592
    result = kg_to_pounds(1)
    assert result == 2.20462


def test_ounce():
    result = ounce_to_gr(1)
    assert result == 28.3495
    result = gr_to_ounce(1)
    assert result == 0.035274


def test_gallon():
    result = gallon_to_litre(1)
    assert result == 3.78541
    result = litre_to_gallon(1)
    assert result == 0.264172


def test_pint():
    result = pint_to_litre(1)
    assert result == 0.473176
    result = litre_to_pint(1)
    assert result == 2.11338
