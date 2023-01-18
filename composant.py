#  Classe abstraite Composant :
#  - 1 nœud de départ,
#  - 1 nœud d’arrivée ;
#  pour pouvoir donner un sens à la valeur
#  positive ou négative des courants/tensions.

from abc import ABC, abstractmethod
from noeud import Noeud
from math import pi

class Composant(ABC):

    def __init__(self, noeud_depart: Noeud, noeud_arrivee: Noeud, w = 100.0) -> None:
        self._noeud_depart = noeud_depart
        self._noeud_arrivee = noeud_arrivee
        self._w = w

    @property
    def noeud_depart(self) -> Noeud:
        return self._noeud_depart

    @noeud_depart.setter
    def noeud_depart(self, noeud_depart: Noeud) -> None:
        self._noeud_depart = noeud_depart

    @property
    def noeud_arrivee(self) -> Noeud:
        return self._noeud_arrivee

    @noeud_arrivee.setter
    def noeud_arrivee(self, noeud_arrivee: Noeud) -> None:
        self._noeud_arrivee = noeud_arrivee

    @property
    def w(self) -> float:
        return self._w

    @w.setter
    def w(self, w: float) -> None:
        self._w = w

    @abstractmethod
    def coeff_u(self) -> complex:
        pass

    @abstractmethod
    def coeff_i(self) -> complex:
        pass

    @abstractmethod
    def coeff_c(self) -> complex:
        pass
