import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(10)
col = ['red', 'green', 'blue', 'white']
c = 0

#python.advance.projects
for i in range (50):
    t.forward(i * 10)
    t.right(144)
    t.color(col[c])
    if c == 3:
        c = 0
    else:
        c += 1
