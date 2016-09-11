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
n2 = AddNode(1, -1)
n3 = AddNode(1, 1)
n4 = AddNode(-1, 1)

n5 = AddNode(-1, -2)
n6 = AddNode(1, -2)

n7 = AddNode(2, -1)
n8 = AddNode(2, 1)

n9 = AddNode(1, 2)
n10 = AddNode(-1, 2)

n11 = AddNode(-2, 1)
n12 = AddNode(-2, -1)

Ns = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12]


e1 = GetEdge(n1, n2, length = 500, C = 900, t = 3)
e2 = GetEdge(n2, n3, length = 500, C = 900, t = 3)
e3 = GetEdge(n3, n4, length = 500, C = 900, t = 3)
e4 = GetEdge(n4, n1, length = 500, C = 900, t = 3)

e5 = GetEdge(n1, n5, length = 500, C = 1000, t = 2)
e6 = GetEdge(n2, n6, length = 500, C = 1000, t = 2)
e7 = GetEdge(n2, n7, length = 500, C = 1000, t = 2)
e8 = GetEdge(n3, n8, length = 500, C = 1000, t = 2)
e9 = GetEdge(n3, n9, length = 500, C = 1000, t = 2)
e10 = GetEdge(n4, n10, length = 500, C = 1000, t = 2)
e11 = GetEdge(n4, n11, length = 500, C = 1000, t = 2)
e12 = GetEdge(n1, n12, length = 500, C = 1000, t = 2)
Es = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12]

Flow.endpoints = [n5,n6,n7,n8,n9,n10,n11,n12]
Qs = []
for p in Flow.endpoints:
    Qs.append(Flow(1000, p))
