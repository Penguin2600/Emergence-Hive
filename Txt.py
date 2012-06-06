import pygame.locals
from Audio import MenuSamples

class Write(pygame.sprite.Sprite):
    def __init__(self, color, size, pos, text, inc=0):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.topleft=pos.topleft
        self.rect.top+=inc

class MainMenu(pygame.sprite.Sprite):
    def __init__(self, pos, options):
        pygame.sprite.Sprite.__init__(self)
        self.menu=pygame.sprite.Group()
        self.over=[0,0,0,0,0,0,0,0,0,0]
        self.space=30
        self.clicked=0
        self.options=options
        self.pos=pos
        self.sounds=MenuSamples()

    def Update(self, events):
        inc=0
        mevent=0
        self.clicked=0
        self.menu.empty()

        for event in events:
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                mevent= event.button
            else:
                mevent=0
                
        mpos=pygame.mouse.get_pos()
        mouse=pygame.locals.Rect(mpos[0]-30,mpos[1]-30,30,30)#give the mouse a rectangle
        
        for x in self.options:
            inc+=self.space
            if mouse.top < (inc+self.pos.top) and mouse.bottom > (inc+self.pos.top+10) and mevent==1 :
                self.menu.add(Write([255,160,160], 30, self.pos, x, inc))
                self.clicked=(inc/self.space)
                self.sounds.playsound('click')
                
            elif mouse.top < (inc+self.pos.top) and mouse.bottom > (inc+self.pos.top+10) and mevent==0:
                self.menu.add(Write([160,255,160], 30, self.pos, x, inc))
                
                if self.over[(inc/self.space)]==0:
                    self.sounds.playsound('over')
                    self.over[(inc/self.space)]=1
          
            else:
                self.menu.add(Write([255,255,255], 30, self.pos, x, inc))
                if self.over[(inc/self.space)]==1:
                    self.over[(inc/self.space)]=0
                
        
                

        
                
        
