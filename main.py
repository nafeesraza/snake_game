import time
import turtle as t
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
src = t.Screen()
src.setup(600, 600)
src.title("My Snake Game")
src.tracer(0)

snake = Snake()
food = Food()
my_score=ScoreBoard()
src.listen()
src.onkey(snake.up, "Up")
src.onkey(snake.down, "Down")
src.onkey(snake.left, "Left")
src.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    src.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food and increase the score
    if snake.head.distance(food) < 20:
        snake.extend()
        food.refresh()
        my_score.increase_score()

    # Detect collision with wall
    if (snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or
            snake.head.ycor() > 290):
        game_is_on=False
        my_score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on=False
            my_score.game_over()


src.exitonclick()
