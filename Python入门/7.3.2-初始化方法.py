class Cat:
    def __init__(self, newName):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = newName

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名()构造对象的时候, 会自动调用初始化方法__init__
Tom = Cat("Tom")

print(Tom.name)

lazyCat = Cat("大懒猫")
lazyCat.eat()
