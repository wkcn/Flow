#coding=utf-8
from Node import *
from Edge import *
from Flow import *

ox = 200
oy = 200
ratio = 70

def AddNode(x, y):
    nd = Node(ox + x * ratio, oy + y * ratio)
    return nd

n1 = AddNode(-1, -1)
n3 = AddNode(1, -1)

n5 = AddNode(1, 1)
n7 = AddNode(-1, 1)

n10 = AddNode(-2, -1)
n11 = AddNode(2, -1)
n12 = AddNode(2, 1)
n13 = AddNode(-2, 1)

n11.ox = 20
n12.ox = 20

n1.redgreen = True
n3.redgreen = True
n5.redgreen = True
n7.redgreen = True

Ns = [n1,n3,n5,n7,n10,n11,n12, n13]


e1 = GetEdge(n1, n3, length = 500, c = 1650, t = 36.0)

e3 = GetEdge(n3, n5, length = 500, c = 1650, t = 36.0)

e4 = GetEdge(n5, n7, length = 500, c = 1650, t = 36.0)

e6 = GetEdge(n7, n1, length = 500, c = 1650, t = 36.0)

'''
e8 = GetEdge(n10, n1, length = 500, c = 1650, t = 36.0)
e9 = GetEdge(n3, n11, length = 500, c = 1650, t = 36.0)
'''
e10 = GetEdge(n5, n12, length = 500, c = 1650, t = 36.0)
e11 = GetEdge(n7, n13, length = 500, c = 1650, t = 36.0)

e8 = GetEmptyEdge(n10, n1)
e9 = GetEmptyEdge(n3, n11)
#e10 = GetEmptyEdge(n5, n12)
#e11 = GetEmptyEdge(n7, n13)

Es = [e1,e3,e4,e6,e8,e9,e10,e11]

Flow.endpoints = [n10,n12,n13]
Qs = []
for p in Flow.endpoints:
    Qs.append(Flow(1000, p))
