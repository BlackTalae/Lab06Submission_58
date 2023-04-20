import sys 
import pygame as pg

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen,r,g,b):
        pg.draw.rect(screen,(r,g,b),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        if ((pg.mouse.get_pos()[0] <= self.x+self.w and pg.mouse.get_pos()[0] > 0) and (pg.mouse.get_pos()[1] <= self.y+self.h and pg.mouse.get_pos()[1] > 0)):
            return True
        
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
firstObject = Rectangle(20,20,100,100) # สร้าง Object จากคลาส Rectangle ขึ้นมา

btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    # firstObject.draw(screen,255,0,0) # ใส่ screen เข้าไปด้วยเพราะว่าคำสั่ง pg.draw.rect จะเป็นจะต้องระบุระนาบว่าต้องการสร้างรูปบนระนาบใด
    btn.draw(screen,255,0,0)   

    if btn.isMouseOn():
        btn.draw(screen,100,100,100)  
        if (pg.mouse.get_pressed()[0]==1):
            btn.draw(screen,128,0,128)
    # else:
    #     btn.w = 100
    #     btn.h = 100

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False    
