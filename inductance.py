from composant import Composant
from noeud import Noeud

class Inductance(Composant):
    
    def __init__(self, noeud_depart: Noeud, noeud_arrivee: Noeud, nom: str, l: float) -> None:
        super().__init__(noeud_depart, noeud_arrivee)
        self._nom = nom
        self._l = l

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, nom: str) -> None:
        self._nom = nom

    @property
    def l(self) -> float:
        return self._l

    @l.setter
    def l(self, l: float) -> None:
        self._l = l

    def __str__(self) -> str:
        return f"[Inductance {self.nom} ({self.noeud_depart.nom} -> {self.noeud_arrivee.nom}) : inductance {self.l} Henry]"

    def coeff_u(self) -> complex:
        return 1

    def coeff_i(self) -> complex:
        return -1j*self.l*Composant.w

    def coeff_c(self) -> complex:
        return 0

    @classmethod
    def demande(cls, noeud_depart : Noeud, noeud_arrivee : Noeud) -> 'Inductance':
        nom = input("Nom :\n")
        valeur = float(input("Inductance (en Henry) :\n"))
        return Inductance(noeud_depart, noeud_arrivee, nom, valeur)

# Test de la classe Inductance
if __name__ == "__main__":
    n3 = Noeud("n3", 100, 100)
    print(n3)
    n4 = Noeud("n4", 100, 0)
    print(n4)
    l1 = Inductance(n3, n4, "L1", 0.01)
    print(l1)

    # Test coeff_u
    cu = l1.coeff_u()
    print(cu)
    print(type(cu))

    # Test coeff_i
    ci = l1.coeff_i()
    print(ci)
    print(type(ci))

    # Test coeff_c
    cc = l1.coeff_c()
    print(cc)
    print(type(cc))