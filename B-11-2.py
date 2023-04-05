import pyxel
import math
import random

pyxel.init(200,200)


score = 0
gameover = 0
balls = 1

class Ball:
    speed = 3
    def __init__(self):
        self.ballx = random.randint(0, 199)
        self.bally = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle) 
        self.vy = math.sin(angle) 

target = [Ball(), Ball(), Ball()]  #3個のボールを要素とするリストを変数に代入

class Pad: 
    def __init__(self):
        padx = 100


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
    global padx, score, gameover, target, balls, Ball, Pad

    for i in range(0, balls): 

        target[i].ballx += target[i].vx * Ball.speed
        target[i].bally += target[i].vy * Ball.speed

        if target[i].ballx >= 200:
            target[i].vx = - target[i].vx
        if target[i].ballx <= 0:
            target[i].vx = - target[i].vx

        if (pyxel.mouse_x - 20 <= target[i].ballx <=pyxel.mouse_x + 20) and target[i].bally >= 195:
            score += 1
            Ball.speed += 1
            target[i].bally = 0
            target[i].ballx = random.randint(0, 199)
            angle = math.radians(random.randint(30, 150))
            target[i].vx = math.cos(angle)
            target[i].vy = math.sin(angle)
            pyxel.play(0, 0)


        if target[i].bally >= 200:
            target[i].ballx = 100
            target[i].bally = 0
            target[i].vx = 0.866
            gameover += 1
            target[i].ballx = random.randint(0, 199)
            angle = math.radians(random.randint(30, 150))
            target[i].vx = math.cos(angle)
            target[i].vx = math.sin(angle)
            pyxel.play(0, 1)

        if score == 10:
            balls = 2
            Ball.speed = 3
        if score == 20:
            balls = 3
            Ball.speed = 3
        if score == 30:
            balls = 4
            Ball.speed = 3


        Pad.padx = pyxel.mouse_x


def draw():
    global padx, score, gameover, target, balls, Pad
    pyxel.cls(7)
    for i in range(0, balls):
        pyxel.circ(target[i].ballx, target[i].bally, 10, 6)
    pyxel.rect(Pad.padx-20, 195, 40, 5, 14)

    if gameover >= 10:
        pyxel.cls(1)
        pyxel.text(80, 100, "GAME OVER", 7)
        bally = [0, 0, 0]
        pyxel.stop()

    pyxel.text(10, 10, "Score:" + str(score), 1)

pyxel.run(update, draw)
