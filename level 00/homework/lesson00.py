from turtle import*
#გავაკეთოთ სახლი
width(8)
color("Pink")
begin_fill()
forward(200)

right(90)
forward(200)

right(90)
forward(200)

right(90)
forward(200)

right(90)
forward(200)
end_fill()
# გადაიტანეთ პასტა კარების დასახატად
penup()
goto(125,-200)
pendown()

# დავხატთ კარები
color("red")
begin_fill()


left(90)
forward(120)
left(90)
forward(50)
left(90)
forward(120)
end_fill()
#გადავიტანოთ სახურავზე
penup()
goto(0,0)
pendown()
#davxatot saxuravi
color("green")
begin_fill()
left(145)
forward(140)
right(97)
forward(160)
end_fill()
exitonclick()