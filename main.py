import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import QPointF

from ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.button_click)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(random.randint(0, 256), random.randint(
                0, 256), random.randint(0, 256)))
            radius = random.randint(10, 100)
            qp.drawEllipse(QPointF(400, 250), radius, radius)

    def button_click(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
