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


    def on_timer(self):
        if self.iterNum < self.needIterNum:
            for q in Qs:
                q.update(self.needIterNum)
            self.iterNum += 1
        self.update()

    def RestartSim():
        for es in Es:
            for e in es:
                e.Q = 0

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

        pen = QPen(Qt.red, 6 , Qt.SolidLine)
        qp.setPen(pen)
        for es in Es:
            for e in es:
                if e.weight:
                    j1, j2 = e.joints
                    x = (j1.x + j2.x) / 2
                    y = (j1.y + j2.y) / 2
                    qp.drawText(x, y - 2, str(e.Q))
        qp.end()

if __name__ == "__main__":
    import sys  
    app = QApplication(sys.argv)  

    mainwindow = MainWindow()  
    mainwindow.show()  
    sys.exit(app.exec_())  
