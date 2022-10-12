# TODO : import all classes necessary with (example): 

import sys
from circuit import Circuit
from noeud import Noeud

# TODO faire la strucuture du programme (voir sujet du TP pour les outputs)

if __name__ == '__main__':
    
    menu = 1 # TODO Amelioration : liste/enumeration pour le menuing
    circuit = Circuit([])
    while menu != 0:

        print("1 : afficher le circuit")
        print("2 : ajouter un noeud")
        print("3 : supprimer un noeud")
        print("4 : trouver noeud le plus proche")
        print("0 : quitter")
        print("votre choix ?")

        menu = input()

        match menu:

            case '1': # afficher le circuit
                print("Circuit{\n")
                print("---------- noeuds :\n")
                # TODO ajouter fonction affichage des noeuds dans 'circuit.py'
                print(circuit)
                print("}") 
                pass

            case '2': # ajouter un noeud
                noeud1 = Noeud.demande() # TODO à ajouter à une liste dans 'circuit.py'
                print(noeud1)
                # TODO ajouter le noeud au circuit
                circuit.addNoeud(noeud1)
                pass

            case '3': # supprimer un noeud
                # TODO supprimer un noeud à partir d'un menu de séléction des noeuds
                pass
                
            case '4': # trouver noeud le plus proche
                # TODO renvoyer le noeud pour lequel 'noeud.distance()' est le plus petit
                pass

            case '0': # quitter
                sys.exit(0)

            case _:
                print("\nVeuillez entrer une réponse valide.\n")