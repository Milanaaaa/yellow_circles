import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication
from UI import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.diam = 10
        self.pb.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_face(qp)
            qp.end()

    def draw_face(self, qp):
        for i in range(random.randint(2, 15)):
            pen = QPen(Qt.yellow)
            pen.setColor(QColor(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))
            qp.setPen(pen)
            diam = random.randint(20, 50)
            qp.drawEllipse(random.randint(20, 620), random.randint(20, 520), diam, diam)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
