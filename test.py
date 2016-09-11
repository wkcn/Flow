#coding=utf-8
from Node import *
from Edge import *
from Flow import *

n1 = Node(0 , 0) 
n2 = Node(100 , 0) 
n3 = Node(200 , 0) 
n4 = Node(300 , 0) 
n5 = Node(300 , 0) 
n6 = Node(300 , 0) 
n7 = Node(300 , 0) 

e1 = GetEdge(n1, n2, length = 500, C = 2000, t = 2)
e2 = GetEdge(n2, n3, length = 500, C = 1000, t = 2)
e3 = GetEdge(n3, n4, length = 500, C = 1000, t = 2)
e4 = GetEdgeSingle(n2, n5, length = 500, C = 2000, t = 3)
e5 = GetEdge(n3, n6, length = 500, C = 1000, t = 2)
e6 = GetEdge(n3, n5, length = 500, C = 1000, t = 2)
e7 = GetEdge(n5, n7, length = 500, C = 2000, t = 2)

Flow.endpoints = [n1, n4, n6, n7]
Q1 = Flow(1000, n1)
Q2 = Flow(1000, n4)
Q3 = Flow(1000, n6)
Q4 = Flow(1000, n7)
Qs = [Q1, Q2, Q3, Q4]
n = 1000

for i in range(n):
    for q in Qs:
        q.update(n)

E = [e1, e2, e3, e4, e5, e6, e7]

i = 1
for e in E:
    print(i)
    i += 1
    if type(e) == list:
        print (e[0].Q, e[0].weight, e[1].Q, e[1].weight)
    else:
        print(e.Q, e.weight)
