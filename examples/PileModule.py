import GenericOperations as p
from random import randint

pile = p.GenericOperations()
pile.cree_objet_vide()
pile.empiler(1)
pile.empiler(2)
print(pile.liste)

def inversion(pile):
    pile_inversee = p.GenericOperations()
    pile_inversee.cree_objet_vide()

    for i in range(len(pile.liste)):
        dernierElement = pile.depiler()
        pile_inversee.empiler(dernierElement)

    return pile_inversee.liste

def simulation_file(tours):
    file = p.GenericOperations('file')
    file.cree_objet_vide()
    for i in range(tours):
        nombre = randint(0, 100)

        if nombre % 2 == 0:
            nombre *= 10
            file.empiler(nombre)
        else:
            file.depiler()

        return file.liste

def test_parenthesage(string):
    pile = p.GenericOperations()
    pile.cree_objet_vide()

    for chaine in string:
        if chaine == '(':
            pile.empiler(chaine)
        elif chaine == ')':
            pile.depiler()

    if not pile.objet_vide():
        return '%s est mal parenthèsé.' %(string)
    else:
        return '%s est bien parenthèsé.' %(string)

print(inversion(pile))
print(simulation_file(10))
print(test_parenthesage("(10+3)")) # True
print(test_parenthesage("(10+3")) # False
