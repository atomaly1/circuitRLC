from composant import Composant
from noeud import Noeud
from numbers import Complex

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
        return f"[Resistance {self.nom} ({self.noeud_depart} -> {self.noeud_arrivee}) : {self.r} Ohm]"

# TODO
    # 
    #   coeff_u.U + coeff_i.I = coeff_c
    """ {2.x0 + 3.x1 = 4
        {5.x0 + 6.x1 = 7

        est équivalent à
    
        (2 3) . (x0)   (4)
        (5 6)   (x1) = (7) """


    def coeff_u(self) -> Complex:
        pass

    def coeff_i(self) -> Complex:
        pass

    def coeff_c(self, U: float, I: float) -> Complex:
        pass 

if __name__ == "__main__":
    n2 = Noeud("n2", 0, 100)
    print(n2)
    n3 = Noeud("n3", 100, 100)
    print(n3)
    r1 = Resistance(n2, n3, "R1", 200)
    print(r1)
    
    #TEST NON FONCTIONNEL
    #c1 = R1.coeffI
    #c11 = float(sqrt(pow(c1.real)+pow(c1.imag)))
    #print(c1)