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
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)
                # draw a polygon at a random location, orientation, color, and border line thickness
                
                num_sides = random.randint(3, 3)
                for i in range(1,30): 
                        size = random.randint(50, 150)
                        orientation = random.randint(0, 90)
                        location = [random.randint(-300, 300), random.randint(-200, 200)]
                        color = self.get_new_color()
                        border_size = random.randint(1, 10)
                        self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                        reduction_ratio = 0.618
                        
                        
                            
                        
                        turtle.penup()
                        turtle.forward(size*(1-reduction_ratio)/2)
                        turtle.left(90)
                        turtle.forward(size*(1-reduction_ratio)/2)
                        turtle.right(90)
                        location[0] = turtle.pos()[0]
                        location[1] = turtle.pos()[1]
                        
                        
                      

            
                        self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                turtle.done()
                
            elif self.choice == 2:
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)
                # draw a polygon at a random location, orientation, color, and border line thickness
                num_sides = random.randint(3, 5) # triangle, square, or pentagon
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = self.get_new_color()
                border_size = random.randint(1, 10)
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                reduction_ratio = 0.618

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.left(90)
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

    # draw the second polygon embedded inside the original 
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                turtle.done()
                
            elif self.choice == 3:
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)
                # draw a polygon at a random location, orientation, color, and border line thickness
                num_sides = random.randint(3, 5) # triangle, square, or pentagon
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = self.get_new_color()
                border_size = random.randint(1, 10)
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                reduction_ratio = 0.618

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.left(90)
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

    # draw the second polygon embedded inside the original 
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                turtle.done()
                
            elif self.choice == 4:
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)
                # draw a polygon at a random location, orientation, color, and border line thickness
                num_sides = random.randint(3, 5) # triangle, square, or pentagon
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = self.get_new_color()
                border_size = random.randint(1, 10)
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                reduction_ratio = 0.618

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.left(90)
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

    # draw the second polygon embedded inside the original 
                self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                turtle.done()
                
            elif self.choice == 5:
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)
                # draw a polygon at a random location, orientation, color, and border line thickness
                
                num_sides = random.randint(3, 3)
                for i in range(1,20): 
                        size = random.randint(50, 150)
                        orientation = random.randint(0, 90)
                        location = [random.randint(-300, 300), random.randint(-200, 200)]
                        color = self.get_new_color()
                        border_size = random.randint(1, 10)
                        self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                        
                        for i in range(1,3):
                            reduction_ratio = 0.618
                            
                            
                                
                            
                            turtle.penup()
                            turtle.forward(size*(1-reduction_ratio)/2)
                            turtle.left(90)
                            turtle.forward(size*(1-reduction_ratio)/2)
                            turtle.right(90)
                            location[0] = turtle.pos()[0]
                            location[1] = turtle.pos()[1]
                            
                            
                        

                            self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                turtle.done()
                
            elif self.choice == 6:
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)
                # draw a polygon at a random location, orientation, color, and border line thickness
                
                num_sides = random.randint(4, 4)
                for i in range(1,20): 
                        size = random.randint(50, 150)
                        orientation = random.randint(0, 90)
                        location = [random.randint(-300, 300), random.randint(-200, 200)]
                        color = self.get_new_color()
                        border_size = random.randint(1, 10)
                        self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                        
                        for i in range(1,3):
                            reduction_ratio = 0.618
                            
                            
                                
                            
                            turtle.penup()
                            turtle.forward(size*(1-reduction_ratio)/2)
                            turtle.left(90)
                            turtle.forward(size*(1-reduction_ratio)/2)
                            turtle.right(90)
                            location[0] = turtle.pos()[0]
                            location[1] = turtle.pos()[1]
                            
                            
                        

                            self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                turtle.done()
            elif self.choice == 7:
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)
                # draw a polygon at a random location, orientation, color, and border line thickness
                
                num_sides = random.randint(5, 5)
                for i in range(1,20): 
                        size = random.randint(50, 150)
                        orientation = random.randint(0, 90)
                        location = [random.randint(-300, 300), random.randint(-200, 200)]
                        color = self.get_new_color()
                        border_size = random.randint(1, 10)
                        self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                        
                        for i in range(1,3):
                            reduction_ratio = 0.618
                            
                            
                                
                            
                            turtle.penup()
                            turtle.forward(size*(1-reduction_ratio)/2)
                            turtle.left(90)
                            turtle.forward(size*(1-reduction_ratio)/2)
                            turtle.right(90)
                            location[0] = turtle.pos()[0]
                            location[1] = turtle.pos()[1]
                            
                            
                        

                            self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                turtle.done()
                
            elif self.choice == 8:
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)
                # draw a polygon at a random location, orientation, color, and border line thickness
                
                
                for i in range(1,20): 
                        num_sides = random.randint(3, 5)
                        size = random.randint(50, 150)
                        orientation = random.randint(0, 90)
                        location = [random.randint(-300, 300), random.randint(-200, 200)]
                        color = self.get_new_color()
                        border_size = random.randint(1, 10)
                        self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                        
                        for i in range(1,3):
                            reduction_ratio = 0.618
                            
                            
                                
                            
                            turtle.penup()
                            turtle.forward(size*(1-reduction_ratio)/2)
                            turtle.left(90)
                            turtle.forward(size*(1-reduction_ratio)/2)
                            turtle.right(90)
                            location[0] = turtle.pos()[0]
                            location[1] = turtle.pos()[1]
                            
                            
                        

                            self.draw_polygon(num_sides, size, orientation, location, color, border_size)
                turtle.done()



choice = int(input('Which art do you want to generate? Enter a number between 1 to 8,inclusive: '))
play = picture(choice)
play.run()