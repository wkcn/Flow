#coding=utf-8
from math import *
class Edge:
    g = 42.0
    C = 70.0
    T = 15 / 60.0
    K = 1.0
    I = 1.0
    def __init__(self,length, j1, j2, c, t):
        self.length = length * 1.0
        self.joints = [j1, j2]#j1 -> j2
        self.c = c * 1.0
        self.t = t * 1.0 # t值 = self.length / 自由速度(没有其他车辆阻碍时的速度), 这里的t值已经预先计算出来
        self.Q = .0
        self.emp = False
        self.ita = 1.0
    def GetWeight(self, redgreen):
        beta = 2.076 + 2.87 * (self.Q / (self.ita * self.c) ** 3)
        t1 = self.t * (1 + self.Q / ((self.ita * self.c) ** beta))
        d1 = (0.5 * self.C * (1.0 - self.g / self.C) ** 2) / (1.0 - min(1.0, self.Q / self.c) * self.g / self.C)
        d2 = 900.0 * self.T * (self.Q / self.c - 1 + sqrt((self.Q/self.c - 1) ** 2 + 8 * self.K * self.I * (self.Q/self.c) / (self.c * self.T)))
        d3 = 5.0
        if redgreen:
            t1 += d1 + d2 + d3
        else:
            t1 += d2 + d3
        return t1

class EmptyEdge:
    def __init__(self, j1, j2):
        self.joints = [j1, j2]#j1 -> j2
        self.Q = .0
        self.emp = True
    def GetWeight(self, redgreen):
        return .0


#n1 -> n2
def GetEdgeSingle(n1, n2, length, c, t):
    e = Edge(length * 1.0, n1, n2, c * 1.0, t * 1.0)
    n1.edges.append(e)
    if n2 not in n1.neighbors:
        n1.neighbors.append(n2)
    #n2.edges.append(e)
    #if n1 not in n2.neighbors:
    #    n2.neighbors.append(n1)
    return [e]

def GetEdge(n1, n2, length, c, t):
    e1 = GetEdgeSingle(n1, n2, length, c, t)
    e2 = GetEdgeSingle(n2, n1, length, c, t)
    return e1 + e2


#n1 -> n2
def GetEmptyEdgeSingle(n1, n2):
    e = EmptyEdge(n1, n2)
    n1.edges.append(e)
    if n2 not in n1.neighbors:
        n1.neighbors.append(n2)
    #n2.edges.append(e)
    #if n1 not in n2.neighbors:
    #    n2.neighbors.append(n1)
    return [e]

def GetEmptyEdge(n1, n2):
    e1 = GetEmptyEdgeSingle(n1, n2)
    e2 = GetEmptyEdgeSingle(n2, n1)
    return e1 + e2

