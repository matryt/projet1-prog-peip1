from random import randint, choice
from typing import List

fini = False

nombreAllumettes = randint(10, 30)

def genererRegle() -> None:
	"""
	Permet de générer la liste faisant office de règle pour le jeu en cours
	"""
	r = [1]
	while len(r) < randint(2,5):
		n = randint(1, 7)
		if n not in r:
			r.append(n)
	return r

def testNombre() -> int:
    """
    Permet de tester si la chaîne de caractères passée en paramètre peut être convertie ou non en entier, et sinon redemande à chaque fois un nombre jusqu'à qu'il puisse le convertir""" 
    n = input("Joueur, combien voulez-vous prendre d'allumettes ?")
    while type(n) != int:
        try:
            return int(n)
        except:
            print("Vous devez rentrer un nombre !")
            n = input("Joueur, combien voulez-vous prendre d'allumettes ?")

def afficheChoix(regle : List[int]):
	print("Les choix possibles sont ", end="")
	for c in regle:
		print(c, end=" - ")
	print("")

def enleverAllumettes(allumettes : int, regle : List[int]) -> int:
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
    return allumettes == 0 or allumettes - m >= 0

def tirageOrdi(allumettes : int, REGLE : List[int]) -> int:
    c = choice(REGLE)
    while c > allumettes:
        c = choice(REGLE)
    allumettes -= c
    print(f"L'ordi a pris {c} allumettes")
    return allumettes

def jeu(fini, nombreAllumettes) :
    REGLE = genererRegle()
    REGLE.sort()
    afficheChoix(REGLE)
    print(f"Il y a {nombreAllumettes} allumettes au début.")

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
            nombreAllumettes = tirageOrdi(nombreAllumettes, REGLE)
            if nombreAllumettes == 0:
                print("Malheureusement l'ordi a gagné ! Peut-être la prochaine fois !")
                fini = True
            if not jeuPossible(nombreAllumettes, REGLE):
                print("Le nombre d'allumettes est tel qu'il n'est plus possible de jouer ! Match nul.")
                fini = True 

jeu(fini, nombreAllumettes)
