import turtle as t
t.shape('turtle')
side = 100
t.setup(width=1000, height=800)
for i in range(5):
    for j in range(4): 
        t.forward(side) 
        t.left(90)
    side += 20