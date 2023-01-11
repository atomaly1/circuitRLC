import sys, webbrowser

from PySide6.QtCore import QSize, Qt, Slot, QTextStream, QFile
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QWidget, QDockWidget, QPushButton, QFileDialog, QDialog, QMessageBox, QTextEdit

#TODO Ajouter au GSheet
# Fenêtre principale (selon le "Dock Widget Example" : https://doc.qt.io/qtforpython/examples/example_widgets_mainwindows_dockwidgets.html?highlight=dock%20widget#dock-widget-example)
class MainWindow(QMainWindow): 
   
    def __init__(self):
        super().__init__() # Appel du constructeur parent

        # Central Widget
#TODO Importer le fichier interface_graphique.py
        #interface_graphique = InterfaceGraphique()
        self._text_edit = QTextEdit()
        self.setCentralWidget(self._text_edit)

        # Design
        self.setWindowTitle('CircuitRLC')                       # Titre
        self.setWindowIcon(QIcon('icons/rlc_project_v2.ico'))   # Icône
        self.resize(800, 600)                                   # Taille de la fenêtre
        self.setMinimumSize(400, 300)                           # Taille min
        #self.setMaximumSize(800, 600)                          # Taille MAX
        self.setStyleSheet('background:rgba(255,255,255,127)')  # Couleur du fond (white, black, cyan, red, magenta, green, yellow, blue, gray, lightGray, darkGray... OU Color Picker Online OU rgba(63,195,255,127))
        
        # Initialisation des éléments de la fenêtre principale
        self.creer_actions()
        self.creer_boutons()
        self.creer_menus()
        self.creer_barre_outils()
        self.creer_fenetres_detachables()    

    # Actions
    def creer_actions(self):    
        
        # Action nouveau
        self._action_nouveau = QAction('Nouveau', self)
        self._action_nouveau.setShortcut('Ctrl+N')
        
        # Action ouvrir
        self._action_ouvrir = QAction('Ouvrir', self)
        self._action_ouvrir.setShortcut('Ctrl+O')
        
        # Action sauvegarder
        self._action_sauvegarder = QAction('Sauvegarder', self)
        self._action_sauvegarder.setShortcut('Ctrl+S')
        self._action_sauvegarder.triggered.connect(self.sauvegarder)
        
        # Action quitter
        self._action_quitter = QAction('Quitter', self)             # Création d'une action (QAction)
        self._action_quitter.setShortcut('Ctrl+Q')                  # Ajout d'un raccourci pour réaliser une action
        self._action_quitter.triggered.connect(self.quitter_app)    # Déclenchement de la méthode fermant l'application
        
        # Action annuler
        self._action_annuler = QAction('Annuler', self)
        self._action_annuler.setShortcut('Ctrl+Z')
        
        # Action refaire
        self._action_refaire = QAction('Refaire', self)
        self._action_refaire.setShortcut('Ctrl+Y')
        
        # Action resoudre
        self._action_resoudre = QAction('Résoudre', self)
        self._action_resoudre.setShortcut('Ctrl+R')
        self._action_resoudre.triggered.connect(self.resoudre)
        
        # Action aide
        self._action_aide = QAction('Aide', self)
        self._action_aide.setShortcut('F1')
        self._action_aide.triggered.connect(self.aide)
        
        # Action Github
        self._action_github = QAction('Github CircuitRLC', self)
        self._action_github.setShortcut('F2')
        self._action_github.triggered.connect(self.github)

    # Boutons
    def creer_boutons(self):
        
        self._bouton_nouveau = QPushButton('Nouveau')
        self._bouton_ouvrir = QPushButton('Ouvrir')
        self._bouton_sauvegarder = QPushButton('Sauvegarder')
        self._bouton_annuler = QPushButton('Annuler')
        self._bouton_resoudre = QPushButton('Résoudre')
        self._bouton_composant = QPushButton('Ajouter\ncomposant')
        self._bouton_noeud = QPushButton('Ajouter\nnoeud')

    # Barre de menus
    def creer_menus(self):
        
        self._menu_fichier = self.menuBar().addMenu('Fichier')  # Ajout d'un menu déroulant (QMenu)
        self._menu_fichier.addAction(self._action_nouveau)      # Ajout d'une action au menu
        self._menu_fichier.addAction(self._action_ouvrir)
        self._menu_fichier.addSeparator()
        self._menu_fichier.addAction(self._action_sauvegarder)
        self._menu_fichier.addSeparator()
        self._menu_fichier.addAction(self._action_quitter)

        self._menu_edition = self.menuBar().addMenu('Edition')
        self._menu_edition.addAction(self._action_annuler)
        self._menu_edition.addAction(self._action_refaire)

        self._menu_affichage = self.menuBar().addMenu('Affichage')

        self.menuBar().addSeparator()

        self._menu_calculs = self.menuBar().addMenu('Calculs')
        self._menu_calculs.addAction(self._action_resoudre)

        self._menu_aide = self.menuBar().addMenu('Aide')
        self._menu_aide.addAction(self._action_aide)
        self._menu_aide.addSeparator()
        self._menu_aide.addAction(self._action_github)

    # Barre d'outils
    def creer_barre_outils(self):

        self._barre_outils = QToolBar('Toolbar')
        self._barre_outils.setIconSize(QSize(16,16))
        self.addToolBar(Qt.TopToolBarArea, self._barre_outils)
        self._barre_outils.addWidget(self._bouton_nouveau)
        self._barre_outils.addWidget(self._bouton_ouvrir)
        self._barre_outils.addWidget(self._bouton_sauvegarder)
        self._barre_outils.addWidget(self._bouton_annuler)
        self._barre_outils.addWidget(self._bouton_resoudre)
        self._barre_outils.addWidget(self._bouton_composant)
        self._barre_outils.addWidget(self._bouton_noeud)

    # Barre de status
    def creer_barre_statut(self):

        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Application développée par Eliott, Lucie et Emeric - FIP MIK4", 10000)
#TODO Réticule (dans cette box ?)

    # Fenêtres détachables
    def creer_fenetres_detachables(self):

        # Liste composants 
        # Layout
        dock = QDockWidget("Liste des composants", self)
        dock.setMinimumSize(QSize(180,100))
        dock.setAllowedAreas(Qt.LeftDockWidgetArea)
        self._liste_composants = QWidget(dock)
        dock.setWidget(self._liste_composants)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        self._menu_affichage.addAction(dock.toggleViewAction())

#TODO Ajout dynamique de boutons cliquables

        # Informations du composant selectionné
        # Layout
        dock = QDockWidget("Info composants", self)
        dock.setMinimumSize(QSize(180,100))
        dock.setAllowedAreas(Qt.LeftDockWidgetArea)
        self._info_composants = QWidget(dock)
        dock.setWidget(self._info_composants)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        self._menu_affichage.addAction(dock.toggleViewAction())

#TODO Afficher les informations du composant selectionné

        # Informations du composant selectionné
        # Layout
        dock = QDockWidget("Résultats", self)
        dock.setMinimumSize(QSize(180,100))
        dock.setAllowedAreas(Qt.BottomDockWidgetArea)
        self._liste_composants = QWidget(dock)
        dock.setWidget(self._liste_composants)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock)
        self._menu_affichage.addAction(dock.toggleViewAction())

#TODO Afficher les informations du composant selectionné

    # Slots privés
    @Slot()
    # Test sauvegarde
    def sauvegarder(self):
        dialog = QFileDialog(self, "Enregistrer sous")
        dialog.setMimeTypeFilters(['text/plain'])
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setDefaultSuffix('txt')
        if dialog.exec() != QDialog.Accepted:
            return

        filename = dialog.selectedFiles()[0]
        file = QFile(filename)
        if not file.open(QFile.WriteOnly | QFile.Text):
            reason = file.errorString()
            QMessageBox.warning(self, "Dock Widgets",
                    f"Cannot write file {filename}:\n{reason}.")
            return

        out = QTextStream(file)
        with QApplication.setOverrideCursor(Qt.WaitCursor):
            out << self._text_edit.toHtml()

        self.statusBar().showMessage(f"Enregistrement de '{filename}'", 2000)


    @Slot()
    def quitter_app(self):
        QApplication.quit()
    
    @Slot()
    def aide(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab")
    
    @Slot()
    def github(self):
        webbrowser.open("https://github.com/lucie-wabartha/circuitRLC")
    
    @Slot()
    def resoudre(self):
#TODO Pop-up resoudre 
        pass

# Divers
#TODO Ajouter les boutons pour chaque composant
#TODO Un pop up par composant (QPopUpWidget à chercher si existant)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)    # Création de l'instance d'application en lui passant le tableau des arguments

    main_window = MainWindow()      # Instanciation de la fenêtre principale
    main_window.show()              # Afficher la fenêtre principale

    sys.exit(app.exec())            # Démarrage de la boucle de gestion des événements