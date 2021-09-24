class ListOperationsInterface:
    def __init__(self, liste = ''):
        self.liste = liste

    def creer_liste_vide(self) -> list:
        """
            Entrée: None
            Sortie: List
            Créer une liste vide et retourne vrai si la liste retourné est nulle sinon retourne faux
        """

        self.liste = []
        return self.liste == []

    def inserer(self, e, i) -> list:
        """
            Entrées: Element e(str), Index i(int)
            Sortie: List
            Retourne la liste avec l'élement insérer
        """

        if self.longueur() < 0: # Vous devriez utiliser la fonction "creer_liste_vide" dans votre programme principal
            return False

        self.liste.insert(i, e)
        return self.liste

    def rechercher(self, e) -> int:
        """
            Entrée: Element e(str)
            Sortie: -1 si l'élement n'est pas dans la liste sinon l'index de l'élement
            Cherche un élement dans la liste et retourne -1 si il n'est pas trouvé sinon l'index de l'élement est retourné.
        """

        if e not in self.liste:
            return -1

        return self.liste.index(e)

    def lire(self, i) -> object:
        """
            Entrée: Index i(int)
            Sortie: False si la liste n'existe pas sinon l'élement de la liste est retourné
            Récupère un élement de la liste et le retourne (si la liste n'existe pas retourne faux)
        """

        if self.longueur() < 0:
            return False

        return self.liste[i]

    def supprimer(self, i) -> list:
        """
            Entrée: Index i(int)
            Sortie: False si la liste n'existe pas sinon l'élement de la liste est supprimé
            Supprime un élement de la liste et retourne la liste modifiée (si la liste n'existe pas retourne faux)
        """

        if self.longueur() < i:
            return False

        del self.liste[i]
        return self.liste

    def longueur(self) -> int:
        """
            Entrée: None
            Sortie: len(liste)
            Retourne la longueur de la liste
        """

        return len(self.liste)

    def est_liste_vide(self) -> bool:
        """
            Entrée: None
            Sortie: vrai si la liste est vide faux sinon
        """

        return self.liste == []

    def modifier(self, e, i) -> list:
        if self.longueur() - 1 < i:
            return self.liste
        self.liste[i] = e
        return self.liste

interface = ListOperationsInterface()
interface.creer_liste_vide()

interface.inserer("Bonjour", 0)
interface.inserer("Ceci", 1)
interface.inserer("Est", 2)
interface.inserer("Un", 3)
interface.inserer("Test", 4)

texte = interface.lire(0)
print(texte)

longueur = interface.longueur()
print(longueur)

modification = interface.modifier("Bonsoir", 0)
print(modification)
