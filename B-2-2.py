import pyxel
pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0, 200, 10):
    pyxel.line(a, 0, 0, 200-a, 0)

for a in range(0, 200, 10):
    pyxel.line(0, a, 200-a, 0, 0)

    pyxel.flip()


pyxel.show()
