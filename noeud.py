from cmath import sqrt

class Noeud:
    def __init__(self, nom: str, nx: float, ny: float):
        self._nom = nom
        self._nx = nx
        self._ny = ny

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, nom: str) -> None:
        self._nom = nom
    
    @property
    def nx(self) -> float:
        print("lecture nx")
        return self._nx

    @nx.setter
    def nx(self, nx: float) -> None:
        self._nx = nx

    @property
    def ny(self) -> float:
        print("lecture ny")
        return self._ny

    @ny.setter
    def nx(self, ny: float) -> None:
        self._ny = ny

    # TODO : définir méthode __str__
    def __str__(self):
        return f"Noeud {self.nom} en {self.nx},{self.ny}"

    # TODO : définir méthode DISTANCE qui calcule la distance entre un noeud est un point de coordonnées px,py
    def distance(self, px: float, py: float) -> float:
        dx = self.nx - px
        dy = self.ny - py
        return sqrt(pow(dx,2) + pow(dy,2))

    # TODO : définir méthode DEMANDE qui permet à l’utilisateur de créer un nœud en précisant son nom, son abscisse et son ordonnée
    def demande() -> 'Noeud':
        print("**CREATION D'UN NOUVEAU NOEUD**\n")
        print("Entrer le nom du Noeud :")
        nom = input()
        print("Entrer la coordonnée en abscisse (x) du Noeud :")
        nx = input()
        print("Entrer la coordonnée en ordonnée (y) du Noeud :")
        ny = input()
        return Noeud(nom,nx,ny)