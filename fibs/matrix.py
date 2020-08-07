#!/usr/bin/env pyhon
# -*- coding:utf-8 -*-
import numpy

def matrix(n):
    Matrix = numpy.matrix("1 1;1 0")
    return pow(Matrix, n)

def fbis(n):
    """使用numpy库实现斐波拉契数列
    """
    result_list = []
    for i in range(0, n):
        result_list.append(numpy.array(matrix(i))[0][0])
    return result_list

if __name__ == "__main__":
    i=0
    for n in fbis(10):
        print("第%d个数是:%d" % (i, n))
        i+=1
