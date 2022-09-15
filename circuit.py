# pour l’instant, un circuit est défini uniquement comme un ensemble de noeuds (nous nous occuperons des composants plus tard)
# ◦ Nous décidons de conserver l’ensemble des noeuds d’un circuit dans un attribut noeuds de type list. Définir l’attribut correspondant (avec @property et __init__)
# ◦ On ne changera pas d’un coup toute la liste des noeuds. On ne défini donc pas de « setter ». Comme une liste est modifiable en python, on pourra par contre ajouter et supprimer des noeuds à la liste.
# ◦ Lors de la création d’un circuit, la liste de ses noeuds est vide

# Définir les méthodes :
# ◦ __str__
# ◦ maxX : renvoie l’abscisse maximale du circuit (abscisse du noeud du circuit ayant la plus grande abscisse). Retourne 0.0 si le circuit est vide (ne contient pas de noeuds)
# ◦ même principe pour minX, maxY, minY
# ◦ noeud_le_plus_proche : renvoie le noeud le plus proche du point de coordonnées px,py. Signale une erreur si le circuit ne contient pas de noeud par :
#   ▪ raise Exception("Circuit vide")
# ◦ contienNoeud : retourne vrai si un nœud est contenu dans le circuit, faux sinon
# ◦ addNoeud : ajoute un nœud au circuit. Si le nœud appartient déjà au circuit :
#   ▪ raise Exception("le noeud est déjà dans le circuit")
# ◦ removeNoeud : retire un nœud du circuit. Si le nœud n’appartient pas au circuit :
#   ▪ raise Exception("le noeud n’est pas dans le circuit")
# ◦ menu : permet la gestion du circuit par menu textuel : voir ci-dessous un exemple d’interaction :
#   ▪ pour la suppression d’un nœud, vous aurez sans doute besoin de la méthode utilitaire choisiNoeud qui permet à l’utilisateur de choisir un nœud existant dans le circuit