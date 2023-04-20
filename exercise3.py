import pygame as pg
pg.init()

win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color(10,10,10)     # ^^^

FONT = pg.font.Font(None, 32)

font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize 32 pixel
font2 = pg.font.Font('freesansbold.ttf', 14) # font and fontsize 32 pixel

text1 = font.render('FRA 142', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect1 = text1.get_rect() # text size
textRect1.center = (text1.get_rect()[2]//2, text1.get_rect()[3]//2)

text2 = font.render('FIRSTNAME : ', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect2 = text2.get_rect() # text size
textRect2.center = (text2.get_rect()[2]//2, text2.get_rect()[3]//2+33)

text3 = font.render('LASTNAME : ', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect3 = text3.get_rect() # text size
textRect3.center = (text3.get_rect()[2]//2, text3.get_rect()[3]//2+65)

text4 = font.render('AGE : ', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect4 = text4.get_rect() # text size
textRect4.center = (text4.get_rect()[2]//2, text4.get_rect()[3]//2+97)

text6 = font2.render('submit', True, (255,255,255), (255,0,0)) # (text,is smooth?,letter color,background color)
textRect6 = text6.get_rect() # text size
textRect6.center = (text6.get_rect()[2]//2+35, text6.get_rect()[3]//2+135)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        
    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
class InputNum(InputBox):
    def __init__(self, x, y, w, h, text=''):
        super().__init__(x, y, w, h, text)
    
    def handle_event(self, event):
        num = [pg.K_0,pg.K_1,pg.K_2,pg.K_3,pg.K_4,pg.K_5,pg.K_6,pg.K_7,pg.K_8,pg.K_9]
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key in num:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen,r,g,b):
        pg.draw.rect(screen,(r,g,b),(self.x,self.y,self.w,self.h))
    def isMouseOn(self):
        if ((pg.mouse.get_pos()[0] <= self.x+self.w and pg.mouse.get_pos()[0] > 0) and (pg.mouse.get_pos()[1] <= self.y+self.h and pg.mouse.get_pos()[1] > 0)):
            return True

input_box1 = InputBox(230, 33, 140, 32) # สร้าง InputBox1 (x,y,w,h)
input_box2 = InputBox(230, 65, 140, 32) # สร้าง InputBox2 (x,y,w,h)
input_box3 = InputNum(230, 97, 140, 32) # สร้าง InputBox3 (x,y,w,h)
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
button = Rectangle(10,129,100,30)
run = True
cnt = 0

while run:
    
    screen.fill((255, 255, 255))
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)   
       
    button.draw(screen,255,0,0)
    screen.blit(text6, textRect6)
    if button.isMouseOn():
        button.draw(screen,100,100,100)
        if (pg.mouse.get_pressed()[0]==1):
            t="Hello "+input_box1.text+" "+input_box2.text+" ! You are "+input_box3.text+" years old."
            text5 = font2.render(t, True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
            textRect5 = text5.get_rect() # text size
            textRect5.center = (text5.get_rect()[2]//2+10, text5.get_rect()[3]//2+200)
            cnt+=1
            # input_box1.text=""
            # input_box2.text=""
    if cnt > 50 :
        screen.blit(text5, textRect5)
    
        # input_box3.text=""        
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()