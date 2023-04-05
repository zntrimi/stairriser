# from random import randint を追加します
from random import randint
import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Pyxel Jump")

        pyxel.load("assets/jump_game.pyxres")

        # ここに雲を入れます
        self.far_cloud = [(-10, 75), (40, 65), (90, 60)]
        self.near_cloud = [(10, 25), (70, 35), (120, 15)]

        # ここに床を入れます i*60は床同士の隙間
        self.floor = [(i * 60, randint(8, 104), True) for i in range(4)]

        # ここに果物を入れます
        self.fruit = [(i * 60, randint(0, 104), randint(0, 2), True) for i in range(4)]

        self.poison = [(i * 60, randint(0, 104), randint(0, 2), True) for i in range(4)]


        self.score = 0
        self.player_x = 72
        self.player_y = -16
        self.player_vy = 0
        self.player_is_alive = True

        pyxel.playm(0, loop=True)

        pyxel.run(self.update, self.draw)

    def update(self):
        # ここにキーボード「q」で終了の処理を入れます
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.update_player()

        # ここに果物のupdateメソッド呼び出しを入れます
        for i, v in enumerate(self.fruit):
            self.fruit[i] = self.update_fruit(*v)

        for i, v in enumerate(self.poison):
            self.poison[i] = self.update_poison(*v)

        # ここに床のupdateメソッド呼び出しを入れます
        for i, v in enumerate(self.floor):
            self.floor[i] = self.update_floor(*v)

    
    # ここにpoisonのupdateメソッドを入れます

    def update_poison(self, px, py, kind, is_active):
        if is_active and abs(px - self.player_x) < 12 and abs(py - self.player_y) < 12:
            is_active = False
            self.score -= (kind + 1) * 100
            self.player_vy = min(self.player_vy, -8)

            #再生する音楽
            pyxel.play(3, 4)

        #poisonの感覚
        px -= 2

        if px < -40:
            px += 240
            py = randint(0, 104)
            kind = randint(0, 2)
            is_active = True

        return (px, py, kind, is_active)





    # ここに果物のupdateメソッドを入れます
    def update_fruit(self, x, y, kind, is_active):
        if is_active and abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12:
            is_active = False
            self.score += (kind + 1) * 100
            self.player_vy = min(self.player_vy, -8)
            pyxel.play(3, 4)

        #果物の感覚
        x -= 2

        if x < -40:
            x += 240
            y = randint(0, 104)
            kind = randint(0, 2)
            is_active = True

        return (x, y, kind, is_active)

    # ここに床のupdateメソッドを入れます
    def update_floor(self, x, y, is_active):
        if is_active:
            if (
                self.player_x + 16 >= x
                and self.player_x <= x + 40
                and self.player_y + 16 >= y
                and self.player_y <= y + 8
                and self.player_vy > 0
            ):
                is_active = False
                self.score += 10
                self.player_vy = -12
                pyxel.play(3, 3)
        
        #床が落ちる速度
        else:
            y += 1
        
        #床が流れる速度
        x -= 4

        if x < -40:
            x += 240
            y = randint(8, 104)
            is_active = True

        return x, y, is_active

    def update_player(self):
        # ここにキーボード「左矢印」「右矢印」で移動の処理を入れます
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            self.player_x = max(self.player_x - 2, 0)

        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)

        self.player_y += self.player_vy
        self.player_vy = min(self.player_vy + 1, 8)

        if self.player_y > pyxel.height:
            if self.player_is_alive:
                self.player_is_alive = False
                pyxel.play(3, 5)

            if self.player_y > 600:
                self.score = 0
                self.player_x = 72
                self.player_y = -16
                self.player_vy = 0
                self.player_is_alive = True

    def draw(self):
        pyxel.cls(12)

        # ここに空と山と森と雲を入れます
        # draw sky
        pyxel.blt(0, 88, 0, 0, 88, 160, 32)

        # draw mountain
        pyxel.blt(0, 88, 0, 0, 64, 160, 24, 12)

        # draw forest
        offset = pyxel.frame_count % 160
        for i in range(2):
            pyxel.blt(i * 160 - offset, 104, 0, 0, 48, 160, 16, 12)

        # draw clouds
        offset = (pyxel.frame_count // 16) % 160
        for i in range(2):
            for x, y in self.far_cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 64, 32, 32, 8, 12)

        offset = (pyxel.frame_count // 8) % 160
        for i in range(2):
            for x, y in self.near_cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 0, 32, 56, 8, 12)

        # ここに床の描画を入れます
        # draw floors 16がアセット
        for x, y, is_active in self.floor:
            pyxel.blt(x, y, 0, 0, 16, 40, 8, 12)

            

        # ここに果物の描画を入れます
        # draw fruits
        for x, y, kind, is_active in self.fruit:
            if is_active:
                pyxel.blt(x, y, 0, 32 + kind * 16, 0, 16, 16, 12)


        
        # ここにposinの描画を入れます
        # draw poison
        for px, py, kind, is_active in self.poison:
            if is_active:
                pyxel.blt(px, py, 0, 0, 120, 16, 16, 12)

        # draw player
        pyxel.blt(
            self.player_x,
            self.player_y,
            0,
            16 if self.player_vy > 0 else 0,
            0,
            16,
            16,
            12,
        )

        # draw score
        s = "SCORE {:>4}".format(self.score)
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)

App()