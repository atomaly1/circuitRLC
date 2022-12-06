import cmath
import numpy as np
from typing import List
import sys



"""
Loi d'Ohm => Pour chaque composant : a*U + b*I = c
Loi des noeuds => Somme des I = 0
Loi des mailles

0: [ a0 b0  0  0  0  0  0  0  0  0 ]   [ U0 ]   [ c0 ]
1: [  0  0 a1 b1  0  0  0  0  0  0 ]   [ I0 ]   [ c1 ]
2: [  0  0  0  0 a2 b2  0  0  0  0 ]   [ U1 ]   [ c2 ]
3: [  0  0  0  0  0  0 a3 b3  0  0 ]   [ I1 ]   [ c3 ]
4: [  0  0  0  0  0  0  0  0 a4 b4 ] * [ U2 ] = [ c4 ]
5: [                               ]   [ I2 ]   [    ]
6: [                               ]   [ U3 ]   [    ]
7: [                               ]   [ I3 ]   [    ]
8: [                               ]   [ U4 ]   [    ]
9: [                               ]   [ I4 ]   [    ]
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
        
        return np.around(np.linalg.solve(self._mat_a, self._mat_b),2)

def sys_lin_exemple(omega : float) -> Sys_lineaire:

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

    nbr_composants = 5
    nbr_inconnus = nbr_composants * 2

    mat_a = np.zeros((nbr_inconnus,nbr_inconnus), dtype=complex)
    mat_b = np.zeros(nbr_inconnus, dtype=complex)

    i = 0

    #----------- loi d'Ohm
    # une équation par composant

    # générateur : 1.U0 = fem + 0.I0 <=> 1.U0 - 0.I0 = fem (on considère le déphase nul aux bornes du générateur)
    # avec fem = 10 => 1.U0 - 0.I0 = 10
    # 0: [ 1  0  0  0  0  0  0  0  0  0 ]  [ 10 ]
    mat_a[i, 2*0] = complex(1,0)
    mat_b[i] = complex(10,0)
    i += 1
    # resistance R1 : 1.U1 - 200.I1 = 0
    # 1: [ 0  0  1  -200  0  0  0  0  0  0 ]  [ 0 ]
    mat_a[i,2*1] = complex(1,0)
    mat_a[i,2*1+1] = complex(-200,0)
    i += 1
    # inductance L1 : U1 - j.L1.omega.I1 = 0
    # 2: [ 0  0  0  0  1  -j.0.01.omega  0  0  0  0 ]  [ 0 ]
    mat_a[i,2*2] = complex(1,0)
    mat_a[i,2*2+1] = -1j*0.01*omega
    i += 1
    # resistance R2 : U1 - R2.I1 = 0
    # 3: [ 0  0  0  0  0  0  1  -400  0  0 ]  [ 0 ]
    mat_a[i,3*2] = complex(1,0)
    mat_a[i,3*2+1] = complex(-400,0)
    i += 1
    # condensateur C1 : U1 - 1/(j.C1.omega).I1 = 0
    # 4: [ 0  0  0  0  0  0  0  0  1  -1/j.0.0001.omega ]  [ 0 ]
    mat_a[i,4*2] = complex(1,0)
    mat_a[i,4*2+1] = -1/(1j*0.0001*omega)
    i += 1

    #----------- loi des noeuds
    # il y a 4 noeud, cela donne 3 equations
    # noeud 1 : I0 - I4 - I3 = 0
    # 5: [ 0  1  0  0  0  0  0  -1  0  -1 ]  [ 0 ]
    mat_a[i,2*0+1] = complex(1,0)
    mat_a[i,2*4+1] = complex(-1,0)
    mat_a[i,2*3+1] = complex(-1,0)
    i += 1
    # noeud 2 : - I0 + I1 = 0
    # 6: [ 0  -1  0  1  0  0  0  0  0  0 ]  [ 0 ]
    mat_a[i,2*0+1] = complex(-1,0)
    mat_a[i,2*1+1] = complex(1,0)
    i += 1
    # noeud 3 : -I1 + I4 + I2 = 0
    # 7: [ 0  0  0  -1  0  1  0  0  0  1 ]  [ 0 ]
    mat_a[i,2*1+1] = complex(-1,0)
    mat_a[i,2*4+1] = complex(1,0)
    mat_a[i,2*2+1] = complex(1,0)
    i += 1

    #-------------- loi des mailles
    # à partir de la base de maille :
    # on représente les maille par un vecteur de même taille que le nombre de composant
    # la composante i du vecteur vaut 1 si le composant i appartient à la maille, 0 sinon
    # exemple la maille [1,1,0,0,1] est la maille G-R1-C1
    # la somme des tensions est nulle (en faisant attention au signes)
    #  maille 1 : G-R1-C1 = [1,1,0,0,1]
    mat_a[i,2*0] = complex(1,0)
    mat_a[i,2*1] = complex(-1,0)
    mat_a[i,2*4] = complex(-1,0)
    i += 1
    #  maille 1 : L1-R2-C1 = [0,0,1,1,1]
    mat_a[i,2*2] = complex(1,0)
    mat_a[i,2*3] = complex(1,0)
    mat_a[i,2*4] = complex(-1,0)
    i += 1

    return Sys_lineaire(mat_a, mat_b)

if __name__ == '__main__':
    sys = sys_lin_exemple(100)
    print(sys)
    sol = sys.solve()

    print("solution : ")
    
    for elmt in sol:
        print("[", end='')
        print(round(cmath.polar(elmt)[0], 2),end='')
        print(", ", end='')
        print(round(cmath.polar(elmt)[1], 2), end='')
        print("]")

