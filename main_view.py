import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidgetAction

class MainView(QMainWindow):

    def __init__(self):
        super().__init__() # Appel du constructeur parent
        self.setWindowTitle("CircuitRLC") # Titre de la fenêtre
        self.setWindowIcon(QIcon("icons/rlc_project_v4.ico")) 
        self.resize(400, 300)

if __name__ == '__main__':
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # TODO : Instancier et afficher votre fenêtre graphique.
    main_view = MainView()
    main_view.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())