import turtle

def draw_square(t, size, color):
    t.color(color)
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_triangle(t, size, color):
    t.color(color)
    for _ in range(3):
        t.forward(size)
        t.right(120)

def draw_circle(t, size, color):
    t.color(color)
    t.circle(size)

def clear_drawing(t):
    t.clear()

screen = turtle.Screen()
t = turtle.Turtle()

while True:
    shape = input("Enter the shape to draw (square/triangle/circle) or 'clear' to clear: ").strip().lower()
    if shape == 'clear':
        clear_drawing(t)
    else:
        size = int(input("Enter the size: "))
        color = input("Enter the color: ").strip().lower()
        if shape == 'square':
            draw_square(t, size, color)
        elif shape == 'triangle':
            draw_triangle(t, size, color)
        elif shape == 'circle':
            draw_circle(t, size, color)
        else:
            print("Invalid shape")
    cont = input("Do you want to continue? (yes/no): ").strip().lower()
    if cont == 'no':
        break

turtle.done()
