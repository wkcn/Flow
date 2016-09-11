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

e1 = GetEdge(n1, n3, length = 500, c = 1800, t = 28.6)
e3 = GetEdge(n3, n4, length = 500, c = 1800, t = 28.6)


e6 = GetEdge(n3, n8, length = 500, c = 1800, t = 28.6)
e7 = GetEdge(n3, n7, length = 500, c = 1800, t = 28.6)

Flow.endpoints = [n1, n4, n7, n8]

Q1 = Flow(1800, n1) 
Q2 = Flow(1800, n4) 
Q3 = Flow(1800, n7) 
Q4 = Flow(1800, n8) 

Qs = [Q1, Q2, Q3, Q4]
Es = [e1, e3, e6, e7]
Ns = [n1, n3, n4, n7, n8]
