import turtle
import sys

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)
        t.right(120)
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)

def koch_snowflake(length, level):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-length/2, length/3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python koch_snowflake.py <length> <level>")
        sys.exit(1)

    try:
        length = float(sys.argv[1])
        level = int(sys.argv[2])
    except ValueError:
        print("Please provide valid numerical values for length and level.")
        sys.exit(1)

    koch_snowflake(length, level)
