# Loic LAMOUR et Mathieu CUVELIER - Groupe 5

import turtle as tu
from math import sqrt


def dessinePolygone(cotes, longueur, x, y, t, couleur):
	"""
	Fonction pour dessiner un polygone régulier

	:param cotes: Nombre de côtés
	:type cotes: int
	:param longueur: Longueur de chaque côté
	:type longueur: int/float
	:param x: Position en abscisse
	:type x: int/float
	:param y: Position en ordonnée
	:type y: int/float
	:param t: La tortue à utiliser
	:type t: Turtle()
	:param couleur: Couleur dans laquelle dessiner le cercle
	:type couleur: str/tuple
	"""
	t.up()
	t.color(couleur)
	t.goto(x, y)
	t.down()
	t.seth(0)
	for i in range(cotes):
		t.forward(longueur)
		t.left(360 / cotes)


def dessineCercle(x, y, t, couleur, longueur):
	"""
	Fonction pour dessiner un cercle
	:param x: Position en abscisse
	:type x: int/float
	:param y: Position en ordonnée
	:type y: int/float
	:param t: La tortue à utiliser
	:type t: Turtle()
	:param couleur: Couleur dans laquelle dessiner le cercle
	:type couleur: str/tuple
	:param longueur: Longueur de chaque arc de cercle
	:type longueur: int/float
	"""
	t.color(couleur)
	t.begin_fill()
	dessinePolygone(250, longueur, x, y, t, couleur)
	t.end_fill()


def dessineDemiCercle(cotes, longueur, x, y, t, couleur):
	"""
	Fonction pour dessiner un polygone régulier

	:param cotes: Nombre de côtés
	:type cotes: int
	:param longueur: Longueur de chaque côté
	:type longueur: int/float
	:param x: Position en abscisse
	:type x: int/float
	:param y: Position en ordonnée
	:type y: int/float
	:param t: La tortue à utiliser
	:type t: Turtle()
	:param couleur: Couleur dans laquelle dessiner le cercle
	:type couleur: str/tuple
	"""
	t.up()
	t.begin_fill()
	t.color(couleur)
	t.goto(x, y)
	t.down()
	t.seth(180)
	for i in range(cotes // 2):
		t.forward(longueur)
		t.right(360 / cotes)
	t.right(90)
	t.forward(80 * longueur)
	t.end_fill()


def buisson(x, y, fruitsADessiner, fruitsManges, t):
	"""
	Fonction pour dessiner un buisson avec les fruits

	:param x: Position en abscisse
	:type x: int/float
	:param y: Position en ordonnée
	:type y: int/float
	:param fruits: Le nombre de fruits à dessiner
	:type fruits: int
	:param t: La tortue à utiliser
	:type t: Turtle()
	"""
	t.hideturtle()
	emplacements = [
		(x - 22.5, y + 20),
		(x - 7.5, y + 20),
		(x + 7.5, y + 20),
		(x + 22.5, y + 20),
		(x + 37.5, y + 20),
		(x + 52.5, y + 20),
		(x + 67.5, y + 20),
		(x - 22.5, y + 40),
		(x - 7.5, y + 40),
		(x + 7.5, y + 40),
		(x + 22.5, y + 40),
		(x + 37.5, y + 40),
		(x + 52.5, y + 40),
		(x + 67.5, y + 40)
	]
	for i in range(3):
		dessineCercle(x + 25 * i, y, t, (0, 86, 27), 1)
	for j in range(fruitsADessiner):
		dessineCercle(emplacements[0][0], emplacements[0][1], t, (196, 14, 0), 0.1)
		emplacements.pop(0)
	for k in range(fruitsManges):
		dessineDemiCercle(250, 0.13, emplacements[0][0], emplacements[0][1], t, (163, 163, 163))
		emplacements.pop(0)

def numero(coords, n, t, couleur):
	"""
	Permet d'écrire un numéro aux coordonnées spécifiées
	:param coords: Les coordonnées du texte
	:type coords: tuple
	:param n: Le numéro à afficher
	:type n: int
	:param t: La tortue à utiliser
	:type t: Turtle
	:param couleur: couleur texte
	:type couleur: str or tuple
	"""
	t.up()
	t.goto(coords[0], coords[1])
	t.down()
	t.color(couleur)
	t.write(f'Tas {str(n)}', align="center", font=('Arial', 16, "bold"))


def couronne(s) -> None:
	"""
	Fonction pour dessiner une couronne à la fin lorsque le joueur gagne

	:param s: La classe Screen sur laquelle dessiner
	:type s: Screen()
	"""
	s.clear()
	s.colormode(255)
	tu.hideturtle()
	initialize()
	tu.color(186, 180, 0)
	tu.width(2)
	tu.up()
	tu.goto(-100, -100)
	tu.seth(0)
	tu.down()
	tu.begin_fill()
	tu.forward(215)
	tu.left(90)
	tu.forward(200)
	pointe(26.57)
	pointe(53.13)
	tu.setheading(270)
	tu.forward(200)
	tu.end_fill()
	finish()


def pointe(angle):
	"""
	Dessine une pointe pour le dessin de la couronne
	Fonction réutilisée dans la fonction couronne()

	:param angle: L'angle de départ pour la pointe
	:type angle: int/float
	"""
	tu.left(180 - angle)
	tu.forward(120)
	tu.right(180 - 53.13)
	tu.forward(120)


def os(x, y, droite=True):
	"""
	Fonction pour dessiner un os de la tête de mort

	:param x: Position en abscisse
	:type x: int/float
	:param y: Position en ordonnée
	:type y: int/float
	:param droite: True si cela concerne l'os droit, False sinon
	:type droite: bool
	"""
	tu.up()
	tu.goto(x, y)
	tu.down()
	tu.width(10)
	tu.left(15)
	if droite:
		tu.forward(154.96)
	else:
		tu.forward(135.2)
	tu.right(70.47)
	tu.forward(42.64)
	tu.left(54.03)
	tu.forward(41.08)
	tu.left(45.28)
	tu.forward(49.92)
	tu.left(46.512)
	tu.forward(42.12)
	tu.left(39.02)
	tu.forward(34.32)
	tu.left(71.08)
	tu.forward(18.2)
	tu.left(180)
	tu.forward(18.2)
	tu.left(27.56)
	tu.forward(19.76)
	tu.left(54.61)
	tu.forward(55.12)
	tu.left(51.3)
	tu.forward(34.32)
	tu.left(42.74)
	tu.forward(50.96)
	tu.left(48.79)
	tu.forward(33.8)
	tu.left(18.55)
	tu.forward(29.12)
	tu.right(71.93)
	if not droite:
		tu.forward(154.96)
	else:
		tu.forward(135.2)
	tu.left(105.09)
	tu.down()
	tu.up()
	tu.forward(79.04)
	tu.forward(-79.04)
	tu.up()
	tu.goto(x, y)


def bouche(x, y, angle):
	"""
	Fonction pour dessiner une bouche de la tête de mort

	:param x: Position en abscisse
	:type x: int/float
	:param y: Position en ordonnée
	:type y: int/float
	:param angle: L'angle de départ
	:type angle: int/float
	"""
	tu.seth(angle)
	tu.right(90)
	tu.up()
	tu.goto(x, y)
	tu.down()
	tu.width(10)
	tu.forward(115.44000000000001)
	tu.seth(0)
	tu.forward(191.88)
	tu.seth(90)
	tu.forward(115.44000000000001)
	tu.forward(-46.800000000000004)

	for i in range(3):
		dent()

	tu.left(90)
	tu.forward(27.411428571428573)

	tu.up()
	tu.goto(x, y)
	tu.right(180)
	tu.up()
	tu.forward(191.88)
	tu.down()


def crane():
	"""
	Fonction pour dessiner le crâne de la tête de mort
	"""
	tu.width(10)
	tu.seth(45)
	tu.forward(100)
	tu.left(45)
	tu.forward(100)
	tu.left(45)
	tu.forward(100)
	tu.left(45)
	tu.forward(190)
	tu.left(45)
	tu.forward(100)
	tu.left(45)
	tu.forward(100)
	tu.left(45)
	tu.forward(100)


def yeux():
	"""
	Fonction pour dessiner des yeux
	"""
	tu.seth(90)
	tu.up()
	tu.forward(150)
	tu.right(90)
	tu.down()
	tu.width(10)
	rectangle(70, 40)
	tu.up()
	tu.forward(110)
	tu.down()
	rectangle(70, 40)


def rectangle(x, y):
	"""
	Fonction pour dessiner un rectangle

	:param x: La longueur du rectangle
	:type x: int/float
	:param y: La largeur du rectangle
	:type y: int/float
	"""
	tu.forward(x)
	tu.left(90)
	tu.forward(y)
	tu.left(90)
	tu.forward(x)
	tu.left(90)
	tu.forward(y)
	tu.left(90)


def initialize():
	"""
	Fonction pour initialiser Turtle de manière à réduire tous les délais de traçage et cacher Turtle.
	"""
	tu.speed(0)
	tu.delay(0)
	tu.tracer(0, 0)
	tu.hideturtle()
	return tu


def finish():
	"""
	Fonction pour mettre à jour la Turtle et récupérer instantanément les tracés de Turtle cachées grâce à initialize()
	"""

	tu.update()
	tu.done()


def tete(s):
	"""
	Fonction pour dessiner une tête de mort reprenant d'autres fonctions définies précédemment

	:param s: La classe Screen sur laquelle dessiner
	:type s: Screen()
	"""
	tu.hideturtle()
	s.clear()
	initialize()
	bouche(-110, -100, 0)
	crane()
	yeux()
	tu.seth(315)
	os(-110 + 191.88, -100)
	tu.seth(201)
	os(-110 - sqrt(5000), -100 + sqrt(5000), False)
	finish()


def dent():
	"""
	Permet de dessiner une dent de la tête de mort
	"""
	tu.left(90)
	tu.forward(27.411428571428573)
	tu.right(90)
	tu.forward(28.080000000000002)
	tu.forward(-56.160000000000004)
	tu.forward(28.080000000000002)
	tu.left(90)
	tu.forward(27.411428571428573)
	tu.right(90)
	tu.forward(19.24)
	tu.forward(-38.48)
	tu.forward(19.24)
