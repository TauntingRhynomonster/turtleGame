from turtle import *
t = Turtle()
scoreT = Turtle()
myScreen = scoreT.getscreen()
scoreT.penup()
scoreT.goto(myScreen.window_width() / 2 - 200, myScreen.window_height()/2-50)
scoreT.hideturtle()
score = 0

def updateScore():
	scoreT.clear()
	scoreT.write("Score: " + str(score),False,"left",font=("Arial",20,"normal"))

updateScore()

myScreen.mainloop()