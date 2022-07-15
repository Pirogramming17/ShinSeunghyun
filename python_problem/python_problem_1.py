import random
num = 0

def brGame(player):
    global num
    #num을 전역변수로 빼줘야 brGame('computer')와 brGame('player')가
    #서로 num을 주고 받을 수 있음
    if player == 'computer':
        if num < 31:
            #computer가 31 이상의 숫자를 입력하거나, 29, 30 즈음에서 혼자 자폭하는 일이
            #없도록 코드 수정
            if num >= 29:
                com = 1
            elif num >= 28:
                com = random.randint(1, 2)
            else:
                com = random.randint(1, 3)
            for k in range(com):
                print(f'computer: {k + 1 + num}')
            num += com
        else:
            print('computer win!')

    if player == 'player':
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

while(True):
    if num < 31:
        brGame('computer')
        brGame('player')
    else:
        break