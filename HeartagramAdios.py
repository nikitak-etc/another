#!/usr/bin/python3
import turtle
import math

t = turtle.Turtle()
t.speed('fastest')


n = 1
k = 8
dot_start = [-300,-100]
dot_end = [300,100]

ornament_length = ((dot_start[0]-dot_end[0])**2+(dot_start[1]-dot_end[1])**2)**0.5
print(ornament_length)
figure_length = ornament_length/n
print(figure_length)
relationship_length = figure_length/ornament_length
relationship_length_small = relationship_length/k/relationship_length

angle = math.atan((dot_end[1]-dot_start[1])/(dot_end[0]-dot_start[0]))*180/math.pi

if dot_start[0] > dot_end[0]:
    angle = angle + 180

print(angle)

t.left(angle)

dot_list = []
dot_list_small = []

t.up()
t.goto(dot_start)

def figure(start, end):
    dot_list_small.clear()
    h = 5
    for j in range(k):
        dot1 = [start[0]+(end[0]-start[0])*(j)*relationship_length_small,start[1]+(end[1]-start[1])*(j)*relationship_length_small ]
        #dot_list.append(dot)
        if j == 0 or j == k:
            t.goto(dot1)
            dot_list_small.append(dot1)
            continue
        if j <= (k+1)/2:
            h = h * 2
        else:
            h = h / 2
        if j%2 == 0:
            t.up()
            t.goto(dot1)
            t.right(90)
            t.forward(h)
            t.left(90)
            t.down()
            dot_list_small.append(t.pos())
            t.goto(dot_list_small[j-1])
            t.goto(dot_list_small[j])
        else:
            t.up()
            t.goto(dot1)
            t.left(90)
            t.forward(h)
            t.right(90)
            t.down()
            dot_list_small.append(t.pos())
            t.goto(dot_list_small[j-1])
            t.goto(dot_list_small[j])

def heartagram(dot_start, dot_end):
    for i in range(n+1):
        dot = [dot_start[0]+(dot_end[0]-dot_start[0])*(i)*relationship_length,dot_start[1]+(dot_end[1]-dot_start[1])*(i)*relationship_length ]
        dot_list.append(dot)
        print(dot_list)
        if i > 0:
            figure (dot_list[i-1], dot_list[i])
    t.goto(dot_end)

heartagram(dot_start,dot_end)
turtle.done()