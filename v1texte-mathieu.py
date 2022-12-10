3
777from random import randint, choice
from typing import List


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
	Demande une chaîne de caractères qu'il convertit en nombre si possible, ou en redemande tant que la conversion n'est pas possible y a besoin

	:return: Le nombre converti
	:rtype: int
	"""
	n = input("Joueur, combien voulez-vous prendre d'allumettes ?")
	while type(n) != int:
		try:
			n = int(n)
		except ValueError:
			print("Vous devez rentrer un nombre !")
			n = input("Joueur, combien voulez-vous prendre d'allumettes ?")
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
	:param allumettes: Le nombre d'allumettes au départ
	:type allumettes: int
	:param regle: Les choix possibles
	:type regle: List[int]
	:return: Le nombre d'allumettes final
	:rtype: int
	"""
	nombre = testNombre()

	while nombre > allumettes or nombre not in regle:
		print(f"Vous voulez prendre {nombre} allumettes, ce qui est impossible !")
		nombre = testNombre()

	return allumettes - nombre


def afficherAllumettes(allumettes: int) -> None:
	"""
	Affiche le nombre d'allumettes passées en paramètre
	:param allumettes: Le nombre d'allumettes
	:type allumettes: int

	:example:

	>>> afficherAllumettes(3)
	| | |
	"""
	for i in range(allumettes):
		print('|', end=" ")
	print("\n")


def jeuPossible(allumettes: int, regle: List[int]) -> bool:
	"""
	Détermine s'il est encore possible de jouer, en fonction de si le jeu est fini ou non, et si un des choix permet d'enlever des allumettes
	:param allumettes: Nombre d'allumettes restantes
	:type allumettes: int
	:param regle: Choix d'allumettes possibles
	:type regle: List[int]
	:return: True s'il est encore possible de jouer, False sinon
	:rtype: bool
	"""
	m = regle[0]
	return allumettes == 0 or allumettes - m >= 0


def tirageOrdi(allumettes: int, REGLE: List[int]) -> int:
	"""
	Permet de générer un nombre aléatoire d'allumettes corrspondant au nombre d'allumettes qu'enlève l'ordinateur
	:param allumettes: Nombre d'allumettes restantes
	:type allumettes: int
	:param REGLE: Choix d'allumettes possibles
	:type REGLE: List[int]
	:return: Le nombre d'allumettes après le tour de l'ordinateur
	:rtype: int
	"""
	c = choice(REGLE)
	while c > allumettes:
		c = choice(REGLE)
	allumettes -= c
	print(f"--> L'ordi a pris {c} allumette(s)")
	return allumettes


def jeu() -> None:
	"""
	Fonction principale du jeu, qui appelle toutes les autres
	:param fini:
	:type fini:
	:param nombreAllumettes:
	:type nombreAllumettes:
	:return: None
	:rtype: None
	"""

	fini = False
	nombreAllumettes = randint(10, 30)
	REGLE = genererRegle()
	REGLE.sort()
	afficheChoix(REGLE)
	print(f"Il y a {nombreAllumettes} allumettes au début.")

	while not fini:
		afficherAllumettes(nombreAllumettes)
		nombreAllumettes = enleverAllumettes(nombreAllumettes, REGLE)
		allumettesVides = nombreAllumettes == 0
		if allumettesVides:
			print("🎂 Bravo, vous avez gagné !")
			fini = True
		elif not jeuPossible(nombreAllumettes, REGLE):
			print("⚐ Le nombre d'allumettes est tel qu'il n'est plus possible de jouer ! Match nul.")
			fini = True
		else:
			afficherAllumettes(nombreAllumettes)
			nombreAllumettes = tirageOrdi(nombreAllumettes, REGLE)
			if nombreAllumettes == 0:
				print("☠ Malheureusement l'ordi a gagné ! 👎 Peut-être la prochaine fois !")
				fini = True
			if not jeuPossible(nombreAllumettes, REGLE):
				print("⚐ Le nombre d'allumettes est tel qu'il n'est plus possible de jouer ! Match nul.")
				fini = True


jeu()
