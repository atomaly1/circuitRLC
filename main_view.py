import sys, webbrowser

from PySide6.QtCore import QSize, Qt, Slot
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QWidget, QDockWidget, QListWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QTextEdit 

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

        self.create_dock_windows()
        
        # Action nouveau
        action_nouveau = QAction('Nouveau', self)
        action_nouveau.setShortcut('Ctrl+N')
        # Action ouvrir
        action_ouvrir = QAction('Ouvrir', self)
        action_ouvrir.setShortcut('Ctrl+O')
        # Action sauvegarder
        action_sauvegarder = QAction('Sauvegarder', self)
        action_sauvegarder.setShortcut('Ctrl+S')
        # Action quitter
        action_quitter = QAction('Quitter', self) # Création d'une action (QAction)
        action_quitter.setShortcut('Ctrl+Q') # Ajout d'un raccourci pour réaliser une action
        action_quitter.triggered.connect(self.quitter_app) # Déclenchement de la méthode fermant l'application
        # Action annuler
        action_annuler = QAction('Annuler', self)
        action_annuler.setShortcut('Ctrl+Z')
        # Action refaire
        action_refaire = QAction('Refaire', self)
        action_refaire.setShortcut('Ctrl+Y')
        # Action resoudre
        action_resoudre = QAction('Résoudre', self)
        action_resoudre.setShortcut('Ctrl+R')
        action_resoudre.triggered.connect(self.resoudre)
        # Action aide
        action_aide = QAction('Aide', self)
        action_aide.setShortcut('F1')
        action_aide.triggered.connect(self.aide)
        # Action Github
        action_github = QAction('Github CircuitRLC', self)
        action_github.setShortcut('F2')
        action_github.triggered.connect(self.github)
       
        # Menu Bar
        barre_menu = self.menuBar() # Création de la barre de menu (QmenuBar)   
        
        menu_fichier = barre_menu.addMenu('Fichier') # Ajout d'un menu déroulant (QMenu)
        menu_fichier.addAction(action_nouveau) # Ajout d'une action au menu
        menu_fichier.addAction(action_ouvrir)
        menu_fichier.addSeparator()
        menu_fichier.addAction(action_sauvegarder)
        menu_fichier.addSeparator()
        menu_fichier.addAction(action_quitter)

        menu_edition = barre_menu.addMenu('Edition')
        menu_edition.addAction(action_annuler)
        menu_edition.addAction(action_refaire)

        menu_calculs = barre_menu.addMenu('Calculs')
        menu_calculs.addAction(action_resoudre)

        menu_aide = barre_menu.addMenu('Aide')
        menu_aide.addAction(action_aide)
        menu_aide.addSeparator()
        menu_aide.addAction(action_github)

        # Tool Bar
        toolbar = QToolBar('Toolbar')
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(Qt.TopToolBarArea, toolbar)
        toolbar.addWidget(QPushButton('Nouveau'))
        toolbar.addWidget(QPushButton('Ouvrir'))
        toolbar.addWidget(QPushButton('Sauvegarder'))
        toolbar.addWidget(QPushButton('Annuler'))
        toolbar.addWidget(QPushButton('Résoudre'))
        toolbar.addWidget(QPushButton('Ajouter\ncomposant')) 
        toolbar.addWidget(QPushButton('Ajouter\nnoeud'))

        # Central Widget
        main_view = InterfaceGraphique()
        self.setCentralWidget(main_view)

        # Status Bar
        status_bar = self.statusBar()
        status_bar.showMessage("Application développée par Eliott, Lucie et Emeric - FIP MIK4", 10000)

#TODO Liste composant
    def create_dock_windows(self):
        dock = QDockWidget("Liste des composants", self)
#TODO Resize horizontal
        dock.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.liste_composants = QWidget(dock)
        
        #Demo
        #self._customer_list.addAction(QPushButton("Résistance : R1", self))
        #self._customer_list.addItems(QPushButton("Générateur Tension : G", self))

        dock.setWidget(self.liste_composants)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

        dock = QDockWidget("Info composants", self)
#TODO Resize horizontal
        dock.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.info_composants = QWidget(dock)
        
        #Demo
        #self._customer_list.addAction(QPushButton("Résistance : R1", self))
        #self._customer_list.addItems(QPushButton("Générateur Tension : G", self))

        dock.setWidget(self.info_composants)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)


    # Slots privés
    @Slot()
    def quitter_app(self):
        QApplication.quit()
    @Slot()
    def aide(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
    @Slot()
    def github(self):
        webbrowser.open("https://github.com/lucie-wabartha/circuitRLC")
    @Slot()
    def resoudre(self):
#TODO Pop-up resoudre 
        pass

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
class Résultats(QDockWidget):
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