import pyxel
import math
import random

pyxel.init(200,200)

ballx = 100
bally = 0
angle = 0
vx = 0.866
vy = 0.5
speed = 5
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
    global ballx, bally, vx, vy, speed, padx, score, angle



    ballx += vx*speed
    bally += vy*speed
    if ballx >= 200:
        vx = - vx
    if ballx <= 0:
        vx = - vx


    if (pyxel.mouse_x - 20 <= ballx <=pyxel.mouse_x + 20) and bally >= 195:
        score += 1
        speed += 1
        bally = 0

        ballx = random.randint(0, 199)

        angle = math.radians(random.randint(30, 150))
        vx = math.cos(angle)
        vy = math.sin(angle)
        pyxel.play(0, 0)


    if bally >= 200:
        ballx = 100
        bally = 0
        vx = 0.866

        speed += 1

        ballx = random.randint(0, 199)

        angle = math.radians(random.randint(30, 150))
        vx = math.cos(angle)
        vy = math.sin(angle)
        pyxel.play(0, 1)





    padx = pyxel.mouse_x


def draw():
    global ballx, bally, vx, vy, padx, score
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(10, 10, "Score:" + str(score), 1)




pyxel.run(update, draw)
