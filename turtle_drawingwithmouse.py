import turtle

t = turtle.Turtle("turtle")
s = turtle.Screen()
t.speed(-1)
t.width(10)

def dragging(x, y):  #  These parameters will be the mouse position
    t.ondrag(None)   # Ondrag = This function is used to bind fun to mouse-move event on this turtle on canvas ( stops backtracking )
    t.setheading(t.towards(x, y))  # Dit zet de richting van u turtle naar(towards) u x, y. Dus dit is als we iets willen tekenen dat de positie altijd in de richting is van ons muis 
    t.goto(x, y)  # This method is used to move the turtle to an absolute position
    t.ondrag(dragging) # Hier zie je dat ik dragging heb gebruikt voor dat hij die functie dragging blijft gebruiken tijdens het tekenen

def clickRight(x, y):
    t.clear()   # Dit is als je op u rechtermuis knop drukt na het tekenen dat alles weggaat dus eigenlijk alles word clear.

def main():  # This will run the program
    turtle.listen()
    
    t.ondrag(dragging)  # When we drag the turtle object call dragging
    turtle.onscreenclick(clickRight, 3)  # Dit is als je op u scherm drukt met u rechtermuis dan cleared hij alles , 3 = rechtermuis

    s.mainloop()  # This will continue running main() 

main()
