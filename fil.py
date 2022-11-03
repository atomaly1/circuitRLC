from composant import Composant
from noeud import Noeud

class Fil(Composant):
    
    def __init__(self, noeud_depart: Noeud, noeud_arrivee: Noeud) -> None:
        super().__init__(noeud_depart, noeud_arrivee)

    def __str__(self) -> str:
        return f"[Fil ({self.noeud_depart.nom} -> {self.noeud_arrivee.nom})]"

    def coeff_u(self) -> complex:
        return 0

    def coeff_i(self) -> complex:
        return 0

    def coeff_c(self) -> complex:
        return 0

# Test de la classe Fil
if __name__ == "__main__":
    n1 = Noeud("n1", 0, 0)
    print(n1)
    n2 = Noeud("n2", 0, 100)
    print(n2)
    philibert = Fil(n1, n2)
    print(philibert)

    # Test coeff_u
    cu = philibert.coeff_u()
    print(cu)
    print(type(cu))

    # Test coeff_i
    ci = philibert.coeff_i()
    print(ci)
    print(type(ci))

    # Test coeff_c
    cc = philibert.coeff_c()
    print(cc)
    print(type(cc))