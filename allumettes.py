# Loic LAMOUR et Mathieu CUVELIER - Groupe 5

from random import randint, choice
from time import sleep
from typing import List

from affichage import *


def genererTas() -> list:
	"""
	Permet de générer les différents tas d'allumettes pour la partie à jouer
	:return: Le nombre d'allumettes par tas
	:rtype: list
	"""
	tas = []
	allumettesTotales = randint(15, 25)
	for _ in range(randint(2, 3)):
		if allumettesTotales // 2 > 2:
			a = randint(2, allumettesTotales // 2)
			tas.append(a)
			allumettesTotales -= a
	if allumettesTotales != 0:
		tas.append(allumettesTotales)
	return tas


def tasVide(tas):
	"""
	Teste si tous les tas sont vides ou non
	:param tas: Le nombre d'allumettes par tas
	:type tas: list
	:return: True si tout est vide, False sinon
	:rtype: bool
	"""
	for allumettes in tas:
		if allumettes != 0:
			return False
	return True


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


def testNombre(message: str) -> int:
	"""
	Demande des chaînes de caractères, jusqu'à qu'il soit possible de la convertir en nombre

	:param message: Le message à demander à l'utilisateur
	:type message: str
	:return: Le nombre converti
	:rtype: int
	"""
	test = False
	while not test:
		try:
			n = int(input(message))
			test = True
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


def afficheTas(tas: list):
	"""
	Affiche le nombre de tas et le nombre d'allumettes dans chaque
	:param tas: Le nombre d'allumettes dans chaque tas
	:type tas: list
	"""
	c = ""

	c += f"Il y a {len(tas)} tas. \nIls possèdent respectivement "

	for allumettes in tas:
		c += f"{allumettes}, "

	print(f"{c[:-2]} allumettes.")

def enleverAllumettes(tas: list, regle: List[int]) -> list:
	"""
	Permet de retourner le nombre d'allumettes après le tour du joueur
	:param tas: Le nombre d'allumettes par tas avant que le joueur ne joue
	:type tas: list
	:param regle: Les choix possibles
	:type regle: List[int]
	:return: Le nombre d'allumettes après le tour
	:rtype: int
	"""
	allumettesSouhaitees = testNombre("Joueur, combien voulez-vous prendre d'allumettes ?")
	tasDemande = testNombre("Joueur, dans quel tas voulez-vous prendre ces allumettes ?") - 1

	while allumettesSouhaitees > tas[tasDemande] or allumettesSouhaitees not in regle:
		# Vérifie que qu'il reste au moins autant d'allumettes que le joueur veut en prendre et qu'il respecte les règles
		print(f"Vous voulez prendre {allumettesSouhaitees} allumettes, ce qui est impossible !")
		allumettesSouhaitees = testNombre("Joueur, combien voulez-vous prendre d'allumettes ?")
		tasDemande = testNombre("Joueur, dans quel tas voulez-vous prendre ces allumettes ?") - 1

	tas[tasDemande] -= allumettesSouhaitees

	return tas


def afficherAllumettes(tas: list, t, ECRAN: tuple) -> None:
	"""
	Affiche le nombre d'allumettes passées en paramètre
	:param tas: Le nombre d'allumettes par tas avant que le joueur ne joue
	:type tas: list
	:param t: L'objet Turtle à utiliser pour le dessin
	:type t: Turtle
	:param ECRAN: La taille de la fenêtre fixée
	:type ECRAN: tuple[int]

	"""
	t.clear()
	espaceRestant = ECRAN[0] - 50 * (sum(tas) + len(tas) - 1)
	coords = [-940 + espaceRestant / 2, 0]
	for ta in tas:
		dessinePaquet(coords[0], coords[1], 200, (244, 164, 96), t, ta)
		coords[0] += 50 * (ta + 1)


def jeuPossible(tas: list, regle: List[int]) -> bool:
	"""
	Détermine s'il est encore possible de jouer, en fonction du nombre d'allumettes, et si au moins un des nombres contenu dans la règle permet d'enlever des allumettes
	:param tas: Le nombre d'allumettes par tas avant que le joueur ne joue
	:type tas: list
	:param regle: Choix d'allumettes possibles
	:type regle: List[int]
	:return: True s'il est encore possible de jouer, False sinon
	:rtype: bool

	:example:
	>>> jeuPossible([2, 5, 6],[2,3,4])
	False

	>>> jeuPossible([2, 2, 2],[3,5,7])
	True

	"""
	possible = False
	for allumette in tas:
		if allumette != 0 or allumette - regle[0] >= 0:
			possible = True
	return possible


def tirageOrdi(tas: list, regle: List[int]) -> list:
	"""
	Permet de générer un nombre aléatoire d'allumettes correspondant au nombre d'allumettes qu'enlève l'ordinateur
	:param tas: Le nombre d'allumettes par tas avant que le joueur ne joue
	:type tas: list
	:param regle: Choix d'allumettes possibles
	:type regle: List[int]
	:return: Le nombre d'allumettes après le tour de l'ordinateur
	:rtype: int
	"""
	tasAEnlever = randint(0, len(tas) - 1)
	allumettesMax = tas[tasAEnlever]
	c = choice(regle)
	while c > allumettesMax:
		c = choice(regle)
		tasAEnlever = randint(0, len(tas) - 1)
		allumettesMax = tas[tasAEnlever]
	tas[tasAEnlever] -= c
	print(f"--> L'ordi a pris {c} allumette(s) dans le tas {tasAEnlever+1}")
	return tas


def jeu() -> None:
	"""
	Fonction principale du jeu, qui appelle toutes les autres
	"""
	TAILLE_ECRAN = (1400, 700)
	s = tu.Screen()
	s.colormode(255)
	s.screensize(TAILLE_ECRAN[0], TAILLE_ECRAN[1])
	tu.speed(0)
	s.bgcolor(1, 139, 104)

	TAILLE_ECRAN = (1920, 1080)

	tu.hideturtle()

	tc = tu.Turtle()
	tc.hideturtle()

	fini = False
	tas = genererTas()
	REGLE = genererRegle()
	REGLE.sort()
	afficheChoix(REGLE)
	print(f"Il y a {sum(tas)} allumettes au début.")
	afficheTas(tas)
	while not fini:
		afficherAllumettes(tas, tc, TAILLE_ECRAN)
		tas = enleverAllumettes(tas, REGLE)
		if tasVide(tas) or not jeuPossible(tas, REGLE):
			print("Vous avez gagné !")
			couronne(s)
			sleep(5)
			fini = True
		else:
			tas = tirageOrdi(tas, REGLE)
			if tasVide(tas) or not jeuPossible(tas, REGLE):
				print("☠ Malheureusement l'ordi a gagné ! 👎 Peut-être la prochaine fois !")
				fini = True
				tete(s)
				sleep(5)
	s.bye()


jeu()  # Appelle la fonction principale jeu et lance le mini jeu
