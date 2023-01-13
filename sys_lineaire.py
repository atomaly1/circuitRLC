import numpy as np
from circuit import Circuit
from composant import Composant



"""
n nb de noeuds
c nb de composants
Loi d'Ohm => Pour chaque composant : a*U + b*I = c => c équations
Loi des noeuds => Somme des I = 0 => n-1 équations
Loi des mailles => 2*c - c - n-1 = c-n-1 équations
"""

class SysLineaire() : # systeme lineaire de la forme ax = b
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

    def _count_dipoles(circuit : Circuit) -> int :
        counter = 0
        for composant in circuit.composants:
            if str(type(composant)) != "<class 'fil.Fil'>":
                counter += 1
        return counter

    @classmethod
    def create_sys_lin(cls, circuit : Circuit, omega : float) -> 'SysLineaire':

        # Troubleshooting
        # TODO : vérifier que le circuit sois fermé

        nb_composants = len(circuit.composants)
        nb_inconnus = nb_composants * 2
        index_ligne = 0

        # On cherche a écrire le système sous la forme matrcielle : A * X = B
        mat_a = np.zeros((nb_inconnus,nb_inconnus), dtype=complex)
        mat_b = np.zeros(nb_inconnus, dtype=complex)

        '''
        for row_index, row in enumerate(mat_a):
            for col_index, item in enumerate(row):
                print(mat_a[row_index][col_index])
        '''

        # Equations d'impédances (sans Fils)
        for i in range(nb_composants):
            mat_a[i, 2*i] = circuit.composants[i].coeff_u()
            mat_a[i, 2*i+1] = circuit.composants[i].coeff_i()
            mat_b[i] = circuit.composants[i].coeff_c()
            index_ligne += 1
                
        # Loi des noeuds (sans Fils)
        nb_noeuds = len(circuit.noeuds)

        for i in range(nb_noeuds - 1) :
            for j in range(nb_composants - 1) :
                if circuit.noeuds[i] == circuit.composants[j].noeud_depart:
                    mat_a[index_ligne, 2*j+1] = 1
                elif circuit.noeuds[i] == circuit.composants[j].noeud_arrivee:
                    mat_a[index_ligne, 2*j+1] = -1
            index_ligne += 1

        # Loi des mailles simplifiée

        # Déclaration des variables
        temp_composants = circuit.composants.copy()
        maille = []
        liste_mailles = []
        noeud_base = circuit.noeuds[2]
        noeud_courant = noeud_base

        # Déclaration des fonctions
        def liste_composants_ayant_noeud_départ(snoeud_depart, scircuit) -> list:
            liste_composants =[]            
            for composant in scircuit.composants :
                if composant.noeud_depart == snoeud_depart :
                    liste_composants.append(composant)
            return liste_composants


        def ajouter_composant_dans_maille(snoeud_courant) : # Ajoute un composant dans la maille et retourne le nouveau noeud courant
            for composant in temp_composants :
                if snoeud_courant == composant.noeud_depart :
                    maille.append(composant)
                    temp_composants.remove(composant)
                    snoeud_courant = composant.noeud_arrivee
                    return snoeud_courant

        def ajouter_maille_dans_circuit(smaille) :
            for composant in smaille :
                for i in range(nb_composants - 1) :
                    if composant == circuit.composants[i] :
                        if str(type(composant))  == "<class 'generateur_tension.GenerateurTension'>" :
                            mat_a[index_ligne, 2*i] = 1
                        else : 
                            mat_a[index_ligne, 2*i] = -1

        noeud_courant = ajouter_composant_dans_maille(noeud_courant)
        while noeud_courant != noeud_base :
            noeud_courant = ajouter_composant_dans_maille(noeud_courant) 
        # TODO check si la maille est une permutation, si oui exploration d'une nouvelle maille

        print(maille)
        liste_mailles.append(maille)
        # Ajoute la maille à la matrice
        ajouter_maille_dans_circuit(maille)
        index_ligne += 1
                        
                    
             
        '''
        for i in range(0,nb_noeuds-1) :
            noeud_base = circuit.noeuds[i]
            noeud_courant = ajouter_dans_maille(noeud_courant)
            #noeud_courant = ajouter_dans_maille(noeud_courant)
        '''         

        return SysLineaire(mat_a, mat_b)

def sys_lin_exemple(omega : float) -> SysLineaire:

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
    mat_a[i,2*3] = complex(1,0)
    mat_a[i,2*3+1] = complex(-400,0)
    i += 1
    # condensateur C1 : U1 - 1/(j.C1.omega).I1 = 0
    # 4: [ 0  0  0  0  0  0  0  0  1  -1/j.0.0001.omega ]  [ 0 ]
    mat_a[i,2*4] = complex(1,0)
    mat_a[i,2*4+1] = -1/(1j*0.0001*omega)
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

    return SysLineaire(mat_a, mat_b)

if __name__ == '__main__':
    omega = 100
    
    """
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
    """
   
    
    circuit = Circuit.create_circuit_test()
    print(circuit)
    lin_sys = SysLineaire.create_sys_lin(circuit,omega)
    print(lin_sys)
    
    '''
    sol = lin_sys.solve()

    print("solution : ")
    
    for elmt in sol:
        print("[", end='')
        print(round(cmath.polar(elmt)[0], 2),end='')
        print(", ", end='')
        print(round(cmath.polar(elmt)[1], 2), end='')
        print("]")

    '''
