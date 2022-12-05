import numpy as np
from typing import List
import sys

"""
Nous partons du circuit exemple :
circuit courant :
Circuit{
---------- noeuds :
[Noeud n1 : 0,0]
[Noeud n2 : 0,100]
[Noeud n3 : 100,100]
[Noeud n4 : 100,0]
---------- composants :
[0 : GenerateurTension G (n1 -> n2) : fem 10 Volt
[1 : Resistance R1 (n2 -> n3) : 200 Ohm]
[2 : Inductance L1 (n3 -> n4) : inductance 0.01 Henry]
[3 : Resistance R2 (n4 -> n1) : 400 Ohm]
[4 : Condensateur C1 (n3 -> n1) : capacite 0.0001 Farad]
"""

"""
Loi d'Ohm => Pour chaque composant : a*V + b*I = c
Loi des noeuds => Somme des I = 0
Loi des mailles

0: [ a0  0  0  0 b0  0  0  0  0 ]   [ V0 ]   [ c0 ]
1: [  0 a1  0  0  0 b1  0  0  0 ]   [ V1 ]   [ c1 ]
2: [  0  0 a2  0  0  0 b2  0  0 ]   [ V2 ]   [ c2 ]
3: [  0  0  0 a3  0  0  0 b3  0 ]   [ V3 ]   [ c3 ]
4: [  0  0  0  0 a4  0  0  0 b4 ] * [ V4 ] = [ c4 ]
5: [                            ]   [ I0 ]   [    ]
6: [                            ]   [ I1 ]   [    ]
7: [                            ]   [ I2 ]   [    ]
8: [                            ]   [ I3 ]   [    ]
9: [                            ]   [ I4 ]   [    ]
"""

class Sys_lineaire() : # systeme lineaire de la forme ax = b
    def __init__(self, mat_a : list[list[complex]], mat_b : list[complex] ) -> None : 
        self._mat_a = mat_a
        self._mat_b = mat_b

    @property
    def mat_a(self) -> list[list[complex]]:
        return self._mat_a

    @property
    def mat_b(self) -> list[complex]:
        return self._mat_b

    def __str__(self) -> str :
        buffer = "Matrice : \n"
        buffer += f"{self._mat_a}"
        buffer += "\nsecond membre : "
        buffer += f"{self._mat_b}"
        return buffer

    def solve(self) -> list[complex] : 
        return np.linalg.solve(self._mat_a, self._mat_b)