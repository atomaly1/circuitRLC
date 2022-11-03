from composant import Composant
from noeud import Noeud

class Resistance(Composant):
    
    def __init__(self, noeud_depart: Noeud, noeud_arrivee: Noeud, nom: str, r: float) -> None:
        super().__init__(noeud_depart, noeud_arrivee)
        self._nom = nom
        self._r = r

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, nom: str) -> None:
        self._nom = nom

    @property
    def r(self) -> float:
        return self._r

    @r.setter
    def r(self, r: float) -> None:
        self._r = r

    def __str__(self) -> str:
        return f"[Resistance {self.nom} ({self.noeud_depart.nom} -> {self.noeud_arrivee.nom}) : {self.r} Ohm]"

    #   coeff_u.U + coeff_i.I = coeff_c
    """ {2.x0 + 3.x1 = 4
        {5.x0 + 6.x1 = 7

        est équivalent à
    
        (2 3) . (x0)   (4)
        (5 6)   (x1) = (7) """

    def coeff_u(self) -> complex:
        #coeff_u = complex(1,0)     #Force le type 'complex' sur la variable (cast)
        #return coeff_u
        return 1

    def coeff_i(self) -> complex:
        return -self.r

    def coeff_c(self) -> complex:
        return 0

# Test de la classe Resistance
if __name__ == "__main__":
    n2 = Noeud("n2", 0, 100)
    print(n2)
    n3 = Noeud("n3", 100, 100)
    print(n3)
    r1 = Resistance(n2, n3, "R1", 200)
    print(r1)

    # Test coeff_u
    cu = r1.coeff_u()
    print(cu)
    print(type(cu))

    # Test coeff_i
    ci = r1.coeff_i()
    print(ci)
    print(type(ci))

    # Test coeff_c
    cc = r1.coeff_c()
    print(cc)
    print(type(cc))