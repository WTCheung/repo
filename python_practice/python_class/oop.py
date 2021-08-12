# @Author   :wayne
#面向对象
# class 类名（驼峰法命名）：
#     类属性
#     类方法
class House:
    #静态属性->类变量（类之中，方法之外）
    door = "red"
    floor = "white"
    #动态方法
    def sleep(self):
        print("在房子里可以睡觉")

    def cook(self):
        print("在房子里可以做饭吃")

#把类实例化、
#北欧
north_house = House()
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