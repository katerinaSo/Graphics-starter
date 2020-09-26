from graphics import *

stage=GraphWin("swap places",800,800)

blue_cup=Rectangle(Point(100,10),Point(190,200)) 
red_cup=Rectangle(Point(250,10),Point(340,200))

blue_cup.setFill("blue")  
red_cup.setFill("red")
blue_cup.draw(stage) 
red_cup.draw(stage)

# your code for swap of cups' places using just names (variables)
   


red_cup.undraw()
blue_cup.undraw()
blue_cup.setFill("blue")
red_cup.setFill("red")
blue_cup.draw(stage)
red_cup.draw(stage)
