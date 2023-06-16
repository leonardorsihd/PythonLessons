import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Configuração da janela de jogo
wn = turtle.Screen()
wn.title("Jogo da Cobra")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cabeça da cobra
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Comida da cobra
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Placar
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Pontuação: 0  Maior Pontuação: 0", align="center", font=("Courier", 24, "normal"))

# Funções para movimentar a cobra
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Configuração dos controles do teclado
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Loop principal do jogo
while True:
    wn.update()

    # Verificar colisões com a parede
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # Esconder os segmentos
        for segment in segments:
            segment.goto(1000, 1000)

        # Limpar a lista de segmentos
        segments.clear()

        # Resetar a pontuação
        score = 0

        # Resetar o delay
        delay = 0.1

        pen.clear()
        pen.write("Pontuação: {}  Maior Pontuação: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

    # Verificar colisão com a comida
    if head.distance(food) < 20:
        # Mover a comida para uma posição aleatória
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Adicionar um segmento à aaa
