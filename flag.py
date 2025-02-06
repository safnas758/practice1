import turtle as t

t.bgcolor("light blue")

def draw_side(height,width):
    t.penup()
    t.goto(height/2,0)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()
    t.penup()
    t.goto(0,0)
    t.pendown()




    


def draw_circle(height, width, radius, color):
    t.penup()
    t.goto(0,width/3)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()
    t.goto(-height/2,width)
    t.left(180)
    t.forward(10)
    t.pendown()

def draw_flagpole(width):
    t.left(90)
    t.pensize(5)
    t.forward(width*2)

def draw_flag2(height,width):
    
    t.penup()
    t.left(90)
    t.goto(200,0)
    t.left(270)
    t.pendown()
    t.pensize(1)
    t.fillcolor("red")
    t.begin_fill()
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.end_fill()

def draw_circle2():
    t.penup()
    t.goto(275,-27)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.goto(190,0)
    t.pendown

def draw_pole2():
    t.left(90)
    t.penup()
    t.pensize(5)
    t.pendown()
    t.forward(140)

    




   

def main():

    draw_side(200,100)
    draw_circle(200,100,20,"white")
    draw_flagpole(100)

    draw_flag2(70,150)
    draw_circle2()
    draw_pole2()

    
    input("enter any key to exit")

main()