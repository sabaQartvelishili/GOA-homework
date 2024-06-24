from turtle import *
speed(30)

width(5)

color("gray")
begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
left(90)

end_fill()


color("brown")

begin_fill()

forward(120)
right(90)

forward(60)
right(90)

forward(120)

end_fill()

penup()
goto(200, 200)
pendown()

color("red")

begin_fill()

right(150)
forward(200)

left(120)
forward(200)

end_fill()

begin_fill()
penup()
goto(60, 130)
pendown()

color("yellow")
begin_fill()
right(60)
forward(45)

right(90)
forward(45)

right(90)
forward(45)

right(90)
forward(45)

right(90)
forward(45)

penup()
goto(140, 130)
pendown()

right(90)
forward(45)

right(90)
forward(45)

right(90)
forward(45)

right(90)
forward(45)
end_fill()

color("brown")

penup()
goto(200, 200)
pendown()

forward(200)

penup()
goto(70, 0)
pendown()

right(180)
forward(60)

color("yellow")

penup()
goto(120, 60)
pendown()
forward(1)
penup()
goto(1000, 1000)
pendown()

exitonclick()