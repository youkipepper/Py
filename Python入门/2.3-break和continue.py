i = 0
while i < 10:
    # break 某一条件满足时, 退出循环, 不再执行后续重复的代码
    # i == 3
    if i == 3:
        break
    print(i)
    i += 1
print("over")

j = 0
while j < 10:
    if(j == 3):
        # 注意: 在循环中, 如果使用 continue 这个关键字
        # 在使用关键字之前, 需要确认循环的计数是否修改
        # 否则可能会导致死循环

        j += 1
        continue
    print(j)
    j += 1
