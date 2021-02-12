# -*- coding:utf-8 -*-
# author:yueba
"""
选择排序实现
1.min_pos 和 实际最小值下标对换
2.第i个数和最小数兑换位置
"""
import numpy as np
import time


def select_sort(lis: list):
    for i in range(len(lis)):
        min_pos = i
        for j in range(i, len(lis)):
            if lis[j] < lis[min_pos]:
                min_pos = j
        lis[i], lis[min_pos] = lis[min_pos], lis[i]
    return lis


def random_array(i: int):
    array = np.arange(i)
    np.random.shuffle(array)
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
    array01 = select_sort(array)
    array02 = sorted(array_copy)
    if len(array01) == len(array02):
        for i in range(len(array01)):
            if array01[i] != array02[i]:
                raise Exception("ERROR,array01[%d]=%s,array02[%d]=%s,不相等，算法错误")
    print("Oh~Yeah，没毛病！！！")


if __name__ == '__main__':
    check(random_array(100000))
