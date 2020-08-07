#!/usr/bin/env pyhon
# -*- coding:utf-8 -*-

class Fbis(object):
    """使用魔法函数实现斐波拉契数列
    """

    def __init__(self, n):
        self.n = n     # 最大数列数
        self.current = 0  # 当前位置的斐波拉契数列值
        self.a = 0  # 初始第一个位置
        self.b = 1  # 初始第二个位置

    def __next__(self):
        """next()函数调用时触发
        """
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        """返回自身
        """
        return self


if __name__ == "__main__":
    i=0
    for n  in Fbis(10):
        print("第%d个数是:%d" % (i, n))
        i+=1
