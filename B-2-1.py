import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0, 101, 10):
    pyxel.line(a, 0, 100+a, 200, 0)
    pyxel.flip()
pyxel.show()





# for a in range(0, 201, 10 line space):
    # pyxel.line(0, a　こっちは始まり, 200, 200+a, 0 色)
