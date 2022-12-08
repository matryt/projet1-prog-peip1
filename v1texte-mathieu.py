from random import randint, choice
from typing import List

REGLE = [1, 2, 3]
fini = False

nombreAllumettes = randint(10, 20)

def testNombre() -> int:
    n = input("Joueur, combien voulez-vous prendre d'allumettes ?")
    while type(n) != int:
        try:
            return int(n)
        except:
            print("Vous devez rentrer un nombre !")
            n = input("Joueur, combien voulez-vous prendre d'allumettes ?")

def enleverAllumettes(allumettes : int, regle : list[int]) -> int:
    nombre = testNombre()

    while nombre > allumettes or nombre not in regle:
        print(f"Vous voulez prendre {nombre} allumettes, ce qui est impossible !")
        nombre = testNombre()

    return allumettes - nombre
    
def afficherAllumettes(allumettes : int) -> None:
    for i in range(allumettes):
        print('|', end=" ")
    print("\n")

def jeuPossible(allumettes : int, regle : List[int]) -> bool:
    m = regle[0]
    return allumettes != 0 and allumettes - m < 0

def tirageOrdi(allumettes : int) -> int:
    c = choice(REGLE)
    while c > allumettes:
        c = choice(REGLE)
    allumettes -= c
    print(f"L'ordi a pris {c} allumettes")
    return allumettes

def jeu(REGLE, fini, nombreAllumettes) :
    REGLE.sort()

    while not fini:
        afficherAllumettes(nombreAllumettes)
        nombreAllumettes = enleverAllumettes(nombreAllumettes, REGLE)
        allumettesVides = nombreAllumettes == 0
        if allumettesVides or not jeuPossible(nombreAllumettes, REGLE):
            if allumettesVides:
                print("Bravo, vous avez gagné !")
                fini = True
            else:
                print("Le nombre d'allumettes est tel qu'il n'est plus possible de jouer ! Match nul.")
                fini = True
        else:
            afficherAllumettes(nombreAllumettes)
            nombreAllumettes = tirageOrdi(nombreAllumettes)
            if nombreAllumettes == 0:
                print("Malheureusement l'ordi a gagné ! Peut-être la prochaine fois !")
                fini = True
            if not jeuPossible(nombreAllumettes, REGLE):
                print("Le nombre d'allumettes est tel qu'il n'est plus possible de jouer ! Match nul.")
                fini = True 

jeu(REGLE, fini, nombreAllumettes)
