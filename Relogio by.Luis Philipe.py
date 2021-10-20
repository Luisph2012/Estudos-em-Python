from turtle import *
import turtle
import time
wndw = turtle.Screen()
wndw.bgcolor("black")
wndw.title("Relogio")
wndw.tracer(0)
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)
def corpo():
    raio = 200
    minuto = 10
    hora = 20
    for i in range(60):  
        pu()
        fd(raio)
        pencolor("white")
        if i % 5 == 0:
            pd()
            width(3)
            fd(hora)
            bk(hora)
        else:
            width(1)
            fd(hora - minuto)
            pd()
            fd(minuto)
            bk(minuto)
            pu()
            bk(hora-minuto)
        pu()
        bk(raio)
        rt(6)
corpo()
turtle.hideturtle()
def ponteiro(hr, mn, sec, pen):
    hands = [("white", 80, 12), ("white", 150, 60), ("red", 110, 60)]
    time_set = (hr, mn, sec)
    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part/hand[2])*360
        pen.penup()
        pen.goto(0, 0)
        pen.color(hand[0])
        pen.setheading(90)
        pen.rt(angle)
        pen.pendown()
        pen.fd(hand[1])
while True:
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    ponteiro(hr, mn, sec, pen)
    wndw.update()
    time.sleep(1)
    pen.clear()
wndw.mainloop()
update()

