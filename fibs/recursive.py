#!/usr/bin/env python 
# -*- coding:utf-8 -*-

def fbis(num):
    '''递归法实现斐波拉契数列
    '''
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

if __name__ == "__main__":
    result=fbis(10)
    for i,n in enumerate(result):
        print("第%d个数是:%d"%(i,n))
