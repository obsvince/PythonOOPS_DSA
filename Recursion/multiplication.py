def mul(a, b):
    if a == 0:
        return 0

    if a < 0:
        return mul(a+1, b) - b
    return mul(a-1, b ) + b


if __name__ == '__main__':
    print(mul(4, 5))
    print(mul(2, 1))
    print(mul(5, -6))
    print(mul(-3, 4))
    print(mul(-2, -5))
