from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
EAST = 0
WEST = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.generate_part(pos=position)
            
    
    def generate_part(self, pos):
        snake_body = Turtle("square")
        snake_body.penup()
        snake_body.color("white")
        snake_body.goto(pos)
        self.segments.append(snake_body)

    def move(self):
        for seg_index in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_index-1].xcor()
            new_y = self.segments[seg_index-1].ycor() 
            self.segments[seg_index].goto(x = new_x, y = new_y)

        self.get_part(0).forward(MOVE_DISTANCE)
    
    # movement commands
    def move_up(self):
        head = self.get_part(0)
        if head.heading() != DOWN:
            head.setheading(UP)
    def move_down(self):
        head = self.get_part(0)
        if head.heading() != UP:
            head.setheading(DOWN)
    def move_left(self):
        head = self.get_part(0)
        if head.heading() != EAST:
            head.setheading(WEST)
    def move_right(self):
        head = self.get_part(0)
        if head.heading() != WEST:
            head.setheading(EAST)

    def get_part(self, index):
        return self.segments[index]
