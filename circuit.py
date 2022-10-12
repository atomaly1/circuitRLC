from noeud import Noeud

# TODO définir la classe CIRCUIT => attribut : liste de Noeuds 
class Circuit:
    def __init__(self, noeuds: list):
        self._noeuds = noeuds

    @property
    def noeuds(self) -> list:
        return self._noeuds

    def __str__(self):
        _str = ""
        for elmts in self.noeuds :
            _str += f"[{elmts}]\n"
        return _str 

# TODO définir méthode maxX :renvoie l’abscisse maximale du circuit (abscisse du noeud du circuit ayant la plus grande abscisse). Retourne 0.0 si le circuit est vide (ne contient pas de noeuds)
# TODO A tester :
    def maxX(self) -> float :
        maxX = 0.0
        if len(self._noeuds) == 0:
            pass
        else:
            for noeud in self._noeuds:
                if self._noeuds._nx > maxX:
                    maxX = self._noeuds._nx
        return maxX

# TODO definir méthode minX
# TODO Création En cours
    def minX(self) -> float :
        minX = 0.0
        if len(self.noeuds) == 0:
            pass
        else:
            for noeud in self.noeuds:
                if self.noeuds.nx > minX:
                    minX = self.noeuds.nx
        return minX

# TODO définir méthode maxY

# TODO définir méthode minY

# TODO définir méthode  noeud_le_plus_proche : renvoie le noeud le plus proche du point de coordonnées px,py. Signale une erreur si le circuit ne contient pas de noeud par :
#   ▪ raise Exception("Circuit vide")

# TODO définir méthode contienNoeud : retourne vrai si un noeud est contenu dans le circuit, faux sinon
# TODO à tester -> marche pas
    def contienNoeud(self, noeud : Noeud) -> bool:
        for elmts in self.noeuds :
            if elmts == noeud : return True
        return False


# TODO définir méthode addNoeud : ajoute un nœud au circuit. Si le nœud appartient déjà au circuit :
#   ▪ raise Exception("le noeud est déjà dans le circuit")
# TODO à tester
    def addNoeud(self, noeud : Noeud) -> None:
        if self.contienNoeud(noeud) :
            raise Exception("le noeud est déjà dans le circuit")
        else : self.noeuds.append(noeud)
        

# TODO définir méthode removeNoeud : retire un nœud du circuit. Si le nœud n’appartient pas au circuit :
#   ▪ raise Exception("le noeud n’est pas dans le circuit")
# TODO à tester
    def removeNoeud(self, noeud : Noeud) -> None:
        if not self.contienNoeud(noeud) :
            raise Exception("le noeud n’est pas dans le circuit")
        else : self.noeuds.remove(noeud)

# TODO gérer exception si Noeud non trouvé
# TODO à tester
    def choisiNoeud(self) -> Noeud:
        print(self)
        print("Taper le nom du Noeud à sélectionner :")
        nomNoeudChoisi = input()
        for noeud in self.noeuds :
            if noeud.nom == nomNoeudChoisi : return noeud
        
'''
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
                return True
'''
if __name__ == "__main__":
    noeud1 = Noeud("n1",1.0,2.0)
    noeud2 = Noeud("n2",3.0,4.0)
    circuit = Circuit(noeud1)

    print("Test fonction contienNoeud:")
    if circuit.contienNoeud(noeud1) :
        print("True")
    else : print("False")
    if circuit.contienNoeud(noeud2) :
        print("True")
    else : print("False")