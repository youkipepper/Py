'''
                  ___====-_  _-====___
            _--^^^#####//      \\#####^^^--_
         _-^##########// (    ) \\##########^-_
        -############//  |\^^/|  \\############-
      _/############//   (@::@)   \############\_
     /#############((     \\//     ))#############\
    -###############\\    (oo)    //###############-
   -#################\\  / VV \  //#################-
  -###################\\/      \//###################-
 _#/|##########/\######(   /\   )######/\##########|\#_
 |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
 `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
    `   `  `      `   / | |  | | \   '      '  '   '
                     (  | |  | |  )
                    __\ | |  | | /__
                   (vvv(VVV)(VVV)vvv)

     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               神兽保佑            永无BUG
'''

'''
Author: youki.cui
Date: 2022-08-15 02:16:58
LastEditors: youki.cui
LastEditTime: 2022-08-16 01:11:21
FilePath: /Py/Python入门/4.6-综合应用-名片管理系统/cardMain.py
Description: Once again to change everything.

Copyright (c) 2022 by youki.cui youkipepper@gmail.com, All Rights Reserved. 
'''
# version 1.0

import cardTools

# 无限循环, 由用户主动决定什么时候退出循环
while True:
    # 显示功能菜单
    cardTools.showMenu()

    actionStr = input("请选择希望执行的操作: ")
    print("您选择的操作是 [%s]" % actionStr)

    # 1,2,3 针对名片的操作
    if actionStr in ["1", "2", "3"]:

        # 新增名片
        if actionStr == "1":
            cardTools.newCard()
        # 显示全部
        elif actionStr == "2":
            cardTools.showAll()
        # 查询名片
        elif actionStr == "3":
            cardTools.seachCard()
        # pass

    # 0 退出系统
    elif actionStr == "0":
        print("欢迎再次使用 [名片管理系统]")
        break
        # 如果在开发程序时, 不希望立刻编写分支内部的代码
        # 可以使用 pass 关键字, 表示一个占位符, 能够保证程序的代码结构正确!
        # 程序运行时, pass 关键字不会执行任何操作!
        # pass

    # 其他内容输入错误, 需要提示用户
    else:
        print("您输入的不正确, 请重新选择")
