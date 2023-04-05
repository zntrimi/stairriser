import pyxel
import math
import random

pyxel.init(200,200)

class Ball:
    speed = 3
    def __init__(self):
        self.x = random.randint(0, 199)
        self.y = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle) * Ball.speed
        self.vy = math.sin(angle) * Ball.speed

VarBall= [Ball(), Ball(), Ball()]
padx = 100
score = 0
miss = 0
balls = 1
receive = 0

pyxel.sound(0).set(note='c3e3g3c4c4', tone='s', volume='4', effect=('n' * 4 + 'f'), speed=7)
pyxel.sound(1).set(note='f3 b2 f2 b1  f1 f1 f1 f1',tone='p',volume=('4' * 4 + '4321'),effect=('n' * 7 + 'f'),speed=9,)

def update():
    global VarBall, padx, score, miss, balls, receive
    for i in range(0, balls):
        if VarBall[i].x >= 200 or VarBall[i].x <= 0:
            VarBall[i].vx= -VarBall[i].vx
        VarBall[i].x += VarBall[i].vx
        VarBall[i].y += VarBall[i].vy
        if VarBall[i].y >= 200:
            pyxel.play(0, 1)
            VarBall[i] = Ball()
            miss += 1
        padx = pyxel.mouse_x
        if VarBall[i].y >= 195 and padx-20 <= VarBall[i].x <= padx+20:
            pyxel.play(0,0)
            receive += 1
            VarBall[i] = Ball()
            score += 10
            if receive == 10 and balls < 3:
                balls += 1
                Ball.speed -= 2
                recieve = 0

def draw():
    global VarBall, padx, score, angle, miss, balls
    if miss >= 10:
        pyxel.text(80, 90, "Game Over", 0)
        pyxel.stop()
    else:
        pyxel.cls(7)
        for i in range(0, balls):
            pyxel.circ(VarBall[i].x, VarBall[i].y, 10, 6)
        pyxel.rect(padx-20, 195, 40, 5, 14)
        pyxel.text(10, 10, "score: " + str(score), 0)

pyxel.run(update, draw)