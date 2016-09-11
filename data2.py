#coding=utf-8
from Node import *
from Edge import *
from Flow import *

ox = 30
oy = 100
ratio = 1.5
n1 = Node(ox, oy) 
n2 = Node(100 * ratio + ox, oy) 
n3 = Node(200 * ratio + ox, oy) 
n4 = Node(300 * ratio + ox, oy) 

n3.redgreen = True

n5 = Node(100 * ratio + ox, 30 * ratio + oy) 
n6 = Node(200 * ratio + ox, 30 * ratio + oy)

n7 = Node(200 * ratio + ox, oy - 30 * ratio) 
n8 = Node(200 * ratio + ox, oy + 60 * ratio) 
n8.oy = 30

e1 = GetEdge(n1, n2, length = 500, c = 1800, t = 28.6)
e2 = GetEdge(n2, n3, length = 500, c = 1800, t = 28.6)
e3 = GetEdge(n3, n4, length = 500, c = 1800, t = 28.6)

e4 = GetEdgeSingle(n5, n6, length = 500, c = 678, t = 72.0)
e4[0].ita = 0.8

e5 = GetEmptyEdge(n2, n5)

e6 = GetEdge(n3, n6, length = 500, c = 1800, t = 28.6)
e7 = GetEdge(n3, n7, length = 500, c = 1800, t = 28.6)
e8 = GetEdge(n6, n8, length = 500, c = 1800, t = 28.6)

Flow.endpoints = [n1, n4, n7, n8]

Q1 = Flow(1800, n1) 
Q2 = Flow(1800, n4) 
Q3 = Flow(1800, n7) 
Q4 = Flow(1800, n8) 

Qs = [Q1, Q2, Q3, Q4]
Es = [e1, e2, e3, e4, e5, e6, e7, e8]
Ns = [n1, n2, n3, n4, n5, n6, n7, n8]
