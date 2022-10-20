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
    # def bordel(Cu, Ci, Cc) -> question pour le prof
    #   Cu.U + Ci.I = Cc 
    #   return C Koa se bordel ?

    def coeff_u(self) -> Complex:
        pass

    def coeff_i(self) -> Complex:
        pass

    def coeff_c(self, U: float, I: float) -> Complex:
        pass 

if __name__ == "__main__":
    n1 = Noeud("n1", 0, 100)
    print(n1)
    n2 = Noeud("n2", 100, 100)
    print(n2)
    r1 = Resistance(n1, n2, "R1", 200)
    print(r1)
    
    #TEST NON FONCTIONNEL
    #c1 = R1.coeffI
    #c11 = float(sqrt(pow(c1.real)+pow(c1.imag)))
    #print(c1)