'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  - /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑     永不宕机     永无BUG
'''

'''
Author: youki.cui
Date: 2022-08-15 19:41:17
LastEditors: youki.cui
LastEditTime: 2022-08-16 01:05:39
FilePath: /Py/Python入门/4.6-综合应用-名片管理系统/cardTools.py
Description: Once again to change everything.

Copyright (c) 2022 by youki.cui youkipepper@gmail.com, All Rights Reserved. 
'''
# version 1.0





# 记录所有的名片字典
cardList = []


def showMenu():
    """显示菜单"""
    print("*"*50)
    print("欢迎使用[名片管理系统] V1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*"*50)


def newCard():
    """Add new card"""
    print("-"*50)
    print("新增名片")

    # 1、提示用户输入名片的详细信息
    nameStr = input("请输入姓名: ")
    phoneStr = input("请输入电话: ")
    qqStr = input("请输入QQ: ")
    emailStr = input("请输入邮箱: ")

    # 2、使用用户输入的信息建立一个名片字典
    cardDic = {"name": nameStr,
               "phone": phoneStr,
               "qq": qqStr,
               "email": emailStr
               }

    # 3、将名片字典添加到列表中
    cardList.append(cardDic)
    print(cardList)

    # 4、提示用户添加成功
    print("添加 %s 的名片成功" % nameStr)


def showAll():
    """显示所有名片"""
    print("-"*50)
    print("显示所有名片")

    # 判断是否存在名片记录, 如果没有, 提示用户并返回
    if len(cardList) == 0:
        print("当前没有任何的名片记录, 请使用新增功能添加名片!")
        return

    # 打印表头
    for name in ["name", "call", "QQ", "email"]:
        print(name, end="\t\t")
    print("")
    # 打印分割线
    print("="*50)
    # 遍历名片列表依次输出字典信息
    for cardDict in cardList:
        print("%s\t\t%s\t\t%s\t\t%s" % (cardDict["name"],
                                        cardDict["phone"],
                                        cardDict["qq"],
                                        cardDict["email"],
                                        ))


def seachCard():
    """搜索名片"""
    print("-"*50)
    print("搜索名片")

    # 1、提示用户输入要搜索的姓名
    findName = input("请输入要搜索的姓名: ")

    # 2、遍历名片列表, 查询要搜索的姓名, 如果没有找到, 需要提示用户
    for cardDict in cardList:
        if cardDict["name"] == findName:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("="*50)
            print("%s\t\t%s\t\t%s\t\t%s" % (cardDict["name"],
                                            cardDict["phone"],
                                            cardDict["qq"],
                                            cardDict["email"],
                                            ))
            # TODO 针对找到的名片记录执行修改和删除的操作
            dealCard(cardDict)
            break
    else:
        print("抱歉, 没有找到 %s" % findName)


def dealCard(findDict):
    print(findDict)
    actionStr = input("请选择要执行的操作"
                      " [1] 修改 [2] 删除 [0] 返回上级")
    if actionStr == "1":

        findDict["name"] = inputCardInfo(findDict["name"], "姓名: ")
        findDict["phone"] = inputCardInfo(findDict["name"], "电话: ")
        findDict["qq"] = inputCardInfo(findDict["name"], "QQ: ")
        findDict["email"] = inputCardInfo(findDict["name"], "邮箱: ")

        print("修改名片")
    elif actionStr == "2":

        cardList.remove(findDict)

        print("删除名片成功!")


'''
description: 
param {*} dicValue
param {*} tipMessage
return {*}
'''
def inputCardInfo(dicValue, tipMessage):
    # 1、提示用户输入内容
    resultStr = input(tipMessage)

    # 2、针对用户的输入进行判断, 如果用户输入了内容, 直接返回结果
    if len(resultStr) > 0:
        return resultStr

    # 3、如果用户没有输入内容, 返回字典中原有的值
    else:
        return dicValue
