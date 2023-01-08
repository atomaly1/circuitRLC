from composant import Composant
from noeud import Noeud

class Condensateur(Composant):
    
    def __init__(self, noeud_depart: Noeud, noeud_arrivee: Noeud, nom: str, c: float) -> None:
        super().__init__(noeud_depart, noeud_arrivee)
        self._nom = nom
        self._c = c

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, nom: str) -> None:
        self._nom = nom

    @property
    def c(self) -> float:
        return self._c

    @c.setter
    def c(self, c: float) -> None:
        self._c = c

    def __str__(self) -> str:
        return f"[Condensateur {self.nom} ({self.noeud_depart.nom} -> {self.noeud_arrivee.nom}) : condensateur {self.c} Farad]"

    def coeff_u(self) -> complex:
        return 1

    def coeff_i(self) -> complex:
        return -1/(1j*self.c*Composant.w)

    def coeff_c(self) -> complex:
        return 0

    @classmethod
    def demande(cls, noeud_depart : Noeud, noeud_arrivee : Noeud) -> 'Condensateur':
        nom = input("Nom :\n")
        valeur = float(input("Capacité (en Farad) :\n"))
        return Condensateur(noeud_depart, noeud_arrivee, nom, valeur)

# Test de la classe Condensateur
if __name__ == "__main__":
    n3 = Noeud("n3", 100, 100)
    print(n3)
    n4 = Noeud("n4", 100, 0)
    print(n4)
    c1 = Condensateur(n3, n4, "C1", 0.01)
    print(c1)

    # Test coeff_u
    cu = c1.coeff_u()
    print(cu)
    print(type(cu))

    # Test coeff_i
    ci = c1.coeff_i()
    print(ci)
    print(type(ci))

    # Test coeff_c
    cc = c1.coeff_c()
    print(cc)
    print(type(cc))