#coding=utf-8
from Node import *
from Edge import *
from Flow import *

ox = 200
oy = 220
ratio = 90

def AddNode(x, y):
    nd = Node(ox + x * ratio, oy + y * ratio)
    return nd

n1 = AddNode(-2, 0)
n2 = AddNode(-1.9, 0)
n3 = AddNode(0, 0)
n4 = AddNode(2, 0)
n5 = AddNode(-1.9, 1.9)
n6 = AddNode(0, 1.9)
n7 = AddNode(0, -2)
n8 = AddNode(0, 2)
n8.oy = 30

n3.redgreen = True

#e1 = GetEdge(n1, n2, length = 1000, c = 1650, t = 36.0)
e1 = GetEmptyEdge(n1, n2)

e2 = GetEdge(n2, n3, length = 1000, c = 1650, t = 36.0)
e3 = GetEdge(n3, n4, length = 1000, c = 1650, t = 36.0)

#e4 = GetEdgeSingle(n5, n6, length = 1000, c = 678, t = 43.2)
e4 = GetEdgeSingle(n5, n6, length = 500, c = 700, t = 96.0)
e4[0].ita = 0.8

e5 = GetEmptyEdge(n2, n5)

e6 = GetEdge(n3, n6, length = 1000, c = 1650, t = 36.0)
e7 = GetEdge(n3, n7, length = 1000, c = 1650, t = 36.0)
#e8 = GetEdge(n6, n8, length = 1000, c = 1650, t = 36.0)
e8 = GetEmptyEdge(n6, n8)

Flow.endpoints = [n1, n4, n7, n8]

Q1 = Flow(1800, n1) 
Q2 = Flow(1800, n4) 
Q3 = Flow(1800, n7) 
Q4 = Flow(1800, n8) 

Qs = [Q1, Q2, Q3, Q4]
Es = [e1, e2, e3, e4, e5, e6, e7, e8]
Ns = [n1, n2, n3, n4, n5, n6, n7, n8]
