import pyxel

pyxel.init(200, 200)
pyxel.cls(7)


for a in range(0, 201, 20):
    for b in range(0, 201, 20):
        pyxel.line(b, 0, a, 200, 0)

    pyxel.flip()


pyxel.show()


# pyxel.init(200, 200)
# pyxel.cls(7)
# for b in range(10, 200, 20):
#     for a in range(10, 200, 20):
#         pyxel.circ(a, b, 10, 0)
# pyxel.show()
