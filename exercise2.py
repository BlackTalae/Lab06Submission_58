import pygame as pg
pg.init()

win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
nx,ny=20,20

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen,r,g,b):
        pg.draw.rect(screen,(r,g,b),(self.x,self.y,self.w,self.h))
w = False
a = False
s = False
d = False
# key = [pg.K_w, pg.K_a, pg.K_s, pg.K_d]
while(True):
    oob = Rectangle(nx,ny,100,100) # สร้าง Object จากคลาส Rectangle ขึ้นมา
    screen.fill((255, 255, 255))
    oob.draw(screen,255,0,0)
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_w: 
            w = True
        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกปล่อย KEYUP ปุ่มถูกกดลง KEYDOWN
            a = True 
        if event.type == pg.KEYDOWN and event.key == pg.K_s:  
            s = True  
        if event.type == pg.KEYDOWN and event.key == pg.K_d: 
            d = True

        if event.type == pg.KEYUP and event.key == pg.K_w: 
            w = False 
        if event.type == pg.KEYUP and event.key == pg.K_a: #ปุ่มถูกปล่อย KEYUP ปุ่มถูกกดลง KEYDOWN  
            a = False
        if event.type == pg.KEYUP and event.key == pg.K_s:    
            s = False
        if event.type == pg.KEYUP and event.key == pg.K_d: 
            d = False    

        if event.type == pg.QUIT:
            pg.quit()
            run = False   
            
    if w: 
        print("Key W down")
        ny-=1 
    if a: 
        print("Key A down")
        nx-=1
    if s:    
        print("Key S down")
        ny+=1
    if d: 
        print("Key D down")
        nx+=1  

    if ny<0: 
        print("Error")
        ny=0
    if nx<0: 
        print("Error")
        nx=0
    if ny+oob.h>win_y:    
        print("Error")
        ny=win_y-oob.h
    if nx+oob.w>win_x: 
        print("Error")
        nx=win_x-oob.w
                    