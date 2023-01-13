import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QLabel, QApplication

class InterfaceGraphique(QWidget):
    def __init__(self):
        super().__init__()

        self.points = []
        self.label = QLabel(self)
        self.label.setText("Click to add points")
        self.update_points()
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.points.append(event.pos())
    def enterEvent(self, event):
        self.parent().statusBar().showMessage("Mouse Entered Widget")
        self.setCursor(Qt.CrossCursor)
    def leaveEvent(self, event):
        self.parent().statusBar().clearMessage()
    def mouseMoveEvent(self, event):
        self.update_points()
        pos = event.pos()
        self.parent().statusBar().showMessage("x: {}, y: {}".format(pos.x(), pos.y()))

    def update_points(self):
        text = "<br>".join([str(p) for p in self.points])
        self.label.setText("Click to add points<br>" + text)
        self.label.adjustSize()


if __name__ == '__main__':
    pass