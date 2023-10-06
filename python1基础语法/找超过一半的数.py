def majorityElement(nums):
    """摩尔投票法，又叫火拼"""
    votes = 0
    for num in nums:
        if votes == 0:
            x = num
        if num == x:
            votes += 1
        else:
            votes -= 1
    return x


if __name__ == '__main__':
    list1 = [2, 23, 323, 1, 1, 1, 1, 34]
    num = majorityElement(list1)
    print(num)
