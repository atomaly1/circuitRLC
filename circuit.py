import sys
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
        str = ""
        for noeud in self.noeuds :
            str += f"{noeud}\n"
        return str 

    # Retourne VRAI si le circuit n'est PAS vide, sinon retourne FAUX
    def _circuit_non_vide(self) -> bool :
        if len(self.noeuds) == 0 : return False
        else : return True

    # Renvoie l’abscisse maximale du circuit (abscisse du noeud du circuit ayant la plus grande abscisse). Retourne 0.0 si le circuit est vide (ne contient pas de noeuds)
    def max_x(self) -> float :
        max_x = 0.0
        if self._circuit_non_vide :
            max_x = self.noeuds[0].nx
            for noeud in self.noeuds:
                if noeud.nx > max_x:
                    max_x = noeud.nx   
        return max_x

    # Renvoie l’abscisse minimale du circuit. Retourne 0.0 si le circuit est vide
    def min_x(self) -> float :
        min_x = 0.0
        if len(self.noeuds) != 0:
            min_x = self.noeuds[0].nx
            for noeud in self.noeuds:
                if noeud.nx < min_x:
                    min_x = noeud.nx   
        return min_x

# TODO définir méthode max_y : Analogue à max_x


# TODO définir méthode min_y : Analogue à max_x

    # Retourne vrai si un noeud est contenu dans le circuit, faux sinon
    # Soit le nom est déjà pris, soit les coordonnées sont déjà prises
    def contien_noeud(self, noeud : Noeud) -> bool:
        for elmt in self.noeuds :
            if elmt.nom == noeud.nom : return True
            if elmt.nx == noeud.nx and elmt.ny == noeud.ny : return True
        return False

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


    # méthode utilitaire pour la gestion du menu 
    def _choisi_noeud(self) -> int:
        print("Taper le numéro du Noeud à sélectionner :")
        for noeud in self.noeuds :
            print(self.noeuds.index(noeud)+1, ": [", noeud, "]")
        print("0 : pour annuler la sélection")
        num_noeud_choisi = int(input())
        if num_noeud_choisi < 0 or num_noeud_choisi > len(self.noeuds):
            raise Exception("choix non valide")
        return num_noeud_choisi     

    # Permet la gestion du circuit par menu textuel 
    def menu(self) -> None:

        print("1 : afficher le circuit")
        print("2 : ajouter un noeud")
        print("3 : supprimer un noeud")
        print("4 : trouver noeud le plus proche")
        print("0 : quitter")
        print("votre choix ?")

        menu = input()

        match menu:
            case '1': # Afficher le circuit
                print("Circuit{\n---------- noeuds :")
                print(self)
                print("}") 

            case '2': # Ajouter un noeud
                new_noeud = Noeud.demande()
                print(new_noeud)
                self.add_noeud(new_noeud)

            case '3': # Supprimer un noeud
                if self._circuit_non_vide() :
                    index = self._choisi_noeud()
                    if index != 0 :
                        self.remove_noeud(self.noeuds[index-1])
                else : print("Circuit vide")
                
            case '4': # Trouver noeud le plus proche
                # renvoyer le noeud pour lequel 'noeud.distance()' est le plus petit
                if self._circuit_non_vide() :
                    px = float(input("abscisse : "))
                    py = float(input("ordonnée : "))
                    # cherche le noeud le plus proche du circuit
                    noeud_temp = self.noeuds[0] 
                    for noeud in self.noeuds:
                        if noeud.distance(px,py) < noeud_temp.distance(px,py):
                            noeud_temp = noeud
                    print("Le noeud le plus proche de (", px, ",", py, ") est :", noeud_temp)
                else : print("Circuit vide")

            case '0': # Quitter
                sys.exit(0)

            case _:
                print("\nVeuillez entrer une réponse valide.\n")

# à utiliser pour tester les fonctions
if __name__ == "__main__":

    circuit = Circuit([])
    n1 = Noeud("n1", 0, 100)
    n2 = Noeud("n2", 100, 0)
    circuit.add_noeud(n1)
    circuit.add_noeud(n2)

    while(True) : circuit.menu()
    
 
    

