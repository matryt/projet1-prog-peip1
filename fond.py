from turtle import *
from math import*
import random as rd
def dessinePolygone (nb_cotes,l,x,y,couleur) :
    up()
    color(couleur)
    goto(x,y)
    down()
    a=360/nb_cotes
    i=1
    while i <= nb_cotes :
        forward(l)
        left(a)
        i+=1
def dessineTriangle (l,x,y,couleur):
    dessinePolygone(3,l,x,y,couleur)

def sapin_forêt(l,x,y):
    hideturtle()
    begin_fill()
    dessinePolygone(4,l,x,y,'brown')
    end_fill()
    begin_fill()
    dessinePolygone(3,2*l,x-l/2,l,'green')
    end_fill()

def forêt(l,x,y,n):
    for i in range(rd.randint(1,9)):
        sapin_forêt(l,x+i*2*l,y)
def rectangle(l,x,y,couleur):
    up()
    goto(x,y)
    down()
    begin_fill()
    color(couleur)
    forward(l)
    left(90)
    forward(3/2*l)
    left(90)
    forward(l)
    left(90)
    forward(3/2*l)
    end_fill()
 


        



def sapin(l,x,y):
    hideturtle()
    begin_fill()
    rectangle(l,x,y,'brown')
    end_fill()
    setheading(0)
    begin_fill()
    up()
    dessineTriangle(2*l,x-l/2,3/2*l,'green')
    end_fill()
    begin_fill()
    dessineTriangle((3/2)*l,x-l/3,3/2*l+sqrt(l**2/4 + l**2)-1,'green')
    end_fill()
    begin_fill()
    dessineTriangle(l,x-l/4+10,3/2*l+sqrt(l**2/4 + l**2)-1+l,'green')
    end_fill()

sapin(60,0,0)

    
    
    
