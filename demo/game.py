import random

counts = 3
anwer = random.randint(1,10)

while counts > 0:
    temp = input('猜猜看，请输入数字：')
    guess = int(temp)

    if guess == anwer:
        print('猜对啦')
        break
    else:
        if guess < anwer:
            print('猜小拉')
        else:
            print('猜大啦')
        counts = counts - 1

print('游戏结束，拜拜')
