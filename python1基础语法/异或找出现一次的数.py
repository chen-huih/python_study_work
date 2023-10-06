def find_101():
    list1=[9,3,5,5,3,2,2]
    num = list1[0]
    for i in range(1, len(list1)):
        num = num ^ list1[i]
    print(num)
def find_102():
    """分治法求两个出现一次的数"""
    list = [2,3,4,3,2,7] #有两个出现一次的数
    result = 0
    for i in list:
        result^=i
    print("异或结果为%d" % result)
    splite = result&-result     #一个数与它的负数相与得到的是它二进制的最后一个1
    result1 = 0
    result2 = 0
    for i in list:
        if i&splite:
            result1^=i
        else:
            result2^=i
    print("出现一次的俩个数是%d,%d" % (result1, result2))
if __name__ == '__main__':
    find_102()