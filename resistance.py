from math import sqrt
from composant import Composant
from noeud import Noeud
from numbers import Complex

class Resistance(Composant):
    
    def __init__(self, noeud_depart: Noeud, noeud_arrivee: Noeud, nom: str, valeur: float) -> None:
        super().__init__(noeud_depart, noeud_arrivee, nom, valeur)

    @property
    def nom(self) -> str:
        return super().nom

    @nom.setter
    def nom_setter(self, nom: str) -> None:
        return super().nom_setter

    @property
    def valeur(self) -> float:
        return super().valeur

    @valeur.setter
    def valeur_setter(self, valeur: float) -> None:
        return super().valeur_setter

    def coeffU(self) -> float:
        return complex(0)

    def coeffI(self) -> Complex:
        return complex(self.valeur)

    def coeffC(self, U: float, I: float) -> Complex:
#TODO fonction pour calculer le module d'un complexe
        return 0 #0 à changer avec module(self.coeffU)*U + module(self.coeffI)*I

if __name__ == "__main__":
    n1 = Noeud("n1", 0, 100)
    n2 = Noeud("n2", 100, 100)
    R1 = Resistance("R1", 100, n1, n2)
    
    #TEST NON FONCTIONNEL
    #c1 = R1.coeffI
    #c11 = float(sqrt(pow(c1.real)+pow(c1.imag)))
    #print(c1)