import turtle as tu

# dessine une croix dans le carré de largeur l dont le point en bas
# à gauche est (x,y), avec la tortue t
def dessineCroix(x,y,l,c,t):
    """"
    x:int position en abscisse 
    y:int position en ordonnée
    l:int longueur 
    c:str or tuple  couleur 
    t:turtle
    Fonction pour dessiner une croix
    """
    t.up()
    t.goto(x,y)
    t.down()
    t.color(c)
    t.width(5)
    t.goto(x+l,y+l)
    t.up()
    t.goto(x+l,y)
    t.down()
    t.goto(x,y+l)
    t.width(1)

# dessine une allumette avec la tortue t
def dessineAllumette(x,y,l,c,t):
    """"
    x:int position en abcisse 
    y:int position en ordonnée
    l:int longueur de l'allumette
    c:str or tuple  couleur de l'allumette
    t:turtle
    fonction pour dessiner une allumette
    """
    t.up()
    t.goto(x,y)
    t.down()
    t.color(c)
    t.setheading(90)
    t.width(20)
    t.forward(l)
    t.width(30)
    t.color("red")
    t.forward(2)

def dessinePaquet(x, y, l, c, t, nb):
    """"
    x:int position en abcisse 
    y:int position en ordonnée
    l:int longueur de l'allumette
    c:str or tuple  couleur de l'allumette
    t:turtle
    nb:int nombre d'allumette dans le paquet
    Fonction reprennant la fonction dessineAllumette() pour dessiner un paquet d'allumette
    """
    for i in range(nb):
        dessineAllumette(x+i*50,y,l,c,t)


def couronne(s) -> None:
    """
    fonction pour dessiner une couronne à la fin lorsque le joueur gagne
    """
    s.clear()
    s.colormode(255)
    tu.hideturtle()
    tu.color(236, 228, 0)
    tu.up()
    tu.goto(-100, -100)
    tu.seth(0)
    tu.down()
    tu.forward(215)
    tu.left(90)
    tu.forward(200)
    pointe(26.57)
    pointe(53.13)
    tu.setheading(270)
    tu.forward(200)


def pointe(angle):
    """
    angle:float
    dessine une pointe pour le dessin de la couronne 
    fonction reutilisé danns la fonction couronne()
    """
    tu.left(180 - angle)
    tu.forward(120)
    tu.right(180 - 53.13)
    tu.forward(120)
