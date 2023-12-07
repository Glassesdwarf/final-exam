import random
import turtle
class picture:
    def __init__(self,choice):
        self.choice = choice
        
    def draw_polygon(self,num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360/num_sides)
        turtle.penup()
    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    def run(self):
        if self.choice == 1:
        elif self.choice == 2:
        elif self.choice == 3:
        elif self.choice == 4:
        elif self.choice == 5:
        elif self.choice == 6:
        elif self.choice == 7:
        elif self.choice == 8:
            
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
    

choice = int(input('Which art do you want to generate? Enter a number between 1 to 8,inclusive: '))
picture(choice)
picture.run