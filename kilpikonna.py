import turtle

joku = turtle.Turtle()

def drawstar(pituus):
    for numero in range(0, 4):
        turtle.forward(pituus)
        turtle.right(145)

def suorakulmio(leveys, pituus, alkuX, alkuY, vari):
    turtle.begin_fill()
    turtle.speed(500)
    turtle.color(vari)
    turtle.setpos(alkuX, alkuY)
    turtle.setheading(0)
    turtle.forward(leveys)
    turtle.right(90)
    turtle.forward(pituus)
    turtle.right(90)
    turtle.forward(leveys)
    turtle.right(90)
    turtle.forward(pituus)
    turtle.end_fill()

suorakulmio(90, 80, -40, 100, "gray")

suorakulmio(20, 50, -50, -50, "gray")

suorakulmio(20, 50, 50, -50, "gray")

suorakulmio(80, 90, -40, 20, "gray")

turtle.done()