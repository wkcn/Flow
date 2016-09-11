#coding=utf-8
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Node import *
from Edge import *
from Flow import *
from threading import *

from data1 import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(500, 500)
        self.setWindowTitle("Flow")
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
        ox = 30
        oy = 400
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
        self.buttonEnd.move(ox + 320, oy + 30)
        self.buttonEnd.setText("Finish Sim")
        QObject.connect(self.button, SIGNAL("clicked()"),self.RestartSim) 
        QObject.connect(self.buttonEnd, SIGNAL("clicked()"),self.FinishSim) 


    def on_timer(self):
        if self.iterNum < self.needIterNum:
            for q in Qs:
                q.update(self.needIterNum)
            self.iterNum += 1
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

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.black, 3 , Qt.SolidLine)
        qp.setPen(pen)
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
                    text = str(c) + " %d" % e.Q 
                    qp.drawText(x - 10, y - 2 + u * 18, text)
                    u += 1
        qp.end()

if __name__ == "__main__":
    import sys  
    app = QApplication(sys.argv)  

    mainwindow = MainWindow()  
    mainwindow.show()  
    sys.exit(app.exec_())  
