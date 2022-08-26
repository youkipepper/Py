class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
Tom = Cat()

Tom.eat()
Tom.drink()

print(Tom)
addr = id(Tom)
print("%d" % addr)
