import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QLabel, QApplication, QFrame




class InterfaceGraphique(QFrame):
    DEFAULT_BORDURE = True

    # DEFAULT_BORDURE peut être utilisé dans __init__
    def __init__(self,bordure : bool = DEFAULT_BORDURE):
        super().__init__()
        if bordure :
            self.setFrameStyle(QFrame.Panel | QFrame.Plain)
            self.setLineWidth(5)

if __name__ == '__main__':
    pass

