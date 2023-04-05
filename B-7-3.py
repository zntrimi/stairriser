import pyxel

pyxel.init(200,200)
pyxel.mouse(True)

x=0
y=0
z=0
u=0

def update():
    global x, y, z, u

    if pyxel.btnp(pyxel.KEY_SPACE):
        x = pyxel.mouse_x
        y = pyxel.mouse_y

    if pyxel.btn(pyxel.KEY_SPACE):
        z = pyxel.mouse_x
        u = pyxel.mouse_y


def draw():
    global x, y, z, u
    pyxel.cls(7)
    pyxel.line(x, y, z, u, 0)



pyxel.run(update, draw)
