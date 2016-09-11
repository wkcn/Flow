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
n3 = AddNode(0, 0)
n4 = AddNode(2, 0)
n7 = AddNode(0, -2)
n8 = AddNode(0, 2)
n8.oy = 30

n3.redgreen = True

e1 = GetEdge(n1, n3, length = 1000, c = 1650, t = 36.0)
e3 = GetEdge(n3, n4, length = 1000, c = 1650, t = 36.0)


e6 = GetEdge(n3, n8, length = 1000, c = 1650, t = 36.0)
e7 = GetEdge(n3, n7, length = 1000, c = 1650, t = 36.0)

Flow.endpoints = [n1, n4, n7, n8]

Q1 = Flow(1800, n1) 
Q2 = Flow(1800, n4) 
Q3 = Flow(1800, n7) 
Q4 = Flow(1800, n8) 

Qs = [Q1, Q2, Q3, Q4]
Es = [e1, e3, e6, e7]
Ns = [n1, n3, n4, n7, n8]
