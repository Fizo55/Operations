class GenericOperations:
    def __init__(self, typeof = '', liste = ''):
        self.liste = liste
        self.typeof = typeof

    def cree_objet_vide(self) -> bool:
        self.liste = []
        return self.liste

    def objet_vide(self) -> bool:
        return len(self.liste) == 0

    def empiler(self, e) -> list:
        if self.liste == '':
            return self.cree_objet_vide()

        if self.typeof == '':
            self.liste.insert(0, e)
        else:
            self.liste.append(e)
        return self.liste

    def depiler(self) -> list:
        if self.liste == '':
            return self.cree_objet_vide()

        if self.objet_vide():
            return self.liste

        elementSommet = self.liste[0]
        del self.liste[0]
        return elementSommet

if __name__ == "__main__":
    # Pile test
    interface = GenericOperations()
    interface.cree_objet_vide()
    interface.depiler()
    print(interface.objet_vide())
    interface.empiler("Bonjour")
    interface.empiler("Ceci")
    interface.empiler("Est")
    interface.empiler("Un")
    interface.empiler("Test")
    print(interface.liste)
    print(interface.depiler())

    # File test
    interface = GenericOperations('file')
    interface.cree_objet_vide()
    interface.depiler()
    print(interface.objet_vide())
    interface.empiler("Bonjour")
    interface.empiler("Ceci")
    interface.empiler("Est")
    interface.empiler("Un")
    interface.empiler("Test")
    print(interface.liste)
    print(interface.depiler())
