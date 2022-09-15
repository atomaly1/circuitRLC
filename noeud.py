class Noeud:
    def __init__(self, nom: str, nx: float, ny: float):
        self._nom = nom
        self._nx = nx
        self._ny = nx

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

    # TODO : définir ny

    # TODO : définir méthode __str__

    # TODO : définir méthode DISTANCE qui calcule la distance entre un noeud est un point de coordonnées px,py

    # TODO : définir méthode DEMANDE qui permet à l’utilisateur de créer un nœud en précisant son nom, son abscisse et son ordonnée