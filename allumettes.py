# Loic LAMOUR et Mathieu CUVELIER - Groupe 5

from random import randint, choice
from typing import List
from affichage import *
from turtle import *
from time import sleep

def genererRegle() -> List[int]:
	"""
	Permet de générer la liste faisant office de règle pour le jeu en cours
	:return: La liste contenant les différents choix possibles
	:rtype: List[Int]

	:Example:

	>>> genererRegle()
	[1, 2, 5]
	"""
	r = [1]
	while len(r) < randint(2, 5):
		n = randint(1, 7)
		if n not in r:
			r.append(n)
	return r


def testNombre() -> int:
	"""
	Demande des chaînes de caractères, jusqu'à qu'il soit possible de la convertir en nombre
    
	:return: Le nombre converti
	:rtype: int
	"""
	test=False
	while not test :
		try:
			n = int(input("Joueur, combien voulez-vous prendre d'allumettes ?"))
			test=True
		except ValueError:
			print("Vous devez rentrer un nombre !")
			
	return n  # type: ignore


def afficheChoix(regle: List[int]) -> None:
	"""
	Permet d'afficher à l'écran les choix d'allumettes possibles.
	:param regle: Les choix possibles d'allumettes
	:type regle: List[int]

	:example:
	>>> afficheChoix([1, 2, 5])
	Les choix possibles sont 1 - 2 - 5
	"""
	c = "Les choix possibles sont "
	for choix in regle:
		c = c + str(choix) + " - "
	print(c[:-2])


def enleverAllumettes(allumettes: int, regle: List[int]) -> int:
	"""
	Permet de retourner le nombre d'allumettes après le tour du joueur
	:param allumettes: Le nombre d'allumettes avant que le joueur ne joue
	:type allumettes: int
	:param regle: Les choix possibles
	:type regle: List[int]
	:return: Le nombre d'allumettes après le tour
	:rtype: int
	"""
	nombre = testNombre()

	while nombre > allumettes or nombre not in regle: # Vérifie que qu'il reste au moins autant d'allumettes que le joueur veut en prendre  et qu'il respecte les règles
		print(f"Vous voulez prendre {nombre} allumettes, ce qui est impossible !")
		nombre = testNombre()

	return allumettes - nombre


def afficherAllumettes(allumettes: int, t, ECRAN : tuple) -> None:
	"""
	Affiche le nombre d'allumettes passées en paramètre
	:param allumettes: Le nombre d'allumettes actuel
	:type allumettes: int
	:param t: L'objet Turtle à utiliser pour le dessin
	:type t: Turtle

	"""
	t.clear()
	espaceRestant = (ECRAN[0] - 50 - allumettes * 50) / 2
	dessinePaquet(-ECRAN[0]/2+espaceRestant, -200, 200, "white", t, allumettes)


def jeuPossible(allumettes: int, regle: List[int]) -> bool:
	"""
	Détermine s'il est encore possible de jouer, en fonction du nombre d'allumettes, et si au moins un des nombres contenu dans la règle permet d'enlever des allumettes
	:param allumettes: Nombre d'allumettes restantes
	:type allumettes: int
	:param regle: Choix d'allumettes possibles
	:type regle: List[int]
	:return: True s'il est encore possible de jouer, False sinon
	:rtype: bool

	:example:
	>>> jeuPossible(1,[2,3,4])
	False

	>>> jeuPossible(3,[3,5,7])
	True

	"""
	return allumettes == 0 or allumettes - regle[0] >= 0


def tirageOrdi(allumettes: int, regle: List[int]) -> int:
	"""
	Permet de générer un nombre aléatoire d'allumettes correspondant au nombre d'allumettes qu'enlève l'ordinateur
	:param allumettes: Nombre d'allumettes restantes
	:type allumettes: int
	:param regle: Choix d'allumettes possibles
	:type regle: List[int]
	:return: Le nombre d'allumettes après le tour de l'ordinateur
	:rtype: int
	"""
	c = choice(regle)
	while c > allumettes:
		c = choice(regle)
	allumettes -= c
	print(f"--> L'ordi a pris {c} allumette(s)")
	return allumettes


def jeu() -> None:
	"""
	Fonction principale du jeu, qui appelle toutes les autres
	"""
	s = Screen()
	s.colormode(255)
	speed(0)
	s.bgcolor(1, 139, 104)

	TAILLE_ECRAN = (1920, 1080)

	tc = Turtle()
	tc.hideturtle()
        
	fini = False
	nombreAllumettes = randint(10, 30)
	REGLE = genererRegle()
	REGLE.sort()
	afficheChoix(REGLE)
	print(f"Il y a {nombreAllumettes} allumettes au début.")

	while not fini:
		afficherAllumettes(nombreAllumettes, tc, TAILLE_ECRAN)
		nombreAllumettes = enleverAllumettes(nombreAllumettes, REGLE)
		if nombreAllumettes==0 or not jeuPossible(nombreAllumettes, REGLE):
			print("Vous avez gagné !")
			couronne(s)
			sleep(5)

			fini = True
		else:
			nombreAllumettes = tirageOrdi(nombreAllumettes, REGLE)
			if nombreAllumettes == 0 or not jeuPossible(nombreAllumettes, REGLE):
				print("☠ Malheureusement l'ordi a gagné ! 👎 Peut-être la prochaine fois !")
				fini = True

jeu() # Appelle la fonction principale jeu et lance le mini jeu 
