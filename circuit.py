# CLASSE CIRCUIT

# TODO définir la classe CIRCUIT => ensemble de Noeuds = attribut noeuds de type list

# TODO définir l'attribut noeuds avec @property et __init__ (voir noeud.py pour un exemple)

# TODO définir la méthode __str__

# TODO définir méthode maxX :renvoie l’abscisse maximale du circuit (abscisse du noeud du circuit ayant la plus grande abscisse). Retourne 0.0 si le circuit est vide (ne contient pas de noeuds)

# TODO definir méthode minX

# TODO définir méthode maxY

# TODO définir méthode minY

# TODO définir méthode  noeud_le_plus_proche : renvoie le noeud le plus proche du point de coordonnées px,py. Signale une erreur si le circuit ne contient pas de noeud par :
#   ▪ raise Exception("Circuit vide")

# TODO définir méthode contienNoeud

# TODO définir méthode addNoeud : ajoute un nœud au circuit. Si le nœud appartient déjà au circuit :
#   ▪ raise Exception("le noeud est déjà dans le circuit")

# TODO définir méthode removeNoeud : retire un nœud du circuit. Si le nœud n’appartient pas au circuit :
#   ▪ raise Exception("le noeud n’est pas dans le circuit")
 
# TODO définir méthode menu : permet la gestion du circuit par menu textuel : voir ci-dessous un exemple d’interaction :
#   ▪ pour la suppression d’un nœud, vous aurez sans doute besoin de la méthode utilitaire choisiNoeud qui permet à l’utilisateur de choisir un nœud existant dans le circuit