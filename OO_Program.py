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
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        reduction_ratio = 0.618
        # reposition the turtle and get a new location
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        turtle.done()
# adjust the size according to the reduction ratio
        size *= reduction_ratio
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360/num_sides)
        turtle.penup()
    def get_new_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    def run(self):
        if self.choice == 1:
            self.draw_polygon(3,60,size = random.randint(50, 150),orientation = random.randint(0, 90),location = [random.randint(-300, 300), random.randint(-200, 200)]
                              ,color=self.get_new_color,border_size = random.randint(1, 10))
           

    

choice = int(input('Which art do you want to generate? Enter a number between 1 to 8,inclusive: '))
picture(choice)
picture.run