money = list(input("請輸入金額:"))
for i in range(0, len(money)):
    if int(money[i]) == 1:
        print("壹", end="")
    elif int(money[i]) == 2:
        print("貳"end="")
    elif int(money[i]) == 3:
        print("參", end="")
    elif int(money[i]) == 4:
        print("肆", end="")
    elif int(money[i]) == 5:
        print("伍", end="")
    elif int(money[i]) == 6:
        print("坴", end="")
    elif int(money[i]) == 7:
        print("柒", end="")
    elif int(money[i]) == 8:
        print("捌", end="")
    elif int(money[i]) == 9:
        print("玖", end="")
