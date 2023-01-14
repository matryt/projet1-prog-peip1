# Loic LAMOUR et Mathieu CUVELIER - Groupe 5

import math
import random as rd
import turtle as tu


def dessinePolygone(cotes, longueur, x, y, couleur=(1, 106, 136)):
	"""
	Permet de dessiner un polygone quelconque
	:param cotes: Le nombre de côtés à tracer
	:type cotes: int
	:param longueur: La longueur des côtés du polygone
	:type longueur: int/float
	:param x: L'abscisse du début du polygone
	:type x: int/float
	:param y: L'ordonnée du début du polygone
	:type y: int/float
	:param couleur: La couleur dans laquelle tracer le polygone
	:type couleur: tuple / str
	"""
	tu.up()
	tu.color(couleur)
	tu.goto(x, y)
	tu.down()
	tu.seth(0)
	for i in range(cotes):
		tu.forward(longueur)
		tu.left(360 / cotes)


def dessineTriangle(longueur, x, y, couleur):
	"""
	:param longueur: La longueur des côtés du triangle
	:type longueur: int/float
	:param x: L'abscisse du début du triangle
	:type x: int/float
	:param y: L'ordonnée du début du triangle
	:type y: int/float
	:param couleur: La couleur dans laquelle tracer le triangle
	:type couleur: tuple/str
	"""
	dessinePolygone(3, longueur, x, y, couleur)


def dessineCercle(x, y, couleur, longueur):
	"""
	Fonction pour dessiner un cercle
	:param x: Position en abscisse
	:type x: int/float
	:param y: Position en ordonnée
	:type y: int/float
	:param couleur: Couleur dans laquelle dessiner le cercle
	:type couleur: str/tuple
	:param longueur: Longueur de chaque arc de cercle
	:type longueur: int/float
	"""
	tu.color(couleur)
	tu.begin_fill()
	dessinePolygone(250, longueur, x, y, couleur)
	tu.end_fill()


def sapin_foret(longueur, x, y):
	"""
	Permet de dessiner un sapin qui compose la forêt
	:param longueur: La longueur du tronc du sapin
	:type longueur: int/float
	:param x: L'abscisse de début du sapin
	:type x: int/float
	:param y: L'ordonnée de début du sapin
	:type y: int/float
	"""
	tu.hideturtle()
	tu.begin_fill()
	couleurTronc = (95 + rd.randint(0, 25), 52 + rd.randint(0, 20), 0)
	dessinePolygone(4, longueur, x, y, couleurTronc)
	tu.end_fill()
	tu.begin_fill()
	couleurSapin = (22 + rd.randint(0, 20), 92 + rd.randint(0, 35), 0)
	dessinePolygone(3, 2 * longueur, x - longueur / 2, y + longueur, couleurSapin)
	tu.end_fill()


def foret(longueur, x, y):
	"""
	Permet de dessiner une forêt de sapins
	:param longueur: La longueur du tronc des sapins
	:type longueur: int/float
	:param x: L'abscisse du début de la forêt
	:type x: int/float
	:param y: L'ordonnée du début de la forêt
	:type y: int/float
	"""
	tu.speed(0)
	for i in range(18):
		sapin(rd.uniform(longueur / 2, 1.5 * longueur), x + i * 2 * longueur, y)


def rectangle(longueur, x, y, couleur):
	"""
	:param longueur: La largeur du rectangle
	:type longueur: int/float
	:param x: L'abscisse du début du rectangle
	:type x: int/float
	:param y: L'ordonnée du début du rectangle
	:type y: int/float
	:param couleur: La couleur dans laquelle tracer le rectangle
	:type couleur: tuple/str
	"""
	tu.up()
	tu.goto(x, y)
	tu.down()
	tu.begin_fill()
	tu.color(couleur)
	tu.forward(longueur)
	tu.left(90)
	tu.forward(3 / 2 * longueur)
	tu.left(90)
	tu.forward(longueur)
	tu.left(90)
	tu.forward(3 / 2 * longueur)
	tu.end_fill()


def eclair(x, y, coeff):
	"""
	:param x: Position en abscisse
	:type x: int/float
	:param y: Position en ordonnée
	:type y: int/float
	:param coeff: Le coefficient par lequel multiplier les longueurs
	:type coeff: int/float
	"""
	c = min(255, 240 + rd.randint(0, 20) * (-1) ** rd.randint(0, 1))
	tu.color(c, c, 17)
	tu.up()
	tu.goto(x, y)
	tu.down()
	tu.begin_fill()
	tu.forward(50 * coeff)
	tu.right(135)
	tu.forward(85 * coeff)
	tu.left(135)
	tu.forward(30 * coeff)
	tu.right(135)
	tu.forward(100 * coeff)
	tu.right(150)
	tu.forward(70 * coeff)
	tu.left(105)
	tu.forward(30 * coeff)
	tu.right(135)
	tu.forward(85 * coeff)
	tu.end_fill()
	tu.seth(0)


def nuage(x, y, numero=1):
	"""
	Fonction pour dessiner un nuage

	:param x: Position en abscisse
    :type x: int/float
    :param y: Position en ordonnée
    :type y: int/float
    :param numero: Le nuage à afficher
    :type numero: int
    """
	tu.hideturtle()
	couleur = rd.randint(113, 163)
	if numero == 1:
		coeff = coeffMystere(1, 6)
		for i in range(3):
			dessineCercle(x + 25 * i, y + 10 * coeff, (couleur, couleur, couleur), coeff)
			dessineCercle(x + 25 * (i + 1), y - 10 * coeff, (couleur, couleur, couleur), coeff)
	else:
		for i in range(2):
			c = coeffMystere(1, 6)
			dessineCercle(x + 25 * i, y - 8 * c, (couleur, couleur, couleur), c)
			dessineCercle(x + 25 * (i + 1), y + 8 * c, (couleur, couleur, couleur), c)
			dessineCercle(x + 25 * (i + 2), y - 8 * c, (couleur, couleur, couleur), c)


def coeffMystere(nombreDepart, variance):
	"""
	Génère un coefficient aléatoire
	:param nombreDepart: Coefficient d'origine
	:type nombreDepart: int/float
	:param variance: Un nombre permettant de changer la variance par rapport au coefficient d'origine
	:type variance: int/float
	"""
	return nombreDepart + rd.uniform(-1 / variance, 1 / variance)


# (-1) ** rd.randint(1, 2) * rd.random() / variance


def sapin(longueur, x, y):
	"""
	Permet de dessiner un sapin seul
	:param longueur: La longueur du tronc du sapin
	:type longueur: int/float
	:param x: L'abscisse de début du sapin
	:type x: int/float
	:param y: L'ordonnée de début du sapin
	:type y: int/float
	"""
	tu.hideturtle()
	tu.begin_fill()
	couleurTronc = (95 + rd.randint(0, 25), 52 + rd.randint(0, 20), 0)
	rectangle(longueur, x, y, couleurTronc)
	tu.end_fill()
	tu.seth(0)
	tu.begin_fill()
	tu.up()
	couleurSapin = (22 + rd.randint(0, 20), 92 + rd.randint(0, 35), 0)
	dessineTriangle(2 * longueur, x - longueur / 2, y + 3 / 2 * longueur, couleurSapin)
	tu.end_fill()
	tu.begin_fill()
	dessineTriangle((3 / 2) * longueur, x - longueur / 3,
	                y + 3 / 2 * longueur + math.sqrt(longueur ** 2 / 4 + longueur ** 2) - 1, couleurSapin)
	tu.end_fill()
	tu.begin_fill()
	dessineTriangle(longueur, x - longueur / 10,
	                y + 3 / 2 * longueur + math.sqrt(longueur ** 2 / 4 + longueur ** 2) - 1 + longueur, couleurSapin)
	tu.end_fill()


def nuages_ensemble():
	"""
	Permet de dessiner l'ensemble
	"""
	NUAGES = (
		(-780, 180, rd.randint(1, 2)),
		(-595, 295, rd.randint(1, 2)),
		(-340, 270, rd.randint(1, 2)),
		(-130, 320, rd.randint(1, 2)),
		(120, 230, rd.randint(1, 2)),
		(370, 280, rd.randint(1, 2)),
		(620, 320, rd.randint(1, 2))
	)

	for t in NUAGES:
		nuage(t[0], t[1], t[2])


def montagne(s, t):
	"""
	Dessine une montagne en fond à l'aide du Screen s et de la Turtle t
	:param s: La classe Screen à utiliser
	:type s: Screen()
	:param t: La tortue à utiliser
	:type t: Turtle()
	"""
	s.bgcolor(15, 135, 228)
	t.up()
	t.hideturtle()
	t.goto(-960, 55)
	t.down()
	t.begin_fill()
	t.color(8, 40, 100)
	t.goto(-500, 300)
	t.goto(0, 40)
	t.goto(350, 440)
	t.goto(960, 120)
	t.goto(960, -540)
	t.goto(-960, -540)
	t.goto(-960, 55)
	t.end_fill()


def arbres():
	"""
	Dessine tous les arbres du fond
	"""
	foret(50, -900, -500)
	sapin(50 * coeffMystere(1, 5), -60, -60)
	sapin(50 * coeffMystere(1, 5), -170, -100)
	sapin(50 * coeffMystere(1, 5), 60, -120)


def neige():
	""""
	Permet de tracer la neige

	"""
	tu.up()
	tu.hideturtle()
	tu.goto(-635, 228.4)
	tu.down()
	tu.begin_fill()
	tu.color('white')
	tu.goto(-360, 228.4)
	tu.goto(-500, 300)
	tu.goto(-635, 228.4)
	tu.end_fill()
	tu.up()
	tu.goto(270, 350)
	tu.down()
	tu.begin_fill()
	tu.color('white')
	tu.goto(525, 350)
	tu.goto(350, 440)
	tu.goto(270, 350)
	tu.end_fill()


def fond_():
	"""
	Permet de tracer le fond complet
	"""
	TAILLE_ECRAN = (1920, 1080)
	t = tu.Turtle()
	s = tu.Screen()
	s.colormode(255)
	s.screensize(TAILLE_ECRAN[0], TAILLE_ECRAN[1])
	t.speed(0)
	montagne(s, t)
	neige()
	arbres()
	nuages_ensemble()


if __name__ == "__main__":
	tu.tracer(0, 0)
	fond_()
	tu.done()
	tu.exitonclick()
