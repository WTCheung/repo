# @Author   :wayne
import random


class Game:

    def __init__(self):
        # 利用列表推导式生成hp
        self.hp = [x for x in range(990, 1010)]
        # print(self.hp)
        # 从列表种随机取一个值
        self.enemy_hp = random.choice(self.hp)
        # print(self.enemy_hp)

        # 利用列表推导式生成power
        self.power = [x for x in range(150, 210)]
        # print(self.power)
        # 从列表中随机取一个值
        self.enemy_power = random.choice(self.power)
        # print(self.enemy_power)
        self.my_hp = 1000
        self.my_power = 200
        # self.enemy_hp = 1000
        # self.enemy_power = 200
        # 定义一个fight函数实现游戏逻辑
        # 利用列表推导式生成一共要进行几轮x_round
        self.round = [x for x in range(1,6)]
        self.x_round = random.choice(self.round)

    def fight(self):

            # 加入循环，让游戏进行多轮
        while True:
            self.my_hp = self.my_hp - self.enemy_power

            self.enemy_hp = self.enemy_hp - self.my_power

            print(self.my_hp)
#判断谁的血量小于0
            if self.my_hp <= 0:
                print(f"我的血量：{self.my_hp}")
                print(f"敌人的血量：{self.enemy_hp}")
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print(f"我的血量：{self.my_hp}")
                print(f"敌人的血量：{self.enemy_hp}")
                print("我赢了")
                break



game = Game()
game.fight()
