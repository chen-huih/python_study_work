def function1(num1):
    if num1 == 1:
        return 1
    return num1 + function1(num1 - 1)


if __name__ == '__main__':
    num = function1(100)
    print(num)
