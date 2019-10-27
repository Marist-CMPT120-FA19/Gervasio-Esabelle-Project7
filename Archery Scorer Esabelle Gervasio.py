#Esabelle Gervasio
#Archery Scorer

from graphics import *
import math

def rad(point, dist):
    x=point.getX()-dist.getCenter().getX()
    y=point.getY()-dist.getCenter().getY()
    rad=math.sqrt(x*x+y*y)
    
    return rad <=dist.getRadius()
 
    
 
def main():
    #sets accumulator to zero
    score=0
    #Draws target
    win=GraphWin("Bullseye")
    red = Circle(Point(75,75), 50)
    red.setOutline("red")
    red.setFill("red")
    red.draw(win)
    
    blue = Circle(Point(75,75), 40)
    blue.setOutline("blue")
    blue.setFill("blue")
    blue.draw(win)
    
    white = Circle(Point(75,75), 30)
    white.setOutline("white")
    white.setFill("white")
    white.draw(win)
    
    black = Circle(Point(75,75), 20)
    black.setOutline("black")
    black.setFill("black")
    black.draw(win)
    
    yellow = Circle(Point( 75,75), 10)
    yellow.setOutline("yellow")
    yellow.setFill("yellow")
    yellow.draw(win)

    message= Text(Point(100,15), "Click to shoot an arrow")
    message.draw(win)

    #5 clicks with s sum of points            
    for i in range (5):
        p=win.getMouse()
                         
        if(rad(p, yellow)):
                score+=9
                
        elif(rad(p, black)):
                score+=7
                
        elif(rad(p, white)):
                score+=5
                
        elif(rad(p, blue)):
                score+=3
                
        elif(rad(p, red)):
                score+=1
                
        else:
                score+=0
          
    message.setText("Total score is: "+ str(score))
    win.getMouse()
    message.setText("click anywhere to quit")
    win.getMouse()
    win.close()
main()
        
