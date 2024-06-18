def myDan(n): #한단을 출력
    for i in range(1, 10):
        print("%d * %d = %d"%(n, i , n*i))
def myAllDan(): #구구단 전체
    for i in range(1, 10):
        for j in range(1, 10):
            print("%d * %d = %d"%(i, j, i*j))
    print("program end.")


#main
while True:
    chack = int(input("1 : 한번만 / 2 : 전채 / 0 : 종료 | "))

    if chack == 1:
        dan = int(input("몇단 : "))
        myDan(dan)
        replay = input("다시 실행 합니까 (y/n) : ")
        if replay == 'y':
            print("다시 실행 합니다.")
        elif replay == 'n':
            print("program end.")
            break
        else:
            print("잘 못된 입력 입니다.\n program end.")
            break
    elif chack == 2:
        myAllDan()
        break
    elif chack == 0:
        print("program end")
        break