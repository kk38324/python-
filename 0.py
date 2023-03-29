from turtle  import *
from random import *
from time import *
def koch(size,n):   #递归方法绘制科赫雪花
    if n == 0:
        fd(size)
    else:
        for angle in [0,60,-120,60]:
            left(angle)
            koch(size/3,n-1)
def main(a,b,level):    #在选定位置开始绘制n阶雪花
    tracer(False)
    pensize(2)
    setup(600,600)
    penup()
    begin_fill()
    fillcolor(136,171,218)
    goto(a,b)
    pendown()
    koch(50,level)
    right(120)
    koch(50,level)
    right(120)
    koch(50,level)
    seth(0)
    end_fill()
    update()
    
colormode(255)
color(46,89,167)
for i in range(45):     #雪花绘制主过程
    z=[1.2,1.4,1.3,1.5,1.6]
    a=randint(1,10)*z[0]
    b=randint(1,10)*z[1]
    c=randint(1,10)*z[2]
    d=randint(1,10)*z[3]
    e=randint(1,10)*z[4]
    f=10        #雪花下落速度参数设定
    main(-400-a,110-i*f,3)
    main(-300-b,130-i*f,3)    
    main(-200-c,105-i*f,3)
    main(-100-d,125-i*f,3)
    main(e,110-i*f,3)
    main(100-a,120-i*f,3)
    main(200-b,90-i*f,3)
    main(300-c,140-i*f,3)
    main(400-d,100-i*f,3)
    sleep(0.5)     #重新绘制雪花间隔时间
    clear() 
hideturtle()


