import turtle
import random

# Set the animation speed to the maximum
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.tracer(1)


class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(startx, starty)
        self.speed = 2

    def move(self):
        self.fd(self.speed)
        # Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    def is_collision(self, other):
        if other is None:
            return False
        if (self.xcor() >= (other.xcor() - 20)) and \
                (self.xcor() <= (other.xcor() + 20)) and \
                (self.ycor() >= (other.ycor() - 20)) and \
                (self.ycor() <= (other.ycor() + 20)):
            return True


class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 8
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        if self.speed > 1:
            self.speed -= 1


class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 10
        self.setheading(random.randint(0, 360))


class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 12
        self.setheading(random.randint(0, 360))

    def move(self):
        self.fd(self.speed)
        # Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)


class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"

    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):
        if self.status == "ready":
            self.goto(-1000, 1000)
        if self.status == "firing":
            self.fd(self.speed)
        # Border check
        if self.xcor() < -290 or self.xcor() > 290 or self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"


class Game:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()


# Create game and player
game = Game()
game.draw_border()
player = Player("triangle", "white", 0, 0)
enemy = Enemy("circle", "red", -100, 0)
missile = Missile("triangle", "yellow", 0, 0)
ally = Ally("square", "blue", 0, 0)

# Keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()

# Main game loop
while True:
    player.move()
    turtle.update()
    enemy.move()
    missile.move()
    ally.move()

    # Check for collision with the player
    if player.is_collision(enemy):
        player.lives -= 1
        x, y = random.randint(-250, 250), random.randint(-250, 250)
        enemy.goto(x, y)
        if player.lives == 0:
            print("Game Over!")
            break

    # Check for a collision between the missile and the enemy
    if missile.is_collision(enemy):
        x, y = random.randint(-250, 250), random.randint(-250, 250)
        enemy.goto(x, y)
        missile.status = "ready"

    # Check for a collision between the missile and the ally
    if missile.is_collision(ally):
        x, y = random.randint(-250, 250), random.randint(-250, 250)
        ally.goto(x, y)
        missile.status = "ready"
