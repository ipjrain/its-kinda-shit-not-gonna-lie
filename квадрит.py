from turtle import *
import math #подключение мат.модуля
color("blue")#голубой цвет
begin_fill()#начать заполнение 
for i in range(4):#начало цикла описанного ниже
    forward(150)#вперед на 150 градусов
    right(90)#вправо на 90 градусов
end_fill()   #завершить заполнениие 

penup()#поднять перо
forward(150)
pendown()#опустить перо

color("red")
begin_fill()
for i in range(5):
    forward(250)
    right(144)
end_fill()    
    
