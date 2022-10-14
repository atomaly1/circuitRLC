#  Définir la classe abstraite Composant : 
#  tout composant possède un nœud de départ, 
#  et un nœud d’arrivée (on définie un nœud 
#  de départ et un nœud d’arrivée (relation 
#  orientée), plutôt que deux nœuds incidents 
#  pour pouvoir donner un sens à la valeur 
#  positive ou négative des courants/tensions).

from abc import ABC, abstractmethod
from noeud import Noeud

class Composant(ABC):

    def __init__(self, noeud_depart: Noeud, noeud_arrivee: Noeud) -> None:
        self._noeud_depart = noeud_depart
        self._noeud_arrivee = noeud_arrivee