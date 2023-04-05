import pyxel
import math
import random

pyxel.init(200,200)
ballx = [0, 0, 0]
gameover = 0
for i in range(0, 3):
    ballx[i] = random.randint(0, 199)
bally = [0, 0, 0]
vx = [0, 0, 0]
vy = [0, 0, 0]
for i in range(0, 3):
    angle = math.radians(random.randint(30, 150))
    vx[i] = math.cos(angle)
    vy[i] = math.sin(angle)
speed = 2

padx = 100
score = 0



pyxel.sound(0).set(
    note="c3e3g3c4c4", tone="s", volume="4", effect=("n" * 4 + "f"), speed=7
)
pyxel.sound(1).set(
    note="f3 b2 f2 b1  f1 f1 f1 f1",
    tone="p",
    volume=("4" * 4 + "4321"),
    effect=("n" * 7 + "f"),
    speed=9,
)

def update():
    global ballx, bally, vx, vy, speed, padx, score, angle, gameover

    for i in range(0, 3):
        ballx[i] += vx[i]*speed
        bally[i] += vy[i]*speed
        if ballx[i] >= 200:
            vx[i] = - vx[i]
        if ballx[i] <= 0:
            vx[i] = - vx[i]


        if (pyxel.mouse_x - 20 <= ballx[i] <=pyxel.mouse_x + 20) and bally[i] >= 195:
            score += 1
            speed += 1
            bally[i] = 0

            ballx[i] = random.randint(0, 199)

            angle = math.radians(random.randint(30, 150))
            vx[i] = math.cos(angle)
            vy[i] = math.sin(angle)
            pyxel.play(0, 0)


        if bally[i] >= 200:
            ballx[i] = 100
            bally[i] = 0
            vx[i] = 0.866
            gameover += 1

            speed += 1

            ballx[i] = random.randint(0, 199)

            angle = math.radians(random.randint(30, 150))
            vx[i] = math.cos(angle)
            vy[i] = math.sin(angle)
            pyxel.play(0, 1)

        padx = pyxel.mouse_x


def draw():
    global ballx, bally, vx, vy, padx, score, gameover
    pyxel.cls(7)
    for i in range(0,3):
        pyxel.circ(ballx[i], bally[i], 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)

    if gameover >= 10:
        pyxel.cls(1)
        pyxel.text(80, 100, "GAME OVER", 7)
        bally = [0, 0, 0]

    pyxel.text(10, 10, "Score:" + str(score), 1)




pyxel.run(update, draw)
