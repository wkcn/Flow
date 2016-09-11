#coding=utf-8
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Node import *
from Edge import *
from Flow import *
from threading import *

import data1
import data2
import data3

datas = [data1, data2, data3]

Qs = data1.Qs
Es = data1.Es 
Ns = data1.Ns
class MainWindow(QMainWindow):
    def __init__(self, i):
        super(MainWindow, self).__init__()
        self.resize(800, 500)
        self.setWindowTitle("Flow")
        self.Qviewed = True
        global Qs, Es, Ns
        Qs = datas[i].Qs
        Es = datas[i].Es
        Ns = datas[i].Ns

        self.timer = QTimer()
        QObject.connect(self.timer,SIGNAL("timeout()"), self.on_timer)
        self.iterNum = 0
        self.needIterNum = 1000;

        self.labels = [QLabel(self) for _ in range(len(Qs) * 2)]
        ox = 550
        oy = 50
        u = 40
        aIntValidator = QIntValidator()
        aIntValidator.setRange(0, 99999)
        self.editBoxs = [[None for _ in range(len(Qs))] for _ in range(len(Qs))]
        for r in range(len(Qs)):
            for c in range(len(Qs)):
                qe = QLineEdit(self)
                qe.resize(u,u)
                qe.move(ox + u * c, oy + u * r)
                qe.setValidator(aIntValidator)
                value = 0.0
                #r->c
                targets = Qs[r].targets 
                for i in range(len(targets)):
                    if targets[i] == Qs[c].startPoint:
                        value = Qs[r].toValue[i]
                        break

                qe.setText("%d" % value)
                self.editBoxs[r][c] = qe

        self.button = QPushButton(self)
        self.buttonEnd = QPushButton(self)
        self.buttonQViewed = QCheckBox(self)

        self.button.move(ox, oy + len(Qs) * u + 30)
        self.button.setText("RestartSim")

        for i in range(len(Qs)):
            self.labels[i*2].move(ox + u * i + 5, oy - 33)
            self.labels[i*2+1].move(ox - 20, oy + u * i)
            self.labels[i*2].setText("Q%d" % i)
            self.labels[i*2+1].setText("Q%d" % i)
        ox = 30
        oy = 400
        self.buttonQViewed.move(ox + 520, oy + 60)
        self.buttonQViewed.setText("View Time")
        self.buttonEnd.move(ox + 520, oy + 30)
        self.buttonEnd.setText("Finish Sim")
        QObject.connect(self.button, SIGNAL("clicked()"),self.RestartSim) 
        QObject.connect(self.buttonEnd, SIGNAL("clicked()"),self.FinishSim) 
        self.RestartSim()
        fps = 60
        self.timer.start(1000 / fps)


    def on_timer(self):
        if self.iterNum < self.needIterNum:
            for q in Qs:
                q.update(self.needIterNum)
            self.iterNum += 1
        self.Qviewed = (self.buttonQViewed.checkState() == 0)
        self.update()

    def RestartSim(self):

        for r in range(len(Qs)):
            for c in range(len(Qs)):
                value = int(self.editBoxs[r][c].text())
                targets = Qs[r].targets
                for i in range(len(targets)):
                    if targets[i] == Qs[c].startPoint:
                        Qs[r].toValue[i] = value
                        break

        for es in Es:
            for e in es:
                e.Q = 0
        self.iterNum = 0

    def FinishSim(self):
        while self.iterNum < self.needIterNum:
            for q in Qs:
                q.update(self.needIterNum)
            self.iterNum += 1
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.black, 3 , Qt.SolidLine)
        qp.setPen(pen)
        qp.drawText(10, 30, "Iter: %d / %d" % (self.iterNum, self.needIterNum))
        for es in Es:
            for e in es:
                j1, j2 = e.joints
                qp.drawLine(j1.x, j1.y, j2.x, j2.y)

        pen = QPen(Qt.blue, 6 , Qt.SolidLine)
        qp.setPen(pen)
        for node in Ns:
            qp.drawPoint(node.x, node.y)

        pen = QPen(Qt.black, 6 , Qt.SolidLine)
        qp.setPen(pen)
        for i in range(len(Qs)):
            f = Qs[i]
            p = f.startPoint
            qp.drawText(p.x - 8, p.y - 8, "Q%d" % i)

        for es in Es:
            u = 0
            for e in es:
                if e.weight:
                    j1, j2 = e.joints
                    x = (j1.x + j2.x) / 2
                    y = (j1.y + j2.y) / 2
                    c = ''
                    color = Qt.red
                    if j1.x < j2.x:
                        c = '->'
                    elif j1.x > j2.x:
                        c = '<-'
                        color = Qt.blue
                    elif j1.y < j2.y:
                        c = 'v'
                        x += 13
                        color = Qt.blue
                    else:
                        c = '^'
                        x += 13
                    pen = QPen(color, 6 , Qt.SolidLine)
                    qp.setPen(pen)
                    if self.Qviewed:
                        text = str(c) + " %d" % e.Q 
                    else:
                        text = str(c) + " %.2f" % e.weight
                    qp.drawText(x - 30, y - 2 + u * 18, text)
                    u += 1
        qp.end()

