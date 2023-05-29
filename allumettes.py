# Loic LAMOUR et Mathieu CUVELIER - Groupe 5

import turtle as tu
from copy import deepcopy
from random import randint, choice
from time import sleep
from tkinter import Tk

import affichage as aff
import fond


def reglesJeu(s):
	"""
	Permet d'afficher les règles du jeu au début de chaque partie
	:param s: La classe Screen avec laquelle afficher la fenêtre
	:type s: Screen
	"""
	r = s.textinput("Règles du jeu",
	                "Bienvenue dans notre jeu de Nim ! \n Des buissons vont s'afficher, avec plus ou moins de fraises dessus qui symbolisent des allumettes. \n Pour gagner, il faut prendre la dernière fraise du dernier buisson. \n Les choix de fruits vont s'afficher juste après. \n Voulez-vous réafficher les règles (o / n) ?")
	if r != "n":
		reglesJeu(s)


def genererTas() -> list:
	"""
	Permet de générer les différents tas d'allumettes pour la partie à jouer
	:return: Une liste de listes contenant, pour chaque tas, le nombre d'allumettes restantes dans le tas et le nombre initial
	:rtype: list
	"""
	tas = []
	allumettesTotales = randint(15, 25)
	for _ in range(randint(2, 3)):
		if allumettesTotales // 2 > 2:
			a = randint(2, 11)
			tas.append([a, a])
			if allumettesTotales - a > 0:
				allumettesTotales -= a
	if allumettesTotales != 0:
		m = min(11, allumettesTotales)
		tas.append([m, m])
	return tas


def prenom():
	"""
	Génère la fenêtre pour demander son prénom au joueur, et le renvoie
	:return: Le prénom du joueur
	:rtype: str
	"""
	return tu.textinput("Début de partie", "Quel est votre prénom ?")


def tasVide(tas: list) -> bool:
	"""
	Teste si tous les tas sont vides ou non
	:param tas: Une liste de listes contenant, pour chaque tas, le nombre d'allumettes restantes dans le tas et le nombre initial
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
		if allumettes[0] != 0:
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


def testNombre(message, mini, maxi, texte):
	"""
	Demande des chaînes de caractères, jusqu'à qu'il soit possible de la convertir en nombre

	:param message: Le message à demander à l'utilisateur
	:type message: str
	:param mini: Le minimum possible
	:type mini: int
	:param maxi: Le maximum possible
	:type maxi: int
	:param texte: titre de la fenetre numinput
	:type texte: str
	:return: Le nombre converti
	:rtype: int
	"""
	return tu.numinput(texte, message, None, mini, maxi)


def afficheChoix(regle: list):
	"""
	Permet d'afficher à l'écran les choix d'allumettes possibles.
	:param regle: Les choix possibles d'allumettes
	:type regle: list
	:return: Le message à afficher
	:rtype: str

	:example:
	>>> afficheChoix([1, 2, 5])
	Les choix possibles sont 1 - 2 - 5
	"""
	c = "Les choix possibles sont "
	for choix in regle:
		c = c + str(choix) + " - "
	return c[:-2]


def afficheTas(tas: list, s):
	"""
	Affiche le nombre de tas et le nombre d'allumettes dans chaque tas
	:param tas: Une liste de listes contenant, pour chaque tas, le nombre d'allumettes restantes dans le tas et le nombre initial
	:type tas: list
	:param s: La classe Screen avec laquelle afficher la fenêtre
	:type s: Screen

	:example:
	>>> afficheTas([2, 3, 6])
	Il y a 3 tas.
	Ils possèdent respectivement 2, 3, 6 allumettes.
	"""
	c = f"Il y a {sum(i[0] for i in tas)} allumettes au début. Il y a {len(tas)} tas. \nIls possèdent respectivement "

	for allumettes in tas:
		c += f"{allumettes[0]}, "

	c = c[:-2] + " allumettes.\nEntrez n'importe quel caractère pour continuer"

	s.textinput("Début de la partie", c)


def enleverAllumettes(tas: list, regle: list, p: str) -> list:
	"""
	Permet de retourner le nombre d'allumettes après le tour du joueur
	:param tas: Le nombre d'allumettes par tas avant que le joueur ne joue
	:type tas: list
	:param regle: Les choix possibles
	:type regle: list
	:param p: Le prénom du joueur
	:type p: str
	:return: Le nombre d'allumettes par tas après le tour
	:rtype: list
	"""

	allumettesSouhaitees = int(
		testNombre(f"{afficheChoix(regle)} \n{p}, combien voulez-vous prendre de fraises ?", 1, max(regle),
		           "Nombre d'allumettes"))
	tasDemande = int(
		testNombre(f"{p}, dans quel tas voulez-vous prendre ces fraises ?", 1, (len(tas)), "Choix du tas")) - 1

	impossibleTas = (allumettesSouhaitees > tas[tasDemande][0])
	impossibleRegle = (allumettesSouhaitees not in regle)
	while impossibleTas or impossibleRegle:
		# Vérifie que qu'il reste au moins autant d'allumettes que le joueur veut en prendre et qu'il respecte les règles
		if impossibleTas:
			message = f"Vous voulez prendre {allumettesSouhaitees} fraises dans le tas {tasDemande}, alors qu'il n'en contient que {tas[tasDemande][0]} !"
		else:
			message = f"Vous voulez prendre {allumettesSouhaitees} fraises dans le tas {tasDemande}, alors que ce nombre n'est pas dans la règle !"
		allumettesSouhaitees = int(
			testNombre(
				f"{message}\n \n {afficheChoix(regle)} \n {p}, combien voulez-vous prendre de fraises ?",
				1, max(regle),
				"Nombre d'allumettes")
		)
		tasDemande = int(
			testNombre(f"{p}, dans quel tas voulez-vous prendre ces fraises ?", 1, (len(tas)), "Choix du tas")) - 1
		impossibleTas = (allumettesSouhaitees > tas[tasDemande][0])
		impossibleRegle = (allumettesSouhaitees not in regle)

	tas[tasDemande][0] -= allumettesSouhaitees

	return tas


def afficherAllumettes(tas: list, t):
	"""
	Affiche le nombre d'allumettes passées en paramètre
	:param tas: Une liste de listes contenant, pour chaque tas, le nombre d'allumettes restantes dans le tas et le nombre initial
	:type tas: list
	:param t: L'objet Turtle à utiliser pour le dessin
	:type t: Turtle
	"""
	t.clear()
	coordsBuissons = ((-400, -170), (-640, 25), (500, -5), (240, -170))
	coordsNumeros = ((-195, -170), (-440, 20), (410, 10), (185, -180))
	for ta in range(len(tas)):
		aff.buisson(coordsBuissons[ta][0], coordsBuissons[ta][1], tas[ta][0], tas[ta][1] - tas[ta][0], 0.7, t)
		aff.numero(coordsNumeros[ta], ta + 1, t, "white")


def mex(l):
	"""
	Calcule le mex d'une liste
	:param l: La liste dont on veut calculer le mex
	:type l: list
	:return: Le mex de la liste
	:rtype: int
	"""
	i = 0
	while i in l:
		i += 1
	return i


def valPileAllumettes(J, L):
	"""
	Calcule la valeur de Nim d'une pile d'allumettes
	:param J: Le nombre d'allumettes dans la pile
	:type J: int
	:param L: Les règles du jeu
	:type L: list
	:return: La valeur de Nim de la pile
	:rtype: int
	"""
	if J:
		tab = [0]
		for i in range(1, J[0] + 1):
			tab.append(mex([tab[i - j] for j in L if i >= j]))
		return [tab[J[0]], J[1]]
	return [0, 0]


def sumNimList(l):
	"""
	Calcule la somme d'une liste de valeurs de Nim
	:param l: La liste de valeurs de Nim
	:type l: list
	:return: La somme des valeurs de Nim
	:rtype: int
	"""
	s = 0
	l.append([0, 0])
	for i in range(len(l)):
		s = s ^ l[i][0]
	return s


def valJeuAllumettes(jeu, coups):
	"""
	Calcule la valeur de Nim d'un jeu d'allumettes
	:param jeu: Le jeu d'allumettes
	:type jeu: list
	:param coups: Les règles du jeu
	:type coups: list
	:return: La valeur de Nim du jeu
	:rtype: int
	"""
	return sumNimList([valPileAllumettes(i, coups) for i in jeu])


def trouverStratGagnante(tas, coups):
	"""
	Trouve une stratégie gagnante pour le joueur
	:param tas: Le jeu d'allumettes
	:type tas: list
	:param coups: Les règles du jeu
	:type coups: list
	:return: La stratégie gagnante
	:rtype: tuple
	"""
	val = valJeuAllumettes(tas, coups)
	if val != 0:
		for t in range(len(tas)):
			thisTat = tas[t][0]
			for c in coups:
				if thisTat >= c:
					l = tas[:t] + [[thisTat - c, thisTat]] + tas[t + 1:]
					try:
						if type(l[0][0]) == list:
							print(l)
					except:
						pass
					if valJeuAllumettes(l, coups) == 0:
						return t, c
	return None

def tirageOrdi(tas: list, regle: list) -> list:
	s = trouverStratGagnante(tas, regle)
	if s is not None:
		tasAEnlever, c = s
	else:
		tasAEnlever = randint(0, len(tas) - 1)
		allumettesMax = tas[tasAEnlever][0]
		c = choice(regle)
		while c > allumettesMax:
			c = choice(regle)
			tasAEnlever = randint(0, len(tas) - 1)
			allumettesMax = tas[tasAEnlever][0]
	tas[tasAEnlever][0] -= c
	print(f"--> L'ordi a pris {c} allumette(s) dans le tas {tasAEnlever + 1} \n")
	return tas


def animation_tas_vide(TasAnim):
	"""
	Permet d'afficher des éclairs en fonction des tas vides
	:param TasAnim: La liste des allumettes par tas
	:type TasAnim: list
	"""
	L = [[-320, 290], [640, 330], [-120, 330], [390, 295]]
	for i in range(len(TasAnim)):
		if TasAnim[i][0] == 0:
			fond.eclair(L[i][0], L[i][1], 1)


def fin(joueurVainqueur, s):
	"""
	Permet d'afficher le message et les animations de fin
	:param joueurVainqueur: True si c'est le joueur qui a gagné, False sinon
	:type joueurVainqueur: bool
	:param s: La classe Screen sur laquelle afficher les animations
	:type s: Screen
	"""
	if joueurVainqueur:
		print("Vous avez gagné !")
		aff.initialize()
		aff.couronne(s)
		aff.finish()
	else:
		print("☠ Malheureusement l'ordi a gagné ! 👎 Peut-être la prochaine fois !")
		aff.initialize()
		aff.tete(s)
	sleep(5)
	tu.done()
	s.bye()


def bouclePrincipale(s, tc, p):
	"""

	:param s: La classe Screen sur laquelle afficher les messages et les formes
	:type s: Screen
	:param tc: La tortue à utiliser pour les dessins
	:type tc: Turtle
	:param p: Le prénom du joueur
	:type p: str
	"""
	fini = False
	tas = genererTas()
	TasAnim = tas[:]
	REGLE = genererRegle()
	REGLE.sort()
	afficheTas(tas, s)
	if trouverStratGagnante(tas, REGLE) is not None:
		ordiCommence = True
	else:
		ordiCommence = False

	while not fini:
		aff.initialize()
		if not ordiCommence:
			afficherAllumettes(tas, tc)
			tas = enleverAllumettes(tas, REGLE, p)
		else:
			tas = tirageOrdi(tas, REGLE)
		animation_tas_vide(tas)
		afficherAllumettes(tas, tc)

		if tasVide(tas):
			fin(not ordiCommence, s)
			fini = True
		else:
			if ordiCommence:
				tas = enleverAllumettes(tas, REGLE, p)
			else:
				tas = tirageOrdi(tas, REGLE)
			animation_tas_vide(tas)
			if tasVide(tas):
				fin(ordiCommence, s)
				fini = True
	s.bye()


def jeu():
	"""
	Fonction principale du jeu, qui appelle toutes les autres
	"""
	t = Tk()
	TAILLE_ECRAN = (min(1920, t.winfo_screenwidth()), min(1080, t.winfo_screenheight()) - 80)
	t.withdraw()

	tu.setup(TAILLE_ECRAN[0], TAILLE_ECRAN[1], 0, 0)
	s = tu.Screen()
	tu.delay(0)
	s.colormode(255)
	s.screensize(TAILLE_ECRAN[0], TAILLE_ECRAN[1])

	aff.initialize()
	fond.fond_()

	reglesJeu(s)

	tu.hideturtle()

	tc = tu.Turtle()
	tc.hideturtle()

	p = prenom().capitalize()

	bouclePrincipale(s, tc, p)


# Appelle la fonction principale jeu et lance le jeu
jeu()
