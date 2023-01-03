# Loic LAMOUR et Mathieu CUVELIER - Groupe 5

import turtle as tu
from random import randint, choice
from time import sleep

import affichage as aff
import fond


def reglesJeu():
	"""
	Permet d'afficher les règles du jeu au début de chaque partie
	"""
	print("Bienvenue dans notre jeu de Nim !")
	print("Des buissons vont s'afficher, avec plus ou moins de fruits dessus qui représentent les allumettes.")
	print("Pour gagner, il faut prendre le dernier fruit du dernier buisson.")
	print("Les choix d'allumettes vont s'afficher juste après.")
	r = input("Voulez-vous réafficher les règles (o / n) ?")
	if r == "o":
		reglesJeu()


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


def tasVide(tas: list) -> bool:
	"""
	Teste si tous les tas sont vides ou non
	:param tas: Le nombre d'allumettes par tas
	:type tas: list
	:return: True si tout est vide, False sinon
	:rtype: bool

	:Example:
	>>> tasVide([2, 8, 0])
	False
	>>> tasVide([0, 0, 0])
	True
	"""
	for allumettes in tas:
		if allumettes != 0:
			return False
	return True


def genererRegle() -> list:
	"""
	Permet de générer la liste faisant office de règle pour le jeu en cours
	:return: La liste contenant les différents choix possibles
	:rtype: list

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

	return n


def afficheChoix(regle: list):
	"""
	Permet d'afficher à l'écran les choix d'allumettes possibles.
	:param regle: Les choix possibles d'allumettes
	:type regle: list

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
	Affiche le nombre de tas et le nombre d'allumettes dans chaque tas
	:param tas: Le nombre d'allumettes dans chaque tas
	:type tas: list

	:example:
	>>> afficheTas([2, 3, 6])
	Il y a 3 tas.
	Ils possèdent respectivement 2, 3, 6 allumettes.
	"""
	c = f"Il y a {len(tas)} tas. \nIls possèdent respectivement "

	for allumettes in tas:
		c += f"{allumettes}, "

	print(f"{c[:-2]} allumettes.")


def enleverAllumettes(tas: list, regle: list) -> list:
	"""
	Permet de retourner le nombre d'allumettes après le tour du joueur
	:param tas: Le nombre d'allumettes par tas avant que le joueur ne joue
	:type tas: list
	:param regle: Les choix possibles
	:type regle: list
	:return: Le nombre d'allumettes par tas après le tour
	:rtype: list
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


def afficherAllumettes(tas: list, t):
	"""
	Affiche le nombre d'allumettes passées en paramètre
	:param tas: Le nombre d'allumettes par tas avant que le joueur ne joue
	:type tas: list
	:param t: L'objet Turtle à utiliser pour le dessin
	:type t: Turtle
n
	"""
	t.clear()
	coordsBuissons = ((-325, -100), (-325, 50), (250, 85), (250, -100))
	coordsNumeros = ((-325, -125), (-325, 20), (250, 55), (250, -125))
	for ta in range(len(tas)):
		aff.buisson(coordsBuissons[ta][0], coordsBuissons[ta][1], tas[ta], t)
		aff.numero(coordsNumeros[ta], ta + 1, t, "white")


def tirageOrdi(tas: list, regle: list) -> list:
	"""
	Permet de générer un nombre aléatoire d'allumettes correspondant au nombre d'allumettes qu'enlève l'ordinateur
	:param tas: Le nombre d'allumettes par tas avant que le joueur ne joue
	:type tas: list
	:param regle: Choix d'allumettes possibles
	:type regle: list
	:return: Le nombre d'allumettes par tas après le tour de l'ordinateur
	:rtype: list
	"""
	tasAEnlever = randint(0, len(tas) - 1)
	allumettesMax = tas[tasAEnlever]
	c = choice(regle)
	while c > allumettesMax:
		c = choice(regle)
		tasAEnlever = randint(0, len(tas) - 1)
		allumettesMax = tas[tasAEnlever]
	tas[tasAEnlever] -= c
	print(f"--> L'ordi a pris {c} allumette(s) dans le tas {tasAEnlever + 1} \n")
	return tas


def jeu():
	"""
	Fonction principale du jeu, qui appelle toutes les autres
	"""
	TAILLE_ECRAN = (1400, 700)

	reglesJeu()

	s = tu.Screen()
	tu.delay(0)
	s.colormode(255)
	s.screensize(TAILLE_ECRAN[0], TAILLE_ECRAN[1])

	aff.initialize()
	fond.fond_()

	tu.hideturtle()

	tc = tu.Turtle()
	tc.hideturtle()

	fini = False
	tas = genererTas()
	REGLE = genererRegle()
	REGLE.sort()
	print(f"Il y a {sum(tas)} allumettes au début.")
	afficheTas(tas)

	while not fini:
		afficheChoix(REGLE)
		aff.initialize()
		afficherAllumettes(tas, tc)
		tas = enleverAllumettes(tas, REGLE)
		if tasVide(tas):
			print("Vous avez gagné !")
			aff.initialize()
			aff.couronne(s)
			aff.finish()
			sleep(5)
			fini = True
		else:
			tas = tirageOrdi(tas, REGLE)
			if tasVide(tas):
				print("☠ Malheureusement l'ordi a gagné ! 👎 Peut-être la prochaine fois !")
				fini = True
				aff.initialize()
				aff.tete(s)
				sleep(5)
	s.bye()


# Appelle la fonction principale jeu et lance le jeu
jeu()
