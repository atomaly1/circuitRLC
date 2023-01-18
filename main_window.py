'''
Created on 25 juin 2022

@author: Eliott, Lucie & Emeric
'''

import sys, webbrowser

from PySide6.QtCore import QSize, Qt, Slot, QTextStream, QFile 
from PySide6.QtGui import QIcon, QAction, QKeySequence, QRegularExpressionValidator
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QToolBar, QDockWidget, QFileDialog, QDialog, QDialogButtonBox, QMessageBox, QTextEdit, QFormLayout, QLabel, QLineEdit, QVBoxLayout, QComboBox

from noeud import Noeud
from circuit import Circuit
from sys_lineaire import SysLineaire
from interface_graphique import *
from math import pi

circuit_courant = Circuit([],[])

#TODO Ajouter au GSheet
# Fenêtre principale (selon le "Dock Widget Example" : https://doc.qt.io/qtforpython/examples/example_widgets_mainwindows_dockwidgets.html?highlight=dock%20widget#dock-widget-example)
class MainWindow(QMainWindow): 
   
    def __init__(self):
        super().__init__() # Appel du constructeur parent

        # Central Widget
        interface_graphique = InterfaceGraphique()
        self.setCentralWidget(interface_graphique)
        #self.centralWidget().create_ui()

        # Design
        self.setWindowTitle('CircuitRLC')                       # Titre
        self.setWindowIcon(QIcon('icons/rlc_project_v2.ico'))   # Icône
        self.resize(1000, 700)                                   # Taille de la fenêtre
        self.setMinimumSize(400, 300)                           # Taille min
        #self.setMaximumSize(800, 600)                           # Taille MAX
        #self.setStyleSheet('background:rgba(255,255,255,127)')  # Couleur du fond (white, black, cyan, red, magenta, green, yellow, blue, gray, lightGray, darkGray... OU Color Picker Online OU rgba(63,195,255,127))
        
        # Initialisation des éléments de la fenêtre principale
        self.creer_actions()
        self.creer_boutons()
        self.creer_menus()
        self.creer_barre_outils()
        self.creer_barre_etat()
        self.creer_fenetres_detachables()

    def set_circuit_courant(self, circuit : Circuit):
        global circuit_courant
        circuit_courant = circuit

    def get_circuit_courant(self):
        return circuit_courant    

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

        # Action supprimer composant
        self._action_supprimer_composant = QAction('Supprimer', self,
        shortcut=QKeySequence('Ctrl+D'),
        statusTip="Supprimer le composant sélectionné", triggered=self.supprimer_composant)

        # Action modifier composant
        self._action_modifier_composant = QAction('Modifier', self,
        shortcut=QKeySequence('Ctrl+M'),
        statusTip="Modifier le composant sélectionné", triggered=self.modifier_composant)

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

        # Bouton supprimer composant
        self._bouton_supprimer_composant = QPushButton('Supprimer')
        self._bouton_supprimer_composant.clicked.connect(self.supprimer_composant)

        # Bouton modifier composant
        self._bouton_modifier_composant = QPushButton('Modifier')
        self._bouton_modifier_composant.clicked.connect(self.modifier_composant)

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
        # Réticule dans le fichier 'interface_graphique.py'
        status_bar_droite1 = QLabel("En fonctionnement")
        self.statusBar().addPermanentWidget(status_bar_droite1,0)
        status_bar_droite1

#TODO Terminer les fenêtres détachables "Liste composants" et "Info composant"
    # Fenêtres détachables
    def creer_fenetres_detachables(self):

        ##### Liste composants #####
        # Layout
        dock = QDockWidget("Liste des composants", self)
        dock.setMinimumSize(QSize(180,100))
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self._liste_composants = QWidget(dock)
        dock.setWidget(self._liste_composants)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        self._menu_affichage.addAction(dock.toggleViewAction())

#TODO Ajout dynamique de boutons cliquables

        ##### Informations du composant selectionné #####
        ### Layout ###
        dock = QDockWidget("Info composant", self)
        dock.setMinimumSize(QSize(180,100))
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self._info_composant = QWidget(dock)
        self._info_composant.setLayout(QFormLayout())
        dock.setWidget(self._info_composant)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        self._menu_affichage.addAction(dock.toggleViewAction())

        ### Afficher les informations du composant selectionné ###
        # Type
        self.le_type_composant = QLineEdit("")
        self.le_type_composant.setReadOnly(True)
        self.le_type_composant.setPlaceholderText("Résistance")
#TODO Remplacer "Résistance" par le type du composant selectionné
        self._info_composant.layout().addRow(QLabel("Type : "), self.le_type_composant)
        # Nom
        self.le_nom_composant = QLineEdit("")
        self.le_nom_composant.setReadOnly(True)
        self.le_nom_composant.setPlaceholderText("R1")
#TODO Remplacer "R1" par le nom du composant selectionné
        self._info_composant.layout().addRow(QLabel("Nom : "), self.le_nom_composant)
        # Valeur
        self.le_valeur_composant = QLineEdit("")
        self.le_valeur_composant.setReadOnly(True)
        self.le_valeur_composant.setPlaceholderText("1000")
#TODO Remplacer "1000" par la valeur du composant selectionné
        self._info_composant.layout().addRow(QLabel("Valeur : "), self.le_valeur_composant)
        # Noeud départ
        self.le_noeud_depart_composant = QLineEdit("")
        self.le_noeud_depart_composant.setReadOnly(True)
        self.le_noeud_depart_composant.setPlaceholderText("n1")
#TODO Remplacer "n1" par le nom du noeud de départ du composant selectionné
        self._info_composant.layout().addRow(QLabel("Noeud départ : "), self.le_noeud_depart_composant)
        # Noeud arrivée
        self.le_noeud_arrivee_composant = QLineEdit("")
        self.le_noeud_arrivee_composant.setReadOnly(True)
        self.le_noeud_arrivee_composant.setPlaceholderText("n2")
#TODO Remplacer "n2" par le nom du noeud d'arrivée du composant selectionné
        self._info_composant.layout().addRow(QLabel("Noeud arrivée : "), self.le_noeud_arrivee_composant)
        # Boutons supprimer et modifier
        self._info_composant.layout().addRow(self._bouton_supprimer_composant, self._bouton_modifier_composant)
#TODO Griser les boutons si aucun composant n'est selectionné

        ##### Fenêtre de résultats #####
        ### Layout ###
        dock = QDockWidget("Résultats", self)
        dock.setMinimumSize(QSize(180,100))
        dock.setAllowedAreas(Qt.BottomDockWidgetArea)
        self._resultats = QWidget(dock)
        self._resultats.setLayout(QVBoxLayout()) 
        dock.setWidget(self._resultats)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock)
        self._menu_affichage.addAction(dock.toggleViewAction())

        ### Affichage des résultats sous forme de texte ###
        self._te_resultats = QTextEdit()                                              # Widget d'affichage du texte
        self._te_resultats.setReadOnly(True)                                          # Lecture seule
        self._te_resultats.setLineWrapMode(QTextEdit.NoWrap)                          # Pas de retour à la ligne automatique
        self._resultats.layout().addWidget(self._te_resultats)

    @Slot()
    def nouveau(self):
#TODO Nouveau circuit
        self.statusBar().showMessage("Nouveau circuit créé", 2000)

#TODO Ouvrir circuit de test
    @Slot()
    def ouvrir(self):
        self.setCentralWidget(InterfaceGraphique())
        self.centralWidget().create_ui()
        self.centralWidget().show()
        self.set_circuit_courant(Circuit.create_circuit_test())
        self._te_resultats.setText(f'{self.get_circuit_courant()}')
        self.statusBar().showMessage("Circuit de test ouvert", 2000) #"Circuit ouvert"

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
    
#TODO Annuler
    @Slot()
    def annuler(self):
        self.statusBar().showMessage("Dernière action annulée", 2000)

#TODO Refaire
    @Slot()
    def refaire(self):
        self.statusBar().showMessage("Action rétablie", 2000)

    @Slot()
    def resoudre(self):

        # Design
        self._popup_resoudre = QDialog(self)
        self._popup_resoudre.setWindowModality(Qt.ApplicationModal)
        self._popup_resoudre.setWindowTitle("Résoudre le circuit")
        self._popup_resoudre.setFixedSize(279,75)

        # Layout
        layout = QFormLayout(self._popup_resoudre)

        le = QLineEdit("")
        le.setValidator(QRegularExpressionValidator("[0-9]\\d{0,11}\\.[0-9]\\d{0,2}")) # https://www.ics.com/blog/qt-support-input-masks-and-validators
        le.setPlaceholderText("432.0")
        layout.addRow(QLabel("Fréquence f [Hz] : "), le)
        
        self._boutons_popup_resoudre = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addRow(self._boutons_popup_resoudre) # https://stackoverflow.com/questions/3016974/how-to-get-text-in-qlineedit-when-qpushbutton-is-pressed-in-a-string
        
        self._popup_resoudre.show()

        # Force l'utilisateur à entrer des valeurs valides dans chaque champ de saisi pour débloquer le bouton OK
        self._boutons_popup_resoudre.button(QDialogButtonBox.Ok).setEnabled(False)
        le.textChanged.connect(lambda: self._boutons_popup_resoudre.button(QDialogButtonBox.Ok).setEnabled(le.hasAcceptableInput())) #https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLineEdit.html#PySide6.QtWidgets.PySide6.QtWidgets.QLineEdit.textChanged
 
        # Connecte les boutons OK et Annuler à la fonction accept_noeud et reject respectivement
        self._boutons_popup_resoudre.accepted.connect(lambda: self.accept_resoudre(float(le.text())))
        self._boutons_popup_resoudre.rejected.connect(self._popup_resoudre.reject)

#TODO circuit.resoudre(f)
    @Slot(float)
    def accept_resoudre(self, f : float):
        omega = f * 2 * pi
        self._te_resultats.setText(f'{circuit_courant}')
        lin_sys = SysLineaire.create_sys_lin(circuit_courant, omega)
        sol = lin_sys.solve()
        self._te_resultats.setText(f'{lin_sys}\n{lin_sys.solve_str(sol)}')
        self._popup_resoudre.accept()
        self.statusBar().showMessage(f"Circuit résolu pour une fréquence f = {f} Hz", 4000)

    @Slot()
    def aide(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab")
        self.statusBar().showMessage("Ouverture de l'aide", 2000)
    
    @Slot()
    def github(self):
        webbrowser.open("https://github.com/lucie-wabartha/circuitRLC")
        self.statusBar().showMessage("Ouverture de GitHub : circuitRLC", 2000)

#TODO Popup pour ajouter un composant
    @Slot()
    def ajouter_composant(self):
        
        # Design
        self._popup_composant = QDialog(self)
        self._popup_composant.setWindowModality(Qt.ApplicationModal)
        self._popup_composant.setWindowTitle("Ajouter un composant")
        self._popup_composant.setFixedSize(280,180)

        # Layout
        layout = QFormLayout(self._popup_composant)

        # Liste déroulante pour choisir le type de composant (Résistance, Inductance, Condensateur, Générateur de tension, Fil)
        self._liste_composant = QComboBox()
        self._liste_composant.addItems(["Résistance", "Inductance", "Condensateur", "Générateur de tension", "Fil"])
        layout.addRow(QLabel("Type : "), self._liste_composant)

        # Nom
        le_nom = QLineEdit("")
        le_nom.setValidator(QRegularExpressionValidator("[a-zA-Z0-9]\\N{0,14}"))
        le_nom.setPlaceholderText("R1")
        layout.addRow(QLabel("Nom : "), le_nom)
        # Valeur
        le_valeur = QLineEdit("")
        le_valeur.setValidator(QRegularExpressionValidator("[0-9]\\d{0,11}\\.[0-9]\\d{0,2}")) # https://www.ics.com/blog/qt-support-input-masks-and-validators
        le_valeur.setPlaceholderText("200.0")
        layout.addRow(QLabel("Valeur : "), le_valeur)

        # Liste déroulante pour choisir le noeud de départ
        self._liste_noeud_depart = QComboBox()
        self._liste_noeud_depart.addItems(["n1", "n2", "n3", "n4"])
        layout.addRow(QLabel("Noeud de départ : "), self._liste_noeud_depart)

        # Liste déroulante pour choisir le noeud d'arrivée
        self._liste_noeud_arrivee = QComboBox()
        self._liste_noeud_arrivee.addItems(["n1", "n2", "n3", "n4"])
        layout.addRow(QLabel("Noeud d'arrivée : "), self._liste_noeud_arrivee)

        self._boutons_popup_composant = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addRow(self._boutons_popup_composant) # https://stackoverflow.com/questions/3016974/how-to-get-text-in-qlineedit-when-qpushbutton-is-pressed-in-a-string
        
        self._popup_composant.show()              

        # Force l'utilisateur à entrer des valeurs valides dans chaque champ de saisi pour débloquer le bouton OK
        self._boutons_popup_composant.button(QDialogButtonBox.Ok).setEnabled(False)
        le_nom.textChanged.connect(lambda: self._boutons_popup_composant.button(QDialogButtonBox.Ok).setEnabled(le_nom.hasAcceptableInput() and le_valeur.hasAcceptableInput()))
        le_valeur.textChanged.connect(lambda: self._boutons_popup_composant.button(QDialogButtonBox.Ok).setEnabled(le_nom.hasAcceptableInput() and le_valeur.hasAcceptableInput()))

        # Connecte les boutons OK et Annuler à la fonction accept_noeud et reject respectivement
        self._boutons_popup_composant.accepted.connect(lambda: self.accept_composant("Résistance", le_nom.text(), le_valeur.text(), "n1", "n2"))
        self._boutons_popup_composant.rejected.connect(self._popup_composant.reject)        

#TODO circuit.supprimer() si bouton OK cliqué
    @Slot()
    def supprimer_composant(self):
        
        msg = QMessageBox()
        msg.setWindowModality(Qt.ApplicationModal)
        msg.setWindowTitle("Confirmation de suppression")
        msg.setWindowIcon(QIcon('icons/rlc_project_v2.ico')) 
        msg.setText("Êtes-vous sûr de vouloir supprimer le composant sélectionné ?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        ret = msg.exec()

        if ret == QMessageBox.Ok:
            # Ecrire dans la barre d'état "Elément supprimé" pendant 2 secondes
            self.statusBar().showMessage("Composant supprimé", 2000)
        else:
            # Fermer la fenêtre de confirmation
            pass

#TODO popup et circuit.modifier()
    @Slot()
    def modifier_composant(self):  
        self.statusBar().showMessage("Composant modifié", 2000)

#TODO circuit.ajouter_composant(type, nom, valeur, noeud_depart, noeud_arrivee) 
    @Slot(str, str, float, Noeud, Noeud)
    def accept_composant(self, type: str, nom: str, valeur: float, noeud_depart: Noeud, noeud_arrivee: Noeud):
        
        self._popup_composant.accept()
        self.statusBar().showMessage(f"{type} '{nom}' valant {valeur} entre {noeud_depart} et {noeud_arrivee} ajouté(e)", 4000)

    @Slot()
    def ajouter_noeud(self):
     
        # Design
        self._popup_noeud = QDialog(self)
        self._popup_noeud.setWindowModality(Qt.ApplicationModal)
        self._popup_noeud.setWindowTitle("Ajouter un noeud")
        self._popup_noeud.setMinimumSize(178,130)
        self._popup_noeud.setMaximumSize(268,130)
        self._popup_noeud.resize(268,130)

        # Layout
        layout = QFormLayout(self._popup_noeud)

        le1 = QLineEdit("")

        le1.setValidator(QRegularExpressionValidator("[a-zA-Z0-9]\\N{0,14}")) # https://www.ics.com/blog/qt-support-input-masks-and-validators
        layout.addRow(QLabel("Nom : "), le1)
        le1.setPlaceholderText("n1")

        le2 = QLineEdit("")
        le2.setValidator(QRegularExpressionValidator("[0-9]\\d{0,2}"))
        layout.addRow(QLabel("Coordonnée X : "), le2)
        le2.setPlaceholderText("118")

        le3 = QLineEdit("")
        le3.setValidator(QRegularExpressionValidator("[0-9]\\d{0,2}"))
        layout.addRow(QLabel("Coordonnée Y : "), le3)
        le3.setPlaceholderText("712")
        
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

#TODO circuit.ajouter_noeud(nom, nx, ny)
    @Slot(str, float, float)
    def accept_noeud(self, nom: str, nx: float, ny: float):
        
        self._popup_noeud.accept()
        self.statusBar().showMessage(f"Noeud '{nom}' ajouté en ({nx} ; {ny})", 4000)

if __name__ == '__main__':
    pass
