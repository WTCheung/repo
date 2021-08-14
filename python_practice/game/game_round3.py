# @Author   :wayne
#定义一个fight函数实现游戏逻辑
import random


def fight(enemy_hp,enemy_power):
    #定义4个人变量存放数据
    my_hp = 1000
    my_power = 200
    # enemy_hp = 1000
    # enemy_power = 200
    #print敌人的攻击力和血量
    print(f"敌人的血量:{enemy_hp}", f"攻击力:{enemy_power}")

    #加入循环，让游戏进行多轮
    while True:
        my_hp = my_hp - enemy_power

        enemy_hp = enemy_hp - my_power

        print(my_hp)

        if my_hp <= 0:
            print(f"我的血量：{my_hp}")
            print(f"敌人的血量：{enemy_hp}")
            print("我输了")
            break
        elif enemy_hp <= 0:
            print(f"我的血量：{my_hp}")
            print(f"敌人的血量：{enemy_hp}")
            print("我赢了")
            break
if __name__ == "__main__":
    #利用列表推导式生成hp
    hp = [x for x in range(990,1010)]
    print(hp)
    #从列表种随机取一个值
    enemy_hp = random.choice(hp)
    print(enemy_hp)

    #利用列表推导式生成power
    power = [x for x in range(100,200)]
    print(power)
    #从列表中随机取一个值
    enemy_power = random.choice(power)
    print(enemy_power)
    #调用函数
    fight(enemy_hp, enemy_power)