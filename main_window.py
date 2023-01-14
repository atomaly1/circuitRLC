'''
Created on 25 juin 2022

@author: Eliott, Lucie & Emeric
'''

import sys, webbrowser

from PySide6.QtCore import QSize, Qt, Slot, QTextStream, QFile 
from PySide6.QtGui import QIcon, QAction, QKeySequence, QRegularExpressionValidator
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QToolBar, QDockWidget, QFileDialog, QDialog, QDialogButtonBox, QMessageBox, QTextEdit, QFormLayout, QLabel, QLineEdit

from circuit import Circuit
from interface_graphique import *

#from interface_graphique import InterfaceGraphique

#TODO Ajouter au GSheet
# Fenêtre principale (selon le "Dock Widget Example" : https://doc.qt.io/qtforpython/examples/example_widgets_mainwindows_dockwidgets.html?highlight=dock%20widget#dock-widget-example)
class MainWindow(QMainWindow): 
   
    def __init__(self):
        super().__init__() # Appel du constructeur parent

        # Central Widget
        interface_graphique = InterfaceGraphique()
        self.setCentralWidget(interface_graphique)

        # Design
        self.setWindowTitle('CircuitRLC')                       # Titre
        self.setWindowIcon(QIcon('icons/rlc_project_v2.ico'))   # Icône
        self.resize(800, 600)                                   # Taille de la fenêtre
        self.setMinimumSize(400, 300)                           # Taille min
        #self.setMaximumSize(800, 600)                          # Taille MAX
        #self.setStyleSheet('background:rgba(255,255,255,127)')  # Couleur du fond (white, black, cyan, red, magenta, green, yellow, blue, gray, lightGray, darkGray... OU Color Picker Online OU rgba(63,195,255,127))
        
        # Initialisation des éléments de la fenêtre principale
        self.creer_actions()
        self.creer_boutons()
        self.creer_menus()
        self.creer_barre_outils()
        self.creer_barre_etat()
        self.creer_fenetres_detachables()

    # Actions
    def creer_actions(self):    
        
        # Action nouveau
        self._action_nouveau = QAction('Nouveau', self,
        shortcut=QKeySequence.New, 
        statusTip="Créer un nouveau circuit", triggered=self.nouveau)

        # Action ouvrir
        self._action_ouvrir = QAction('Ouvrir', self,
        shortcut=QKeySequence.Open,
        statusTip="Ouvrir un circuit", triggered=self.ouvrir)
        
        # Action sauvegarder
        self._action_sauvegarder = QAction('Sauvegarder', self,
        shortcut=QKeySequence.Save,
        statusTip="Sauvegarder le circuit", triggered=self.sauvegarder)

        # Action quitter
        self._action_quitter = QAction('Quitter', self,
        shortcut=QKeySequence('Ctrl+Q'),
        statusTip="Quitter l'application", triggered=self.close)
        
        # Action annuler
        self._action_annuler = QAction('Annuler', self,
        shortcut=QKeySequence.Undo,
        statusTip="Annuler la dernière action", triggered=self.annuler)

        # Action refaire
        self._action_refaire = QAction('Refaire', self,
        shortcut=QKeySequence.Redo,
        statusTip="Refaire la dernière action", triggered=self.refaire)
        
        # Action resoudre
        self._action_resoudre = QAction('Résoudre', self,
        shortcut=QKeySequence('Ctrl+R'),
        statusTip="Résoudre le circuit", triggered=self.resoudre)

        # Action aide
        self._action_aide = QAction('Aide', self,
        shortcut=QKeySequence.HelpContents,
        statusTip="Afficher l'aide", triggered=self.aide)
        
        # Action Github
        self._action_github = QAction('GitHub CircuitRLC', self,
        shortcut=QKeySequence('F2'),
        statusTip="Afficher le GitHub du projet CircuitRLC", triggered=self.github)

    # Boutons
    def creer_boutons(self):
        
        # Bouton nouveau
        self._bouton_nouveau = QPushButton('Nouveau')
        self._bouton_nouveau.clicked.connect(self.nouveau)

        # Bouton ouvrir
        self._bouton_ouvrir = QPushButton('Ouvrir')
        self._bouton_ouvrir.clicked.connect(self.ouvrir)

        # Bouton sauvegarder
        self._bouton_sauvegarder = QPushButton('Sauvegarder')
        self._bouton_sauvegarder.clicked.connect(self.sauvegarder)

        # Bouton quitter
        self._bouton_annuler = QPushButton('Annuler')
        self._bouton_annuler.clicked.connect(self.annuler)

        # Bouton refaire
        self._bouton_resoudre = QPushButton('Résoudre')
        self._bouton_resoudre.clicked.connect(self.resoudre)

        # Bouton composant
        self._bouton_composant = QPushButton('Ajouter\ncomposant')
        self._bouton_composant.clicked.connect(self.ajouter_composant)

        # Bouton noeud
        self._bouton_noeud = QPushButton('Ajouter\nnoeud')
        self._bouton_noeud.clicked.connect(self.ajouter_noeud)

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
    def creer_barre_etat(self):      
        self.statusBar().showMessage("Application développée par Eliott, Lucie et Emeric - FIP MIK4", 10000)
        status_bar_droite1 = QLabel("En fonctionnement")
        self.statusBar().addPermanentWidget(status_bar_droite1,0)

    # Fenêtres détachables
    def creer_fenetres_detachables(self):

        # Liste composants 
        # Layout
        dock = QDockWidget("Liste des composants", self)
        dock.setMinimumSize(QSize(180,100))
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self._liste_composants = QWidget(dock)
        dock.setWidget(self._liste_composants)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        self._menu_affichage.addAction(dock.toggleViewAction())

#TODO Ajout dynamique de boutons cliquables

        # Informations du composant selectionné
        # Layout
        dock = QDockWidget("Info composants", self)
        dock.setMinimumSize(QSize(180,100))
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
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

    @Slot()
    def nouveau(self):
#TODO Nouveau circuit
        self.statusBar().showMessage("Nouveau circuit créé", 2000)
        pass

    @Slot()
    def ouvrir(self):
#TODO Ouvrir circuit
        self.statusBar().showMessage("Circuit ouvert", 2000)
        pass

    # Test sauvegarde
    @Slot()
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
            out << self._text_edit.toPlainText()

        self.statusBar().showMessage(f"{filename} enregistré", 2000)

    @Slot()
    def quitter_app(self):
        QApplication.quit()
    
    @Slot()
    def annuler(self):
#TODO Annuler
        self.statusBar().showMessage("Dernière action annulée", 2000)
        pass

    @Slot()
    def refaire(self):
#TODO Refaire
        self.statusBar().showMessage("Action rétablie", 2000)
        pass

    @Slot()
    def resoudre(self):
#TODO Pop-up resoudre 
        QMessageBox.about(self, "Résoudre", "Work \nIn \nProgress")
        self.statusBar().showMessage("Résolution du circuit", 2000)
        pass

    @Slot()
    def aide(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab")
        self.statusBar().showMessage("Ouverture de l'aide", 2000)
    
    @Slot()
    def github(self):
        webbrowser.open("https://github.com/lucie-wabartha/circuitRLC")
        self.statusBar().showMessage("Ouverture de GitHub : circuitRLC", 2000)

    @Slot()
    def ajouter_composant(self):
#TODO Pop-up ajouter composant
        QMessageBox.about(self, "Ajouter composant", "Work \nIn \nProgress")
        self.statusBar().showMessage("Composant ajouté", 2000)
        pass

    @Slot()
    def ajouter_noeud(self):
     
        # Design
        self._popup_noeud = QDialog(self)
        self._popup_noeud.setWindowTitle("Ajouter un noeud")
        self._popup_noeud.setMinimumSize(178,130)
        self._popup_noeud.setMaximumSize(268,130)
        self._popup_noeud.resize(268,130)

        # Layout
        layout = QFormLayout(self._popup_noeud)

        le1 = QLineEdit("")
        le1.setValidator(QRegularExpressionValidator("\\N{0,15}")) # https://www.ics.com/blog/qt-support-input-masks-and-validators
        #le2.setPlaceholderText("Nom du noeud")
        layout.addRow(QLabel("Nom : "), le1)

        le2 = QLineEdit("")
        le2.setValidator(QRegularExpressionValidator("[0-9]\\d{0,2}"))
        layout.addRow(QLabel("Coordonnée X : "), le2)

        le3 = QLineEdit("")
        le3.setValidator(QRegularExpressionValidator("[0-9]\\d{0,2}"))
        layout.addRow(QLabel("Coordonnée Y : "), le3)

        self._boutons_popup_noeud = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addRow(self._boutons_popup_noeud) # https://stackoverflow.com/questions/3016974/how-to-get-text-in-qlineedit-when-qpushbutton-is-pressed-in-a-string
        self._popup_noeud.show()              

        # Force l'utilisateur à entrer des valeurs valides dans chaque champ de saisi pour débloquer le bouton OK
        self._boutons_popup_noeud.button(QDialogButtonBox.Ok).setEnabled(False)
        le1.textChanged.connect(lambda: self._boutons_popup_noeud.button(QDialogButtonBox.Ok).setEnabled(le1.hasAcceptableInput() and le2.hasAcceptableInput() and le3.hasAcceptableInput()))
        le2.textChanged.connect(lambda: self._boutons_popup_noeud.button(QDialogButtonBox.Ok).setEnabled(le1.hasAcceptableInput() and le2.hasAcceptableInput() and le3.hasAcceptableInput()))
        le3.textChanged.connect(lambda: self._boutons_popup_noeud.button(QDialogButtonBox.Ok).setEnabled(le1.hasAcceptableInput() and le2.hasAcceptableInput() and le3.hasAcceptableInput()))

        # Connecte les boutons OK et Annuler à la fonction accept_noeud et reject respectivement
        self._boutons_popup_noeud.accepted.connect(lambda: self.accept_noeud(le1.text(), le2.text(), le3.text()))
        self._boutons_popup_noeud.rejected.connect(self._popup_noeud.reject)        

    @Slot(str, float, float)
    def accept_noeud(self, nom: str, nx: float, ny: float):
#TODO circuit.add_noeud(nom, nx, ny)       
        self._popup_noeud.accept()
        self.statusBar().showMessage(f"Noeud '{nom}' ajouté en ({nx} ; {ny})", 4000)
        pass

if __name__ == '__main__':
    
    app = QApplication(sys.argv)    # Création de l'instance d'application en lui passant le tableau des arguments

    main_window = MainWindow()      # Instanciation de la fenêtre principale
    main_window.show()              # Afficher la fenêtre principale

    sys.exit(app.exec())            # Démarrage de la boucle de gestion des événements