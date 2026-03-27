from turtle import *

# l want to paint a house

# step 1: draw a square

speed(6)

color("gray")

begin_fill()

width(7)

forward(200)

left(90)

forward(200)

left(90)

forward(200)

left(90)

forward(200)
end_fill()
#end of square

#start a door

left(90)

forward(70)

color("black")

left(90)

forward(90)

right(90)

forward(60)

right(90)

forward(90)

penup()

goto(200, 200)

pendown()

color("dark red")
begin_fill()
right(150)

forward(200)

left(120)

forward(200)
end_fill()
#end of house

#paint a grass

color("dark green")

penup()
goto(0, 0)
pendown()

right(60)

forward(480)

color("gray")

penup()
goto(200, 200)
pendown()
left(90)

forward(200)

left(90)
color("dark green")

begin_fill()

forward(270)

right(90)

forward(390)

right(90)

forward(950)

right(90)

forward(390)
end_fill()
#end of house

#begining window
color("black")

penup()

goto(90, 90)

right(90)

forward(10)

left(90)

forward(80)

left(90)

forward(30)

pendown()

left(90)
forward(40)

right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
penup()

forward(60)

pendown()

forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)






exitonclick()

