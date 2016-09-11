#coding=utf-8
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import viewer

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(250, 400)
        self.setWindowTitle("Flow")
        self.listWidget = QListWidget(self)
        self.listWidget.resize(250, 400)
        for i in range(len(viewer.datas)):
            self.listWidget.addItem("Model %d" % (i + 1))
        self.win = None
        QObject.connect(self.listWidget, SIGNAL("currentRowChanged (int)"), self.selectMode)

    def selectMode(self):
        i = self.listWidget.currentRow()
        if i != -1:
            self.win = viewer.MainWindow(i)
            self.win.show()


if __name__ == "__main__":
    import sys  
    app = QApplication(sys.argv)  
    mainwindow = MainWindow()  
    mainwindow.show()  
    sys.exit(app.exec_())  
