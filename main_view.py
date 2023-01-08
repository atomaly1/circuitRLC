import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QHBoxLayout, QVBoxLayout

class MainWindow(QMainWindow):
   
    def __init__(self):
        super().__init__() # Appel du constructeur parent
        self.setWindowTitle("CircuitRLC") # Titre de la fenêtre
        self.setWindowIcon(QIcon("icons/rlc_project_v2.ico")) 
        self.resize(400, 300)
        
        main_view = MainView()
        self.setCentralWidget(main_view)

class MainView(QWidget):

    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QPushButton('Sauvegarder/nouveau etc'), 0, 0, 1, 2)  #Remplacer par un layout
        grid.addWidget(QPushButton('Ajouter élements'), 1, 0, 1, 1)         #Remplacer par un layout
        grid.addWidget(QLabel('Coordonnées'), 2, 0, 1, 1)                   #Remplacer par un layout
        grid.addWidget(QLabel('Interface graphique'), 1, 1, 2, 1)           #Remplacer par un layout
        grid.addWidget(QLabel('Logs/Results'), 3, 0, 1, 2)                  #Remplacer par un layout

class Entete(QWidget):
    
    layout = QHBoxLayout()
    #TODO Bouton Nouveau
    #TODO Bouton Ouvrir
    #TODO Bouton Sauvegarder
    #TODO Bouton Calculs
    pass

class MenuComposants(QWidget):

    layout = QVBoxLayout()
    #TODO Ajouter les boutons pour chaque composant
    #TODO Réticule (dans cette box ?)
    pass

#TODO Un pop up par composant (QPopUpWidget à chercher si existant)

#TODO A droite, affichage du circuit : Affichage (Fenêtre graphique ?)
    #TODO Design de chaque composant
    #TODO Placement automatique à partir des noeuds

class Logs(QWidget):

    layout = QVBoxLayout()
    #TODO Fenetre Logs
    pass

#TODO Fenêtre Calculs

if __name__ == '__main__':
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # TODO : Instancier et afficher votre fenêtre graphique.
    main_window = MainWindow()
    main_window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())