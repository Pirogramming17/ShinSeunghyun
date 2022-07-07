num = 0
while (True):
    if num < 31:
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
                print(f'playerA: {i + 1 + num}')
            num += number
    else:
        break

    if num < 31:
        b = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :')
        if b.isnumeric() != True:
            print('정수를 입력하세요')
            continue
        elif int(b) > 3 or int(b) < 0:
            print('1, 2, 3 중 하나를 입력하세요')
            continue
        else:
            number = int(b)
            for i in range(number):
                print(f'playerB: {i + 1 + num}')
            num += number
    else:
        break