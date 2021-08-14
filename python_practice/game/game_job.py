# @Author   :wayne
'''
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，

see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''
# 定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
class TongLao:

    def __init__(self, t_hp, t_power):
        self.t_hp = t_hp
        self.t_power = t_power

    def see_people(self, name):
        self.name = name
        if self.name == 'WYZ':
            print("师弟！！！！")
        if self.name == 'LQS':
            print("师弟是我的！")
        if self.name == 'DCQ':
            print("叛徒！我杀了你")


    def fight_zms(self, enemy_hp ,enemy_power):
        self.enemy_hp = enemy_hp
        self.enemy_power = enemy_power
        self.t_power = self.t_power * 10
        print(f"我的攻击力提升到了{self.t_power}")
        self.t_hp = self.t_hp / 2
        print(f"我的血量还有{self.t_hp}")
        if self.t_hp == 0:
            print("白白提升了攻击力！血槽却没了！输了！")
        else:
            self.t_hp = self.t_hp - self.enemy_power
            print(f"打完以后还剩{self.t_hp}")
            self.enemy_hp = self.enemy_hp - self.t_power
            print(f"打以后敌人还剩{self.enemy_hp}")
            if self.t_hp > self.enemy_hp:
                print("我赢了！")
            else:
                print("我输了")
tong = TongLao(10000,500)
tong.fight_zms(5000,800)