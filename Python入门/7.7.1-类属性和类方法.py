class Tool(object):
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

tool3.count = 99
print("工具对象的总数 %d" % tool3.count)
print("===> %d" % Tool.count)

# 调用类方法
Tool.show_tool_count()