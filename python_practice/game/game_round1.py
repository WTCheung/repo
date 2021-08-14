'''
1.回合制游戏
2.每个角色都有hp 和power，hp代表血量，初始值为1000，power代表攻击力，初始值为200.
3.定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
'''

#定义一个fight函数实现游戏逻辑
def fight():
    #定义4个人变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    #定义最终血量计量方式
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    #判断输赢
    if my_final_hp > enemy_hp:
        print("我赢了")
    #elif my_final_hp < enemy_final_hp:
        #print("我输了")
    else:
        print("loser")
        #三目运算 复制当前行的代码  ctl+d
        #自动导包alt+回车
    print("我赢了") if my_final_hp > enemy_final_hp else print("我输了")
fight()