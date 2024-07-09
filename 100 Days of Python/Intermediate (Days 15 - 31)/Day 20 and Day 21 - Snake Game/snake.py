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
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.generate_part(pos=position)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    
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
            self.get_part(seg_index).goto(x = new_x, y = new_y)

        self.head.forward(MOVE_DISTANCE)
    
    # movement commands
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def move_left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)
    def move_right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def get_part(self, index):
        return self.segments[index]
    
    def length(self):
        return len(self.segments)
