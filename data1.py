#coding=utf-8
from Node import *
from Edge import *
from Flow import *

n1 = Node(0 , 0) 
n2 = Node(100 , 0) 
n3 = Node(200 , 0) 
n4 = Node(300 , 0) 

e1 = GetEdgeSingle(n1, n2, length = 500, C = 1000, t = 2)
e2 = GetEdgeSingle(n2, n3, length = 500, C = 1000, t = 2)
e3 = GetEdgeSingle(n3, n4, length = 500, C = 1000, t = 2)
e4 = GetEdgeSingle(n2, n3, length = 600, C = 900, t = 3)

Flow.endpoints = [n4]
Q1 = Flow(1000, n1) 

Qs = [Q1]
n = 1000
for i in range(n):
    for q in Qs:
        q.update(n)

E = [e1, e2, e3, e4]

for e in E:
    print e.Q, e.weight
