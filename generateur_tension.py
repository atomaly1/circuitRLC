from composant import Composant
from noeud import Noeud

class GenerateurTension(Composant):
    
    def __init__(self, noeud_depart: Noeud, noeud_arrivee: Noeud, nom: str, fem: float) -> None:
        super().__init__(noeud_depart, noeud_arrivee)
        self._nom = nom
        self._fem = fem

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, nom: str) -> None:
        self._nom = nom

    @property
    def fem(self) -> float:
        return self._fem

    @fem.setter
    def fem(self, fem: float) -> None:
        self._fem = fem

    def __str__(self) -> str:
        return f"[GenerateurTension {self.nom} ({self.noeud_depart.nom} -> {self.noeud_arrivee.nom}) : fem {self.fem} Volt]"

    def coeff_u(self) -> complex:
        return 1

    def coeff_i(self) -> complex:
        return 0

    def coeff_c(self) -> complex:
        return -self.fem

# Test de la classe GenerateurTension
if __name__ == "__main__":
    n1 = Noeud("n1", 0, 0)
    print(n1)
    n2 = Noeud("n2", 0, 100)
    print(n2)
    g1 = GenerateurTension(n1, n2, "G", 10)
    print(g1)

    # Test coeff_u
    cu = g1.coeff_u()
    print(cu)
    print(type(cu))

    # Test coeff_i
    ci = g1.coeff_i()
    print(ci)
    print(type(ci))

    # Test coeff_c
    cc = g1.coeff_c()
    print(cc)
    print(type(cc))