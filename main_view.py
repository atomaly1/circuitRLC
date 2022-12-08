import PySide6.QtWidgets as qtw
import PySide6.QtGui as qtg
import random

class FrameAvecBordure(qtw.QFrame):
    # une variable de classe pour définir un comportement par défaut
    # si modifiée : modifie la bordure de toutes les FrameAvecBordure
    # ou le paramètre 'bordure' n'est pas explicitement fourni lors
    # de l'__init__
    DEFAULT_BORDURE = False

    # DEFAULT_BORDURE peut être utilisé dans __init__
    def __init__(self,bordure : bool = DEFAULT_BORDURE):
        super().__init__()
        if bordure :
            # une bordure simple; de nombreuses autres options possibles
            self.setFrameStyle(qtw.QFrame.Panel | qtw.QFrame.Plain)
            self.setLineWidth(1)

