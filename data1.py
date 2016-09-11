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


n5 = Node(100 * ratio + ox, 30 * ratio + oy) 
n6 = Node(200 * ratio + ox, 30 * ratio + oy)


e1 = GetEdgeSingle(n1, n2, length = 500, C = 1000, t = 2)
e2 = GetEdgeSingle(n2, n3, length = 500, C = 1000, t = 2)
e3 = GetEdgeSingle(n3, n4, length = 500, C = 1000, t = 2)

e4 = GetEdgeSingle(n5, n6, length = 600, C = 900, t = 3)

e5 = GetEmptyEdge(n2, n5)
e6 = GetEmptyEdge(n3, n6)

Flow.endpoints = [n4]

Q1 = Flow(1000, n1) 
Q2 = Flow(0, n4) 

Qs = [Q1, Q2]
Es = [e1, e2, e3, e4, e5, e6]
Ns = [n1, n2, n3, n4, n5, n6]
