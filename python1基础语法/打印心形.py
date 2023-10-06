def heart1():
    for i in range(1, 5):
        for j in range(1, 4 - i + 1):
            print(" ", end="")
        for j in range(1, 2 * i + 2):
            if j % 2 == 0:
                print(" ", end="")
            else:
                print("*", end="")
        for j in range(1, 9-i*2+1):
            print(" ", end="")
        for j in range(1, 2 * i + 2):
            if j % 2 == 0:
                print(" ", end="")
            else:
                print("*", end="")
        print()


def heart2():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(" ", end="")
        for j in range(1, 10 - i + 1):
            print("* ", end="")
        print()


if __name__ == '__main__':
    heart1()
    heart2()
