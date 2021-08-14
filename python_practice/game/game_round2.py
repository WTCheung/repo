# @Author   :wayne
#定义一个fight函数实现游戏逻辑
def fight():
    #定义4个人变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    #加入循环，让游戏进行多轮
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        print(my_hp)
        if my_hp <= 0:
            print("我输了")
            break
        elif enemy_hp <= 0:
            print("我赢了")
            break
fight()