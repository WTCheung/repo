# @Author   :wayne
#面向对象
# class 类名（驼峰法命名）：
#     类属性
#     类方法
class House:
    #静态属性->类变量（类之中，方法之外）
    door = "red"
    floor = "white"
    #构造函数,在类实例化的时候就会执行
    def __init__(self):
        #第一种方法，在方法中调用类变量需要加self.
        print(self.door)
        # 实例变量，类的方法中，以“self.变量名”方法定义
        self.kitchen = "cook"
    #动态方法
    def sleep(self):
        # print("在房子里可以睡觉")

        bed = "席梦思"
        self.table = "桌子"
        print(f"在房子里可以躺在{bed}上睡觉")

    def cook(self):

        print("在房子里可以做饭吃")
        print(self.kitchen)
        print(self.table)

#把类实例化、
#北欧
north_house = House()
north_house.sleep()
#不调用sleep方法的时候会报错。调用sleepf方法里的self.变量的时候需要先调用sleep
# AttributeError: 'House' object has no attribute 'table'
north_house.cook()
#中式
China_house = House()
#调用类的属性
print(House.door)
# 修改类属性
House.door = "white"
print(House.door)
# 实例对象调用
print(north_house.door)
# 修改对象属性,不会修改类的属性，只存在这个对象的内部
north_house.door = "black"
print(north_house.door)
print(House.door)