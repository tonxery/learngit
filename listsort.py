#!/usr/bin/env python
#-*- coding:utf-8 -*-
a = (1,2,3)
b = list(a)#元组转换列表
c = tuple(b)#列表转换元组
d = [('a',123),('b',456)]
e = dict(d)#列表转换字典
l = [10,56,4545,4,50000000,6,7]
def test(a):
    '''
#test doc
        '''
    a.sort()
    return a[-1]
    return a
print test(l)
