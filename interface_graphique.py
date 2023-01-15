import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QBrush, QPen, QFont
from PySide6.QtWidgets import QWidget, QLabel, QApplication, QFrame, QGraphicsScene, QGraphicsView, QGraphicsItem




class FrameWithBorder(QFrame):
    DEFAULT_BORDURE = True

    def __init__(self):
        super().__init__()

    # DEFAULT_BORDURE peut être utilisé dans __init__
    def __init__(self,bordure : bool = DEFAULT_BORDURE):
        super().__init__()
        if bordure :
            self.setFrameStyle(QFrame.Panel | QFrame.Plain)
            self.setLineWidth(5)

            

class InterfaceGraphique(FrameWithBorder):

    def __init__(self):
        super().__init__()

        self.create_ui()
        self.show()


    def enterEvent(self, event):
        self.setCursor(Qt.CrossCursor)
    def mouseMoveEvent(self, event):
        self.update_points()
        self.points.append(event.pos())
        pos = event.pos()
        self.parent().statusBar().showMessage("x: {}, y: {}".format(pos.x(), pos.y()))
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.points.append(event.pos())

    def create_ui(self):

        scene = QGraphicsScene(self)
 
        # Définition des pinceaux 
        blackPen = QPen(Qt.black)
        blackPen.setWidth(2)

        def create_resistance(self, px, py, name):
            self.rect = scene.addRect(px, py, 40,20, blackPen)
            self.rect.setFlag(QGraphicsItem.ItemIsMovable)

        def create_noeud(self, px, py, name):
            self.ellipse = scene.addEllipse(px, py, 5, 5, blackPen)
            self.ellipse.setFlag(QGraphicsItem.ItemIsMovable)
        

        def create_text():
            scene.addText("This is the greatest text, ever - Donald J. Trump", QFont("Sanserif", 15))
        

        self.view = QGraphicsView(scene, self)
        self.view.setGeometry(0,0, 1000, 900)


if __name__ == '__main__':
    pass

