def mid_find(list1, value, low, high):

    while low <= high:
        mid = (low + high) // 2
        if list1[mid] < value:
            low = mid+1
        elif list1[mid] > value:
            high = mid-1
        else:
            return mid
    return -1


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7, ]
    num = mid_find(list1, 5, 0, 6)
    print(num)
