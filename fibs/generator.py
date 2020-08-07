#!/usr/bin/env pyhon
# -*- coding:utf-8 -*-

def fbis(n):
    """
    通过yield生成器实现斐波拉契数列
    """
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
        yield a


if __name__ == "__main__":
    i=0
    for n in fbis(10):
        print("第%d个数是:%d" % (i, n))
        i+=1
