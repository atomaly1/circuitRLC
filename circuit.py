# CLASSE CIRCUIT
from noeud import Noeud

# TODO définir la classe CIRCUIT => ensemble de Noeuds = attribut noeuds de type list
class Circuit:
# TODO définir l'attribut noeuds avec @property et __init__ (voir noeud.py pour un exemple)
    def __init__(self, noeuds: list):
        self._noeuds = noeuds

    @property
    def noeuds(self) -> list:
        return self._noeuds

# TODO définir la méthode __str__
    def __str__(self):
        #return f"[{self.noeuds[0]}]"
        _str = ""
        for elmts in self.noeuds :
            _str += self.noeuds[elmts]
        return _str 

# TODO définir méthode maxX :renvoie l’abscisse maximale du circuit (abscisse du noeud du circuit ayant la plus grande abscisse). Retourne 0.0 si le circuit est vide (ne contient pas de noeuds)
    def maxX(self) -> float :
        maxX = 0.0
        if len(self._noeuds) == 0:
            pass
        else:
            for noeud in self._noeuds:
                if self._noeuds._nx > maxX:
                    maxX = self._noeuds._nx
        return maxX

# TODO definir méthode minX

# TODO définir méthode maxY

# TODO définir méthode minY

# TODO définir méthode  noeud_le_plus_proche : renvoie le noeud le plus proche du point de coordonnées px,py. Signale une erreur si le circuit ne contient pas de noeud par :
#   ▪ raise Exception("Circuit vide")

# TODO définir méthode contienNoeud

# TODO définir méthode addNoeud : ajoute un nœud au circuit. Si le nœud appartient déjà au circuit :
#   ▪ raise Exception("le noeud est déjà dans le circuit")
    def addNoeud(self, noeud : Noeud) -> None:
        self.noeuds.append(noeud)

# TODO définir méthode removeNoeud : retire un nœud du circuit. Si le nœud n’appartient pas au circuit :
#   ▪ raise Exception("le noeud n’est pas dans le circuit")
 
# TODO définir méthode menu : permet la gestion du circuit par menu textuel : voir ci-dessous un exemple d’interaction :
#   ▪ pour la suppression d’un nœud, vous aurez sans doute besoin de la méthode utilitaire choisiNoeud qui permet à l’utilisateur de choisir un nœud existant dans le circuit