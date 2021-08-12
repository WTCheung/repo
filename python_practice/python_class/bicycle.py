# @Author   :wayne
'''
写一个Bicycle（自行车）类，有run(骑行)方法。
调用时显示骑行里程KM（骑行时传入的数字）：
再写一个电动自行车的的类EBicycle继承Bicycle类，
添加电池电量valueme属性，通过参数传入，同时有两个方法
1.fill_charge(vol)用来充电，vol为电量
2.run(km)方法用于骑行，每骑行10km消耗1度电
当电量消耗尽时调用Bicycle的run方法骑行
通过传入的骑行里程数，显示骑行结果
'''

#自行车的类
class Bicycle:
    #run方法
    def run(self, km):
        print(f"一共骑行了{km}km.")

# 电动自行车的类
class EBicycle:
    def fill_charge(self, vol):
        print(f"目前电量为：{vol}")

    def run(self, km):
        print(f"骑行了{km}km")
