from turtle import Turtle
import random
COLORS=["red","blue","orange","yellow","green","purple","black"]
STARTING_MOVE_DISTANCE=5
MOVE_INCREMENT=10


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.all_cars=[]
        self.hideturtle()
        self.car_speed=STARTING_MOVE_DISTANCE


    def create_car(self):
         random_chance=random.randint(1,6)
         if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=2,stretch_len=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-260,260)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def level_up(self):
        self.car_speed+=MOVE_INCREMENT



