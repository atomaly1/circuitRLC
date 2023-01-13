import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QLabel

class InterfaceGraphique(QWidget):
    def __init__(self):
        super().__init__()

        # Création de texte à l'intérieur de l'interface graphique : "Interface graphique en WIP..."
        self.label = QLabel("Interface graphique en WIP...", self)

if __name__ == '__main__':
    pass