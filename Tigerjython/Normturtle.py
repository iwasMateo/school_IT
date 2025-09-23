from turtle import *
times=4

def nEck(corners, length):
    i=1
    while i<=corners:
        forward(length)
        right(360/corners)
        i+=1
def irregular3(length, angle):
    forward(length)
    right((360-angle)/2)
    forward(100)
    right((360-angle)/2)
    forward(length)

def doThatThing():
    e=0
    while e<6:
        nEck(3, 60)
        right(360/6)
        e+=1

doThatThing()
clear()
def doThatThing2():
    e=0
    while e<8:
        nEck(3, 360/8)
        right(360/8)
        e+=1
irregular3(100, 30)