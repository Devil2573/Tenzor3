print("Текущие координаты (0,0)")
print("Введите направление движения(W-вверх, S-вниз, A-влево, D-вправо,STOP-остановка) и кол-во шагов, каждое в отдельной строке")
sl=("W","S","A","D","STOP")
x=0
y=0
while(True):
    while(True):
        s1=str(input())
        if s1 in sl:
            break
        else:
            print("Введено не правильное направление")
    if s1=="STOP":
        break
    while(True):
        s2=int(input())
        if s2 >0:
            break
        else:
            print("Введено не правильное кол-во шагов")
    if s1=="D":
        x+=s2
        print("Новые координаты (",x,",",y,")")
    elif s1=="A":
        x-=s2
        print("Новые координаты (",x,",",y,")")
    elif s1=="W":
        y+=s2
        print("Новые координаты (",x,",",y,")")
    elif s1=="S":
        y-=s2
        print("Новые координаты (",x,",",y,")")