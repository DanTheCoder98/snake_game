import turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.move_distance = 20
        self.create_snake()

    def create_snake(self):
        for position in self.starting_positions:
            new_segment = turtle.Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.segments[0].forward(self.move_distance)

