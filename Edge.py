#coding=utf-8
class Edge:
    def __init__(self,length, j1, j2, C, t):
        self.length = length
        self.joints = [j1, j2]#j1 -> j2
        self.C = C * 1.0
        self.t = t * 1.0
        self.Q = .0
    @property
    def weight(self):
        return self.t * (1 + self.Q / self.C)


#n1 -> n2
def GetEdgeSingle(n1, n2, length, C, t):
    e = Edge(length * 1.0, n1, n2, C * 1.0, t * 1.0)
    n1.edges.append(e)
    if n2 not in n1.neighbors:
        n1.neighbors.append(n2)
    #n2.edges.append(e)
    #if n1 not in n2.neighbors:
    #    n2.neighbors.append(n1)
    return e

def GetEdge(n1, n2, length, C, t):
    e1 = GetEdgeSingle(n1, n2, length, C, t)
    e2 = GetEdgeSingle(n2, n1, length, C, t)
    return [e1, e2]

