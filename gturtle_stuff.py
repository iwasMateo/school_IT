from gturtle import *

makeTurtle()
ht()

def nEck(length, corners):
    repeat corners:
        fd(length)
        rt(360/corners)

nEck(input("Länge der Seiten: "), input("Eckenanzahl: "))

