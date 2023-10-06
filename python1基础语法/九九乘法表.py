def mul_table():
    for i in range(1, 10):
        for j in range(1, i+1):
            x = j*i
            print("%d*%d=%d" % (j, i, x), end="\t")
        print("")


if __name__ == '__main__':
    mul_table()