seatCnt = 10
reservedCnt = 0
ticketPrice = 10000
vipDiscount = 5000

seat = ['o'] * seatCnt #List Resize & Set All
userId = input('user Id 입력 >> ')

try:
    vip = int(input('vip인가요? 1 >> '))
except:
    vip = 0

while True:

    print('\n------------------------------------')
    for i in range(0, seatCnt):
        print(i + 1, end=' ')
    print('\n------------------------------------')
    for i in seat:
        print(i, end=' ')
    print('\n------------------------------------')

    try:
        userInput = int(input('원하는 좌석 번호 입력(종료: other)>> '))
    except:
        userInput = -1

    userInput = userInput - 1
    if userInput < 0 or userInput >= seatCnt:
        print('예매 프로그램을 종료합니다.')
        print(userId + '님의 예매 확인 영수증입니다.')
        print('예매된 좌석 번호는', end='')
        for i in range(0, seatCnt):
            if seat[i] == 'x':
                print(str(i) + '번', end='')

        print('예매 좌석 수는 : ' + str(reservedCnt))
        total = reservedCnt * ticketPrice
        if vip:
            print('vip 금액은 : ' + str(total - vipDiscount))
        else:
            print('일반 금액은 : ' + str(total))
        break


    print(str(userInput + 1)+'을 선택하셨군요!' )
    if seat[userInput] == 'o':
        seat[userInput] = 'x'
        reservedCnt = reservedCnt + 1
        print('예매 처리 완료')
    else:
        print('이미 예매됨')

