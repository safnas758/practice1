import turtle as t

t.bgcolor("light blue")

def draw_side(height,width): #sides of main rectangle
    t.penup()
    t.goto(height/2,0)       #position of rectangle
    t.pendown()
    t.fillcolor("red")       #color of rectangle
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




    


def draw_circle(height, width, radius, color): # for the main white circle in th middle
    t.penup()
    t.goto(0,width/3)                          #positioning it to the middle of the rectangle
    t.pendown()
    t.fillcolor(color)                         #color of the circle
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()
    t.goto(-height/2,width)
    t.left(180)
    t.forward(10)
    t.pendown()

def draw_flagpole(length):            #for the flag pole
    t.left(90)
    t.pensize(5)                     #size of the pole
    t.forward(length*2)               #length of the pole

def draw_flag2(height,width):      # for the small flag right next to the main one
    
    t.penup()
    t.left(90)
    t.goto(200,0)      #position of the rectangle 
    t.left(270)
    t.pendown()
    t.pensize(1)
    t.fillcolor("red")   #color of the rectangle
    t.begin_fill()
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.end_fill()

def draw_circle2():    #for the white circle in the middle of the small flag
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

def draw_pole2():    # pole of the small flag
    t.left(90)
    t.penup()
    t.pensize(5)     #size of the pole
    t.pendown()
    t.forward(140)   #lenth of the pole

    




   

def main():           #used to call out functions

    draw_side(200,100)                #calling out the rectangle of the main flag
    draw_circle(200,100,20,"white")   #calling out the circle of the main flag
    draw_flagpole(100)                #calling out the pole of the main flag

    #for the small flag 
    draw_flag2(70,150)  #calling out the rectangle of the small flag
    draw_circle2()     #calling out the small white circle of the small flag 
    draw_pole2()       #calling out the pole of the small flag

    
    input("enter any key to exit") #used to end the drawing by entering any key in the keyboard

main() #calling out every function to show to drawing of two flag