import turtle as tu 
def initialize():
 tu.speed(0)
 tu.delay(0)
 tu.tracer(0,0)
 tu.hideturtle()
 return tu
def finish():
 tu.update()
 tu.done()
def dessinePolygone(cotes, longueur, x, y, t, couleur):
    """

    cotes:int nombre de cotes
    longueur:int longueur 
    x:int position en abcisse
    y:int position en ordonnée
    t turtle
    couleur:tuple 
    fonction pour dessinner un polygone quelconque 

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
    x:int position en abscisse
    y:int position en ordonnée
    t turtle
    couleur:str or tuple 
    longueur:float/int
    Fonction pour dessiner un cercle

    """
    t.color(couleur)
    t.begin_fill()
    dessinePolygone(250, longueur, x, y, t, couleur)
    t.end_fill()

initialize()
dessineCercle(0,0,tu,'red',0.1)
finish()