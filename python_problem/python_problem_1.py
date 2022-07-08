def brGame(player):
    global num
    if player == 'computer':
        if num < 31:
            com = random.randint(1, 3)
            for k in range(com):
                print(f'computer: {k + 1 + num}')
            num += com
        else:
            print('computer win!')

    elif player == 'player':
        if num < 31:
            while (True):
                a = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')
                if a.isnumeric() != True:
                    print('정수를 입력하세요')
                    continue
                elif int(a) > 3 or int(a) < 0:
                    print('1, 2, 3 중 하나를 입력하세요')
                    continue
                else:
                    number = int(a)
                    for i in range(number):
                        print(f'player: {i + 1 + num}')
                num += number
                break
        else:
            print('player win!')

