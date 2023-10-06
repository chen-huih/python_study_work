import random


class sort_tool():
    @classmethod  # 类方法
    def buubble(cls, list1):
        i = len(list1) - 1
        while i > 0:
            j = 0
            flag = 1
            while j < i:
                if list1[j] > list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]
                    flag = 0
                j += 1
            if flag:
                break
            i -= 1

    @classmethod
    def select(cls, list1):  # 简单选择排序
        arr_len = len(list1)
        for i in range(0, arr_len):
            min_idex = i
            for j in range(i, arr_len):
                if list1[min_idex] > list1[j]:
                    min_idex = j
            list1[i], list1[min_idex] = list1[min_idex], list1[i]

    @classmethod
    def insert(cls, list1):  # 插入排序
        arr_len = len(list1)
        for i in range(1, arr_len):
            num = list1[i]
            index = i
            j = i - 1
            while j >= 0 and list1[j] > num:
                index = j
                list1[j + 1] = list1[j]
                j -= 1
            list1[index] = num

    @classmethod
    def partition(cls, list1, low, high):  # 确定一次快排的中枢位
        pivot = list1[low]
        while low < high:  # low小于high，当两个指针碰到一起时，确定元素插入位置
            while low < high and list1[high] >= pivot:
                high -= 1
            list1[low] = list1[high]
            while low < high and list1[low] <= pivot:
                low += 1
            list1[high] = list1[low]
        list1[low] = pivot
        return low

    @classmethod
    def quick(cls, list1, low, high):
        if low < high:
            pivot = cls.partition(list1, low, high)
            cls.quick(list1, low, pivot - 1)
            cls.quick(list1, pivot + 1, high)

    @classmethod
    def heap(cls, dad_index, arr_len):  # 堆排序
        dad = arr_len // 2 - 1
        pass

    @classmethod
    def adjusttree(cls, ):  # 调整一个大根堆子树
        pass

    @classmethod
    def merge(cls, list1, low, high):  # 归并
        temp_list = [0] * len(list1)
        temp_list[low:high] = list1[low:high]    # high设为high+1时会出错
        mid = (high + low) // 2  # 前一部分多
        i = low
        k = low
        j= mid + 1
        while i <= mid and j <= high:
            if temp_list[i] <= temp_list[j]:
                list1[k] = temp_list[i]
                i += 1
            else:
                list1[k] = temp_list[j]
                j += 1
            k += 1
        while i <= mid:
            list1[k] = temp_list[i]
            k += 1
            i += 1
        while j <= high:
            list1[i] = temp_list[j]
            k += 1
            j += 1

    @classmethod
    def list_merge(cls, list1, low, high):
        if low < high:
            mid = (high - low) // 2
            cls.list_merge(list1, low, mid - 1)
            cls.list_merge(list1, mid, high)
            cls.merge(list1, low, high)

    @classmethod
    def count_sort(cls,list1, ):
        lens = len(list1)
        temp_list = [0]*lens
        for i in range(0, lens):
            temp_list[list1[i]]+=1
        j = 0
        for i in range(0, lens):
            while temp_list[i]:
                list1[j] = i        # 该出易出错
                temp_list[i]-=1
                j+=1

if __name__ == '__main__':
    list1 = [17, 4, 1, 14, 20, 3, 13, 15, 14, 4]
    list2 = []
    for i in range(0, len(list1)):
        list2.append(random.randrange(0, len(list1)))
    print(list2)
    # for i in range(10):
    #     list1.append(random.randint(1, 20))
    # print("对列表进行排序：")
    # print(list1)
    # sort_tool.buubble(list1)
    # sort_tool.select(list1)
    # sort_tool.insert(list1)
    # sort_tool.quick(list1, 0, 9)
    # sort_tool.merge(list1, 0, 9)
    sort_tool.count_sort(list2)
    # print(list1)
    print(list2)
