# -*- coding:utf-8 -*-
# author:yueba
import numpy as np
import time

def random_array(i: int):
    array = np.arange(i)
    np.random.shuffle(array)
    return array


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

# 装饰器计算功能运行时间
def cal_time(fn):
    def wrapper(args):
        start = time.time()
        fn(args)
        end = time.time()
        spend = end - start
        print(spend)

    return wrapper


# 对数器实现
@cal_time
def check(array):
    array_copy = array.copy()
    array01 = bubble_sort(array)
    array02 = sorted(array_copy)
    if len(array01) == len(array02):
        for i in range(len(array01)):
            if array01[i] != array02[i]:
                raise Exception("ERROR,array01[%d]=%s,array02[%d]=%s,不相等，算法错误")
    print("Oh~Yeah，没毛病！！！")


if __name__ == '__main__':
    check(random_array(1000))
