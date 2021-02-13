# -*- coding:utf-8 -*-
# author:yueba
"""
思路：从第二个数的位置开始，往前最比较，如果小于前面的数，就换一个位置，
这就是一次插排，完成后，从第三个数位置往前作比较，依此类推
"""
a = [58, 36, 17, 49, 82, 3, 39]


def insertion_Sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:                 # 内层循环比较
            arr[j + 1], arr[j] = arr[j], a[j + 1]      # 如果后面的小于前面的，两个数交换位置
            j -= 1                                     # 然后往前进一位，继续重复比较，知道j等于第一个为止 
    return arr

