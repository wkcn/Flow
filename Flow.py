#coding=utf-8
from Queue import *
from copy import *

class Flow:
    endpoints = []
    def __init__(self, value, startPoint):
        self.startPoint = startPoint
        self.targets = self.GetTargets()
        self.SetValue(value)
    def SetValue(self, value):
        self.value = value * 1.0
        self.toValue = [self.value / len(self.targets) for _ in range(len(self.targets))] # 默认均分
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
        for i in range(len(self.targets)):
            t = self.targets[i]
            y = self.toValue[i] * 1.0 / n
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
                                ndis = dis + e.GetWeight(w.redgreen)
                                npo = w
                                nelst = copy(elst)
                                nelst.append(e)
                                q.put((ndis, npo, nelst))

    def PrintResult(self, Qs):
        sid = 0
        for u in Qs:
            if u == self:
                break
            sid += 1
        for i in range(len(self.targets)):
            t = self.targets[i]
            #startPoint -> t
            q = PriorityQueue()
            vis = []
            q.put((0, self.startPoint))
            while not q.empty():
                dis, po = q.get()
                if po == t:
                    tid = 0
                    for u in Qs:
                        if u.startPoint == t:
                            break
                        tid += 1
                    print ("from Q%d to Q%d = %.2f" % (sid,tid,dis))
                for w in po.neighbors:
                    for e in po.edges:
                        if e.joints[0] == po and e.joints[1] == w:
                            if e and e not in vis:
                                vis.append(e)
                                ndis = dis + e.GetWeight(w.redgreen)
                                npo = w
                                q.put((ndis, npo))

