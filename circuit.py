from noeud import Noeud

# TODO définir la classe CIRCUIT => attribut : liste de Noeuds 
class Circuit:
    def __init__(self, noeuds: list):
        self._noeuds = noeuds

    @property
    def noeuds(self) -> list:
        return self._noeuds

    # Construction de la chaine de caractère pour afficher le circuit
    def __str__(self): 
        _str = ""
        for elmts in self.noeuds :
            _str += f"[{elmts}]\n"
        return _str 

# TODO définir méthode max_x :renvoie l’abscisse maximale du circuit (abscisse du noeud du circuit ayant la plus grande abscisse). Retourne 0.0 si le circuit est vide (ne contient pas de noeuds)

# TODO definir méthode min_x : Analogue à max_x
# TODO Création En cours
    def min_x(self) -> float :
        min_x = 0.0
        if len(self.noeuds) != 0:
            for noeud in self.noeuds:
                if self.noeuds.nx > min_x:
                    min_x = self.noeuds.nx   
        return min_x

# TODO définir méthode max_y : Analogue à max_x


# TODO définir méthode min_y : Analogue à max_x


    # Renvoie le noeud le plus proche du point de coordonnées px,py. Signale une erreur si le circuit ne contient pas de noeud par : ▪ raise Exception("Circuit vide")
    def noeud_le_plus_proche(self, px : float, py : float) -> Noeud :
        if len(self.noeuds) != 0 :
            noeud_proche = self.noeuds[0]
            for noeud in self.noeuds :
                if noeud.distance(px,py) < noeud_proche.distance(px,py) : 
                    noeud_proche = noeud
            return noeud_proche     
        else : raise Exception("Circuit vide")

    # Retourne vrai si un noeud est contenu dans le circuit, faux sinon
    def contien_noeud(self, noeud : Noeud) -> bool:
        if noeud in self.noeuds :
            return True
        else: return False

    # Ajoute un nœud au circuit. Si le nœud appartient déjà au circuit : ▪ raise Exception("le noeud est déjà dans le circuit")
    def add_noeud(self, noeud : Noeud) -> None:
        if self.contien_noeud(noeud) :
            raise Exception("le noeud est déjà dans le circuit")
        else : self.noeuds.append(noeud)
        
    # Retire un nœud du circuit. Si le nœud n’appartient pas au circuit : ▪ raise Exception("le noeud n’est pas dans le circuit")
    def remove_noeud(self, noeud : Noeud) -> None:
        if not self.contien_noeud(noeud) :
            raise Exception("le noeud n’est pas dans le circuit")
        else : self.noeuds.remove(noeud)

# TODO méthode utilitaire pour la gestion du menu
# TODO gérer exception si Noeud non trouvé
# TODO à tester
    def choisi_noeud(self) -> Noeud:
        print(self)
        print("Taper le nom du Noeud à sélectionner :")
        nom_noeud_choisi = input()
        for noeud in self.noeuds :
            if noeud.nom == nom_noeud_choisi : return noeud
        
'''En cours...
# TODO définir méthode menu : permet la gestion du circuit par menu textuel : voir ci-dessous un exemple d’interaction :
#   ▪ pour la suppression d’un nœud, vous aurez sans doute besoin de la méthode utilitaire choisiNoeud qui permet à l’utilisateur de choisir un nœud existant dans le circuit
    def menu(self) -> bool:

        print("1 : afficher le circuit")
        print("2 : ajouter un noeud")
        print("3 : supprimer un noeud")
        print("4 : trouver noeud le plus proche")
        print("0 : quitter")
        print("votre choix ?")

        input = input()

        match input:
            case '1': # afficher le circuit
                print("Circuit{")
                print("---------- noeuds :")
                # TODO ajouter fonction affichage des noeuds dans 'circuit.py'
                print(self)
                print("}") 
                return True

            case '2': # ajouter un noeud
                newNoeud = Noeud.demande()
                print(newNoeud)
                # TODO ajouter le noeud au circuit
                self.addNoeud(newNoeud)
                return True

            case '3': # supprimer un noeud
                # TODO supprimer un noeud à partir d'un menu de séléction des noeuds
                removeNoeud(choisiNoeud())
                return True
                
            case '4': # trouver noeud le plus proche
                # TODO renvoyer le noeud pour lequel 'noeud.distance()' est le plus petit
                return True

            case '0': # quitter
                return False

            case _:
                print("\nVeuillez entrer une réponse valide.\n")
                return True'''

# à utiliser pour tester les fonctions
if __name__ == "__main__":
    noeud1 = Noeud("n1",1.0,2.0)
    noeud2 = Noeud("n2",3.0,4.0)
    circuit = Circuit([])
    
    circuit.add_noeud(noeud1)
    circuit.add_noeud(noeud2)
    print(circuit.noeud_le_plus_proche(3.0,3.0))
