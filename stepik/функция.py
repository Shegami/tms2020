def f(x):
    if x <= -2:
        y = 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        y = - (x / 2)
    else:
        y = (x - 2) ** 2 + 1
    return y