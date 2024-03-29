from turtle import *
from random import randrange
from freegames import square, vector

screen = Screen()
screen.setup(402, 402)

# First food will spawn in middle
food = vector(0, 0)

# Snake will spawn slightly to the right of food
snake = [vector(10, 0)]

# Initial direction of movement is set to downwards
aim = vector(0, -10)

___ change(x, y):
    "Change snake direction."
    # Function is called on key press
    # Changes aim.x and aim.y, which gets passed into head.move in move() function
    aim.x = x
    aim.y = y

___ inside(head):
    "Return True if head inside boundaries."
    # The boundary is between (-200, -200) and (190, 190)
    # Think of it as a large square
    return -200 < head.x < 190 and -200 < head.y < 190

___ move():
    "Move snake forward one segment."
    # Makes the snake continue moving forward even without input
    head = snake[-1].copy()
    head.move(aim)

    # Game over if head is out of bounds or hits body
    __ not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        ______ # What must you include at the end of a function?

    snake.append(head)

    # Randomly decides next location of new food after eating previous food
    # If position of head is equal to position of food, the snake will grow
    # New food will appear in a new random position
    __ head __ food:
        print('Snake:', ___(snake)) # What allows you to count the number of elements in a list?
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    ____:
        snake.pop(0)

    clear()

    # Creates the snake using combination of squares (hence for loop)
    # Gains +1 body per food eaten, starts at 1
    ___ body in snake:
        square(body.x, body.y, 9, 'green')

    # Food is just 1 square
    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 100)


hideturtle()
screen.tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right') # affects x vector positively
onkey(lambda: change(-10, 0), 'Left') # affects x vector negatively
onkey(lambda: change(0, 10), 'Up') # affects y vector positively
onkey(lambda: change(0, -10), 'Down') # affects y vector negatively
move()
done()
