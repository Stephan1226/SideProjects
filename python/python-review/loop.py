import turtle

t = turtle.Turtle()
t.shape("turtle")
t.shapesize(3, 3) # 거북이를 3배 확대한다. 
while True:
    cmd = input("명령을 입력하시오: ")
    if cmd == 'l': 
        t.left(90)
        t.forward(100)
    if cmd == 'r': 
        t.right(90)
        t.forward(100)