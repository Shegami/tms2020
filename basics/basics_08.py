"""
Дана длина ребра куба. Найти объем куба и площадь всей его поверхности.
"""

length = 13

square = length ** 2
square_cube = square * 6

volume_cube = square * length

print(square_cube, volume_cube, sep='\n')
