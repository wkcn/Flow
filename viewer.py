#coding=utf-8
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Node import *
from Edge import *
from Flow import *
from threading import *

import data1
import data2

datas = [data1, data2]

Qs = data1.Qs
Es = data1.Es 
Ns = data1.Ns
class MainWindow(QMainWindow):
    def __init__(self, i):
        super(MainWindow, self).__init__()
        self.resize(500, 500)
        self.setWindowTitle("Flow")
        self.Qviewed = True
        global Qs, Es, Ns
        Qs = datas[i].Qs
        Es = datas[i].Es
        Ns = datas[i].Ns

        self.timer = QTimer()
        QObject.connect(self.timer,SIGNAL("timeout()"), self.on_timer)
        fps = 60
        self.timer.start(1000 / fps)
        self.iterNum = 0
        self.needIterNum = 1000;

        self.labels = [QLabel(self) for _ in range(len(Qs))]
        self.editBoxs = [QLineEdit(self) for _ in range(len(Qs))]
        self.button = QPushButton(self)
        self.buttonEnd = QPushButton(self)
        self.buttonQViewed = QCheckBox(self)
        ox = 30
        oy = 300
        u = 80
        for i in range(len(Qs)):
            self.editBoxs[i].move(ox + u * i, oy)
            self.editBoxs[i].resize(60, 25)
            self.editBoxs[i].setText("%d" % Qs[i].value)
            aIntValidator = QIntValidator()
            aIntValidator.setRange(0, 99999)
            self.editBoxs[i].setValidator(aIntValidator)
            self.labels[i].move(ox + u * i + 5, oy - 36)
            self.labels[i].setText("Q%d" % i)
        self.button.move(ox, oy + 30)
        self.button.setText("RestartSim")
        self.buttonQViewed.move(ox + 320, oy + 60)
        self.buttonQViewed.setText("View Time")
        self.buttonEnd.move(ox + 320, oy + 30)
        self.buttonEnd.setText("Finish Sim")
        QObject.connect(self.button, SIGNAL("clicked()"),self.RestartSim) 
        QObject.connect(self.buttonEnd, SIGNAL("clicked()"),self.FinishSim) 


    def on_timer(self):
        if self.iterNum < self.needIterNum:
            for q in Qs:
                q.update(self.needIterNum)
            self.iterNum += 1
        self.Qviewed = (self.buttonQViewed.checkState() == 0)
        self.update()

    def RestartSim(self):
        for i in range(len(Qs)):
            Qs[i].value = int(self.editBoxs[i].text()) 
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
                    if j1.x < j2.x:
                        c = '->'
                    elif j1.x > j2.x:
                        c = '<-'
                    elif j1.y < j2.y:
                        c = 'v'
                        x += 13
                    else:
                        c = '^'
                        x += 13
                    if u == 0:
                        pen = QPen(Qt.red, 6 , Qt.SolidLine)
                    else:
                        pen = QPen(Qt.blue, 6 , Qt.SolidLine)
                    qp.setPen(pen)
                    if self.Qviewed:
                        text = str(c) + " %d" % e.Q 
                    else:
                        text = str(c) + " %.2f" % e.weight
                    qp.drawText(x - 10, y - 2 + u * 18, text)
                    u += 1
        qp.end()

