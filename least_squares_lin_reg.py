from math import sqrt
"""takes x-y-coordinates as a list of tuples and calculates the least squares regression line for the relationship"""
example = [(43, 99), (21, 65), (25, 79), (42, 75), (57, 87), (59, 81)]


def lin_reg(points_list):
    x_sums = 0
    xy_sums = 0
    y_sums = 0
    x_squared_sums = 0
    y_squared_sums = 0

    for i in points_list:
        x, y = i
        temp_x = x
        temp_y = y
        x_squared = x * x
        y_squared = y * y
        xy = x * y

        x_sums += temp_x
        y_sums += temp_y
        x_squared_sums += x_squared
        y_squared_sums += y_squared
        xy_sums += xy

    n = len(points_list)
    m = ((n * xy_sums) - (x_sums * y_sums)) / ((n * x_squared_sums) - (x_sums * x_sums))
    b = (y_sums - (m * x_sums)) / n
    r = ((n * xy_sums) - (x_sums * y_sums)) / sqrt((n * x_squared_sums - (x_sums * x_sums)) * ((n * y_squared_sums) - (y_sums * y_sums)))
    return m, b, r


m1, b1, r1 = lin_reg(example)
print(f'y = {m1}x + {b1}\nr = {r1}')
