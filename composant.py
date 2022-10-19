#  Définir la classe abstraite Composant : 
#  tout composant possède un nœud de départ, 
#  et un nœud d’arrivée (on définie un nœud 
#  de départ et un nœud d’arrivée (relation 
#  orientée), plutôt que deux nœuds incidents 
#  pour pouvoir donner un sens à la valeur 
#  positive ou négative des courants/tensions).

from abc import ABC, abstractmethod, abstractproperty
from numbers import Complex
from noeud import Noeud

class Composant(ABC):

    def __init__(self, noeud_depart: Noeud, noeud_arrivee: Noeud, nom: str, valeur: float) -> None:
        self._noeud_depart = noeud_depart
        self._noeud_arrivee = noeud_arrivee
        self._nom = nom
        self._valeur = valeur

    # Pour être général, on va considérer que tout composant doit pouvoir calculer trois constantes
    # (complexes) CU , CI ,CC , qui définisse l’équation linéaire générale :
    # CU . U + CI .I = CC
    # Compléter la définition de la classe Composant avec la déclaration des méthodes abstraites coeffU
    # coeffI et coeffC. Spécialisez ces méthodes dans toutes les sous-classes.

    @abstractproperty
    def nom(self) -> str:
        return self._nom

    @nom.setter
    @abstractmethod
    def nom_setter(self, nom: str) -> None:
        self._nom = nom

    @abstractproperty
    def valeur(self) -> float:
        return self._nom

    @nom.setter
    @abstractmethod
    def valeur_setter(self, valeur: float) -> None:
        self._valeur = valeur

    @abstractmethod
    def coeffU(self) -> Complex:
        pass

    @abstractmethod
    def coeffI(self) -> Complex:
        pass

    @abstractmethod
    def coeffC(self) -> Complex:
        pass