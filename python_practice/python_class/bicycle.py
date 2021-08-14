# @Author   :wayne
'''
写一个Bicycle（自行车）类，有run(骑行)方法。
调用时显示骑行一共要走的总里程KM（骑行时传入的数字）：
再写一个电动自行车的的类EBicycle继承Bicycle类，
添加电池电量valume属性，要行驶的路程有多少count_km,通过参数传入，同时有两个方法
1.fill_charge(vol)用来充电，vol为电量
2.run(km)方法用于骑行，每骑行10km消耗1度电
当电量消耗尽时调用Bicycle的run方法骑行
通过传入的骑行里程数，显示骑行结果
'''

#自行车的类
class Bicycle:
    #run方法
    def run(self, km):
        print(f"我用人力一共骑行了{km}km.")
# bike = Bicycle()
# bike.run(10)
# 电动自行车的类
# 继承：把父类写成 类名的括号里
class EBicycle(Bicycle):
    def __init__(self, valume):
        self.valume = valume
     # 充电的方法
    def fill_charge(self, vol):
        # 充电后的电量 = 本身电量 + 充电电量
        self.valume = self.valume + vol
        print(f"充了{vol}度电，现在的电量为：{self.valume}")
# 骑行的方法
    '''
    2.run(km)方法用于骑行，每骑行10km消耗1度电
当电量消耗尽时调用Bicycle的run方法骑行
通过传入的骑行里程数，显示骑行结果
    '''
    def run(self, km):
        # 获取目前能电动骑行的最大里程数
        power_km = self.valume * 10
        print(f"我可以用电行驶{power_km}km")
        # 判断
        if power_km >= km:
            power_km = power_km - km
            print(f"我用电动车走完了本次旅行，还能用电动车骑行{power_km}km")
        else:
            # 电量不够了，在电用完以后，还得用人力骑行
            print(f"我用电动车骑行了{power_km}km")
            # 当电量消耗尽时调用Bicycle的run方法骑行
            #非继承调用
            # bike = Bicycle()
            # bike.run(km - power_km)
            # 继承调用
            super().run(km - power_km)
# ebike = EBicycle()
# 构造函数有变量，实例化的时候也要传值
# TypeError: __init__() missing 1 required positional argument: 'valume'
ebike = EBicycle(1)
ebike.fill_charge(11)
ebike.run(150)
# ebike.fill_charge(3)