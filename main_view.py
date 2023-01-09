import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QWidget, QDockWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QTextEdit 

#TODO Ajouter au GSheet
# Fenêtre principale
class MainWindow(QMainWindow): 
   
    def __init__(self):
        super().__init__() # Appel du constructeur parent

        # Design
        self.setWindowTitle('CircuitRLC')                       # Titre
        self.setWindowIcon(QIcon('icons/rlc_project_v2.ico'))   # Icône
        self.resize(800, 600)                                   # Taille de la fenêtre
        self.setMinimumSize(400, 300)                           # Taille min
        self.setMaximumSize(800, 600)                           # Taille MAX
        self.setStyleSheet('background:rgba(255,255,255,127)')  # Couleur du fond (white, black, cyan, red, magenta, green, yellow, blue, gray, lightGray, darkGray... OU Color Picker Online OU rgba(63,195,255,127))

        # Menu Bar
        barre_menu = self.menuBar() # Création de la barre de menu (QmenuBar)   
        menu_fichier = barre_menu.addMenu('Fichier') # Ajout d'un menu déroulant (QMenu)
        menu_edition = barre_menu.addMenu('Edition')
        menu_calculs = barre_menu.addMenu('Calculs')
        menu_aide = barre_menu.addMenu('Aide')

        # Tool Bar
        toolbar = QToolBar('Toolbar')
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(Qt.TopToolBarArea, toolbar)
        #TODO Ajouter boutons

        # Central Widget
        main_view = InterfaceGraphique()
        self.setCentralWidget(main_view)

        # Status Bar
        status_bar = self.statusBar()
        status_bar.showMessage("Application développée par Eliott, Lucie et Emeric - FIP MIK4", 10000)

        # Action nouveau
        action_nouveau = QAction('Nouveau', self)
        menu_fichier.addAction(action_nouveau) # Ajout d'une action au menu
        # Action ouvrir
        action_ouvrir = QAction('Ouvrir', self)
        menu_fichier.addAction(action_ouvrir)
        # -------------------------
        menu_fichier.addSeparator()
        # Action sauvegarder
        action_sauvegarder = QAction('Sauvegarder', self)
        menu_fichier.addAction(action_sauvegarder)
        # -------------------------
        menu_fichier.addSeparator()
        # Action quitter
        action_quitter = QAction('Quitter', self) # Création d'une action (QAction)
        action_quitter.setShortcut('Ctrl+Q') # Ajout d'un raccourci pour réaliser une action
        action_quitter.triggered.connect(self.quitter_app) # Déclenchement de la méthode fermant l'application
        menu_fichier.addAction(action_quitter)

    def quitter_app(self):
        QApplication.quit()

# Vue principale
class InterfaceGraphique(QWidget):

    def __init__(self):
        super().__init__()
        
        #TODO Design de chaque composant
        #TODO Placement automatique à partir des noeuds

        '''
        # TEST A SUPPRIMER
        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(QPushButton("Sauvegarder/nouveau etc"), 0, 0, 1, 2)  #Remplacer par un layout
        grid.addWidget(QPushButton("Ajouter élements"), 1, 0, 1, 1)         #Remplacer par un layout
        grid.addWidget(QLabel("Coordonnées"), 2, 0, 1, 1)                   #Remplacer par un layout
        grid.addWidget(QLabel("Interface graphique"), 1, 1, 2, 1)           #Remplacer par un layout
        grid.addWidget(QLabel("Logs/Results"), 3, 0, 1, 1)                  #Remplacer par un layout
        grid.addWidget(QTextEdit("Laisse libre cours à ton imagination..."), 3, 1, 1, 1)
        '''   

#TODO Fenêtre de logs
class Logs(QDockWidget):
    pass

#TODO Liste des composants
class ListeComposants(QDockWidget):
    pass

#TODO Information pour chaque composant
class InfoComposant(QDockWidget):
    pass

# Divers
#TODO Ajouter les boutons pour chaque composant
#TODO Un pop up par composant (QPopUpWidget à chercher si existant)
#TODO A droite, affichage du circuit : Affichage (Fenêtre graphique ?)
#TODO Fenêtre Calculs
#TODO Réticule (dans cette box ?)

if __name__ == '__main__':
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # TODO : Instancier et afficher votre fenêtre graphique.
    main_window = MainWindow()
    main_window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())