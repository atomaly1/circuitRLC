#from email.policy import default
import sys
from noeud import Noeud
from composant import Composant
from fil import Fil
from inductance import Inductance
from resistance import Resistance
from condensateur import Condensateur
from generateur_tension import GenerateurTension

class Circuit():
    def __init__(self, noeuds: list[Noeud], composants : list[Composant]):
        self._noeuds = noeuds
        self._composants = composants

    @property
    def noeuds(self) -> list[Noeud]:
        return self._noeuds

    @property
    def composants(self) -> list[Composant]:
        return self._composants

    # Construction de la chaine de caractère pour afficher le circuit
    def __str__(self): 
        buffer = ""
        buffer += f"Circuit courant : \nCircuit (\n"
        buffer += f"--------- noeuds :\n"
        for noeud in self.noeuds :
            buffer += f"{noeud}\n"
        buffer += f"--------- composants :\n" 
        for composant in self.composants :
            buffer += f"{composant}\n"
        buffer += f")\n"
        return buffer 

    # Retourne VRAI si le circuit n'est PAS vide, sinon retourne FAUX
    def _circuit_non_vide(self) -> bool :
        if len(self.noeuds) == 0 : return False
        else : return True

    # Retourne VRAI si le circuit possède des composants, sinon retourne FAUX
    def _circuit_sans_composants(self) -> bool :
        if len(self.composants) == 0 : return False
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
        
    # Renvoie l'ordonnée  maximale du circuit (ordonnée du noeud du circuit ayant la plus grande ordonnée). Retourne 0.0 si le circuit est vide (ne contient pas de noeuds)
    def max_y(self) -> float :
        max_y = 0.0
        if self._circuit_non_vide :
            max_y = self.noeuds[0].ny
            for noeud in self.noeuds:
                if noeud.ny > max_y:
                    max_y = noeud.ny   
        return max_y

    # Renvoie l'ordonnée minimale du circuit. Retourne 0.0 si le circuit est vide
    def min_y(self) -> float :
        min_y = 0.0
        if len(self.noeuds) != 0:
            min_y = self.noeuds[0].ny
            for noeud in self.noeuds:
                if noeud.ny < min_y:
                    min_y = noeud.ny   
        return min_y

    # Retourne vrai si un noeud est contenu dans le circuit, faux sinon
    # Soit le nom est déjà pris, soit les coordonnées sont déjà prises
    def _contien_noeud(self, noeud : Noeud) -> bool:
        for elmt in self.noeuds :
            if elmt.nom == noeud.nom : return True
            if elmt.nx == noeud.nx and elmt.ny == noeud.ny : return True
        return False

#TODO Retourne vrai si un composant est contenu dans le circuit, faux sinon
    # les coordonnées sont déjà prises ?
    def _contien_composant(self, composant : Composant) -> bool:
        for elmt in self.composants :
            if elmt.noeud_depart == composant.noeud_depart and elmt.noeud_arrivee == composant.noeud_arrivee : return True
        return False

    # Ajoute un nœud au circuit. Si le nœud appartient déjà au circuit : ▪ raise Exception("le noeud est déjà dans le circuit")
    def add_noeud(self, noeud : Noeud) -> None:
        if self._contien_noeud(noeud) :
            raise Exception("le noeud est déjà dans le circuit")
        else : self.noeuds.append(noeud)

    # Ajoute un composant au circuit. Si le nœud appartient déjà au circuit : ▪ raise Exception("le noeud est déjà dans le circuit")
    def add_composant(self, composant : Composant) -> None:
        if self._contien_composant(composant) :
            raise Exception("le composant est déjà dans le circuit")
        else : self.composants.append(composant)

    # Retire un nœud du circuit. Si le nœud n’appartient pas au circuit : ▪ raise Exception("le noeud n’est pas dans le circuit")
    def remove_noeud(self, noeud : Noeud) -> None:
        if not self._contien_noeud(noeud) :
            raise Exception("le noeud n’est pas dans le circuit")
        else : self.noeuds.remove(noeud)
        
    # Retire un composant du circuit. Si le nœud n’appartient pas au circuit : ▪ raise Exception("le noeud n’est pas dans le circuit")
    def remove_composant(self, composant : Composant) -> None:
        if not self._contien_composant(composant) :
            raise Exception("le composant n’est pas dans le circuit")
        else : self.composants.remove(composant)

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

    # méthode utilitaire pour la gestion du menu 
    def _choisi_composant(self) -> int:
        print("Taper le numéro du Composant à sélectionner :")
        for composant in self.composants :
            print(self.composants.index(composant)+1, ": [", composant, "]")
        print("0 : pour annuler la sélection")
        num_composant_choisi = int(input())
        if num_composant_choisi < 0 or num_composant_choisi > len(self.composants):
            raise Exception("choix non valide")
        return num_composant_choisi  

    # méthode utilitaire pour la gestion du menu
    def _choisi_type_composant(self) -> int:
        print("Choisir le type de composant :")
        print("1 : Résistance")
        print("2 : Condensateur")
        print("3 : Inductance")
        print("4 : Générateur de tension")
        print("5 : Fil")
        num_choisi = int(input())
        if num_choisi < 1 or num_choisi > 5:
            raise Exception("choix non valide")
        return num_choisi  

    @classmethod
    def create_circuit_test(cls) -> 'Circuit':
        circuit = Circuit([],[])
        n1 = Noeud("n1", 0, 0)
        n2 = Noeud("n2", 0, 100)
        n3 = Noeud("n3", 100, 100)
        n4 = Noeud("n4", 100, 0)
        circuit.add_noeud(n1)
        circuit.add_noeud(n2)
        circuit.add_noeud(n3)
        circuit.add_noeud(n4)

        gen = GenerateurTension(n1,n2,"G",10)
        r1 = Resistance(n2,n3,"R1",200)
        l1 = Inductance(n3,n4,"L1",0.01)
        r2 = Resistance(n4,n1,"R2",400)
        c1 = Condensateur(n3,n1,"C1",0.0001)
        circuit.add_composant(gen)
        circuit.add_composant(r1)
        circuit.add_composant(l1)
        circuit.add_composant(r2)
        circuit.add_composant(c1)
        return circuit

    # Permet la gestion du circuit par menu textuel 
    def menu_circuit(self) -> bool:

        print("1 : afficher le circuit")
        print("2 : ajouter un noeud")
        print("3 : supprimer un noeud")
        print("4 : trouver noeud le plus proche")
        print("5 : ajouter un composant")
        print("6 : supprimer un composant")
        print("0 : retour")
        print("votre choix ?")

        menu = input()

        if menu == '1':  # Afficher le circuit
            print("Circuit{\n---------- noeuds :")
            print(self)
            print("}") 

        elif menu == '2': # Ajouter un noeud
            new_noeud = Noeud.demande()
            print(new_noeud)
            self.add_noeud(new_noeud)
        
        elif menu == '3': # Supprimer un noeud
            if self._circuit_non_vide():
                index = self._choisi_noeud()
                if index != 0 :
                    self.remove_noeud(self.noeuds[index-1])
            else : print("Circuit vide")

        elif menu == '4' :  # Trouver noeud le plus proche
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

        elif menu == '5' : # Ajouter un composant
            print("Choisir le noeud de départ:\n")
            index_noeud_depart = self._choisi_noeud()
            noeud_depart = self.noeuds[index_noeud_depart - 1]
            print("Choisir le noeud d'arrivée:\n")
            index_noeud_arrivee = self._choisi_noeud()
            noeud_arrivee = self.noeuds[index_noeud_arrivee - 1]
            print("Choisir le type de composant:\n")

            match self._choisi_type_composant():
                case 1:
                    new_resistance = Resistance.demande(noeud_depart, noeud_arrivee)
                    self.add_composant(new_resistance)
                case 2:
                    new_condensateur = Condensateur.demande(noeud_depart, noeud_arrivee)
                    self.add_composant(new_condensateur)
                case 3:
                    new_inductance = Inductance.demande(noeud_depart, noeud_arrivee)
                    self.add_composant(new_inductance)
                case 4:
                    new_generateur = GenerateurTension.demande(noeud_depart, noeud_arrivee)
                    self.add_composant(new_generateur)
                case 5:
                    self.add_composant(Fil(noeud_depart, noeud_arrivee))
                case _:
                    raise Exception("problème ajouter un composant")

        elif menu == '6' : # Supprimer un composant
            if self._circuit_non_vide():
                index = self._choisi_composant()
                if index != 0 :
                    self.remove_composant(self.composants[index-1])
            else : print("Circuit sans composants")

        elif menu == '0' : # Retour
            return False 

        else :
            print("\nVeuillez entrer une réponse valide.\n")

        return True  


# à utiliser pour tester les fonctions
if __name__ == "__main__":

    circuit= Circuit([],[])

    while(True) : 
        
        print("1 : créer un circuit vide")
        print("2 : créer le circuit test du sujet")
        print("3 : gérer le circuit courant")
        print("0 : quitter")
        print("votre choix ?")

        menu = input()

        if menu == '1' :
            circuit = Circuit([],[])
            print(circuit)

        elif menu == '2' :
            circuit = Circuit.create_circuit_test()
            print(circuit)

        elif menu == '3' :
            while circuit.menu_circuit() :
                circuit.menu_circuit()

        elif menu == '0' :
            sys.exit(0)

        else : 
            print("\nVeuillez entrer une réponse valide.\n")
    
 
    

