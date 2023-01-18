# TODO : import all classes necessary with (example): 

import sys
from main_window import MainWindow
from PySide6.QtWidgets import QApplication

# TODO faire la strucuture du programme (voir sujet du TP pour les outputs)

if __name__ == '__main__':

    app = QApplication(sys.argv)    # Création de l'instance d'application en lui passant le tableau des arguments

    main_window = MainWindow()      # Instanciation de la fenêtre principale
    main_window.show()              # Afficher la fenêtre principale

    sys.exit(app.exec())            # Démarrage de la boucle de gestion des événements
