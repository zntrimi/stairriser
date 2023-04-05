import pyxel
import math
import random

pyxel.init(200,200)
ballx = [0]
gameover = 0

for i in range(0, len(ballx)):
    ballx[i] = random.randint(0, 199)
bally = [0]
vx = [0]
vy = [0]
for i in range(0, len(ballx)):
    angle = math.radians(random.randint(30, 150))
    vx[i] = math.cos(angle)
    vy[i] = math.sin(angle)
speed = 2

padx = 100
score = 0
numberofballs = 0
numberofballss = 0

randcolour = 4

padspeed = 1


# b for bonus ball to get extra points
bballcount = 0 #ランダムでボールが生成される。
bballx = 0
bbally = 0
bangle = 0
bvx = 0.866
bvy = 0.5
randomgoing = 0



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
    global ballx, bally, vx, vy, speed, padx, score, angle, gameover, numberofballs, numberofballss, bballcount, bballx, bbally, bangle, bvy, bvx, randomgoing, randcolour, padspeed

    for i in range(0, len(ballx)):
        ballx[i] += vx[i]*speed
        bally[i] += vy[i]*speed
        if ballx[i] >= 200:
            vx[i] = - vx[i]
        if ballx[i] <= 0:
            vx[i] = - vx[i]



        if (padx - 20 <= ballx[i] <=padx + 20) and bally[i] >= 195:
            score += 1
            speed += 1
            bally[i] = 0

            ballx[i] = random.randint(0, 199)

            angle = math.radians(random.randint(30, 150))
            vx[i] = math.cos(angle)
            vy[i] = math.sin(angle)
            pyxel.play(0, 0)

            bballcount = random.randint(0, 10)
            randcolour = random.randint(1, 14)

            print(bballcount)


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

            bballcount = random.randint(8, 10)

            print(bballcount)



        if score == 10:
            numberofballs += 1

        if score == 20:
            numberofballss += 1



        if numberofballs == 1:
            ballx.append(random.randint(0, 199))
            bally.append(random.randint(0, 199))
            angle = math.radians(random.randint(30, 150))
            vx.append (math.cos(angle))
            vy.append (math.sin(angle))
            speed = 5


        if numberofballss == 1:
            ballx.append(random.randint(0, 199))
            bally.append(random.randint(0, 199))
            angle = math.radians(random.randint(30, 150))
            vx.append (math.cos(angle))
            vy.append (math.sin(angle))
            speed = 5


    if bballcount == 10:

        # bballx = random.randint(0, 199)

        # bangle = math.radians(random.randint(30, 150))
        # bvx = math.cos(bangle)
        # bvy = math.sin(bangle)
        # pyxel.play(0, 1)               


        bballx += bvx*4
        bbally += bvx*4


        if bballx >= 200:
            bvx = - bvx
        if bballx <= 0:
            bvx = - bvx
        padspeed = 2
        
        

    else:
        padspeed = 1
    


    if (padx - 20 <= bballx <= padx + 20) and bbally >= 195:

        score += 1
        bbally = 0
        bballcount = 0


    # padx = pyxel.mouse_x

    if pyxel.btn(pyxel.KEY_RIGHT) :
        padx += 6

    if pyxel.btn(pyxel.KEY_LEFT) :
        padx -= 6



def draw():
    global ballx, bally, vx, vy, padx, score, gameover, randcolour
    pyxel.cls(randcolour - 1)
    for i in range(0, len(ballx)):
        pyxel.circ(ballx[i], bally[i], 10, randcolour)
    pyxel.rect(padx-20, 195, 40, 5, 14)

    # pyxel.circ(bbally, bbally, 5, 4)
    pyxel.rect(padx-20, 195, 40, 5, 15)

    if gameover >= 10:
        pyxel.cls(1)
        pyxel.text(80, 100, "GAME OVER", 7)
        bally = [0, 0, 0]

    pyxel.text(10, 10, "Score:" + str(score), 1)




pyxel.run(update, draw)
