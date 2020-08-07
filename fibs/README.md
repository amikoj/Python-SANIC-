习惯性的，我们每学习一个编程语言，都喜欢从数学的原理、经典数题开始我们的学习之旅，而斐波拉契数可以说是各中常客了，仿佛是没有写过斐波拉契数列就不算学了某个语言一样。这篇文章难脱俗套，也是一个“斐波拉契数列”与业界传奇**Python**大叔的故事。

![斐波拉契的微笑](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWFnZXMueGlhb3podWFubGFuLmNvbS9waG90by8yMDIwLzBhZTcyODFmYzdmODU1NTRiMmI2NDM4ZmZjNWJlNDY5LmpwZw?x-oss-process=image/format,png)

### 铁打的斐波拉契流水的编程“大叔“[Python]

话说我们今天的女猪脚大美女"**斐波拉契数列**"也是出身名门响当当的人物。斐波拉契数列自从被伟大的数学家昂纳多·斐波拉契(Leonardoda Fibonacc)通过兔子的繁殖提出以来，一直都是最美丽的数列，受到万众追捧。C/C++爱她(FIB数列)、Java/js追捧，php/Python倾慕，也无愧于它黄金数列之称。那么，斐波拉契数列究竟有啥神秘的呢？

#### 斐波拉契数列
斐波拉契数列值得是一组如下循环的数列:

```shell
1、1、2、3、5、8、13、21、34、……
```
一般在数学中我们可以这样对其进行表达：

```shell
F[1]=1，
F(2)=1,
F(n)=F(n - 1)+F(n - 2)（n ≥ 3，n ∈ N*）

```
很简单的一组数列，但却很诱人，因为专家发现，当数列无穷大的时候，斐波拉契数列的前后两个数之比无限接近与黄金分割比例：约为0.618。赞美的话我就不多说了，我们的大自然、生活无处不包裹在斐波拉契的美艳之中。

那么接下来我们就得看看Python大叔如何来描述**斐波拉契**的美艳不可方物。


### 谦卑的Python

python大叔也是心诚，想着多头并进，换着法子来描述、赞美斐波拉契。这一想起心爱的人啊，就爱如泉涌，这不，Python大叔一不留神就想出来了四种方式来表白斐波拉契。

####  递归方式
递归的方式也是较为常用的方式，通过逐层递进的方式来生成斐波拉契数列：

```python
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

```
### 生成器
这种方式使用到了python的高级特性，可以说诚意满满：
```python
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

```
####  魔法方式实现
这种方式更加突出了python 面向对象的思想,同时也突出了python魔法方法的便利性：
```python
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

```
### 矩阵实现
这种方式可以说性能有较高的提高：
```python
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

```

### 来自Python大叔的自白
Python大叔这一溜串儿操作，心中不禁自得。想着，想我这么优秀的人还哪儿能找到。那么问题来了，Python大叔哪儿优秀了？就这次告白来说我们可以看到Python大叔显而易见的几个亮点：

- 极强的语言表现力
这明显的在代码量上可以完美的得到表达
- 超高的内功修养
生成器和魔法方法强炸天有咩有~
- 无法可说的自来熟
和谁都能混的熟(numpy),它不需要对多高的实际功底就可以通过强大的自来熟特性让别人把它的伙计干好。


### 代码实现
本栏目的所有实现代码均可通过Github或码云获取,项目地址:

- [Github-Python Sanic编程之道](https://github.com/amikoj/Python-SANIC-)
- [码云-Python Sanic编程之道](https://gitee.com/amiko/python_sanic_programming)


### 写在后面的话
看到这么拼命努力的Python大叔，你还有理由不喜欢它吗？那么问题来了，这么可爱的Python大叔，你还要等到什么时候才来重新它？欢迎大家来订阅，你的支持，就是我创作最大的动力！


