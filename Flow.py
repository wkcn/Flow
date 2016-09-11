#coding=utf-8
from Queue import *
from copy import *

class Flow:
    endpoints = []
    def __init__(self, value, startPoint):
        self.value = value * 1.0
        self.startPoint = startPoint
        self.targets = self.GetTargets()
    def GetTargets(self):
        res = []
        vis = [self.startPoint]
        q  = Queue()
        q.put(self.startPoint)
        while not q.empty():
            p = q.get()
            if p in Flow.endpoints and p != self.startPoint:
                res.append(p)
            for w in p.neighbors:
                if w not in vis:
                    q.put(w)
                    vis.append(w)
        return res
    def update(self, n):
        y = self.value * 1.0 / n
        y /= len(self.targets)
        for t in self.targets:
            #startPoint -> t
            q = PriorityQueue()
            vis = []
            q.put((0, self.startPoint, []))
            while not q.empty():
                dis, po, elst = q.get()
                if po == t:
                    for e in elst:
                        e.Q += y
                    break
                for w in po.neighbors:
                    for e in po.edges:
                        if e.joints[0] == po and e.joints[1] == w:
                            if e and e not in vis:
                                vis.append(e)
                                ndis = dis + e.weight
                                npo = w
                                nelst = copy(elst)
                                nelst.append(e)
                                q.put((ndis, npo, nelst))
