#coding=utf-8
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ox = 0
        self.oy = 0
        self.edges = []
        self.neighbors = []
        self.redgreen = False
