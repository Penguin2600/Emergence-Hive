import pygame
import sys
import os

class ButtonGroup():
    def __init__(self):
        self.buttons=[]
        
    def add(self,button):
        self.buttons.append(button)
        
    def remove(self,button):
        self.buttons.remove(button)
        
    def draw(self,surface):
        for button in self.buttons:
            surface.blit(button.image,button.rect)
        
    def update(self,mpos,mevent):
        for button in self.buttons:
            if button.rect.collidepoint(mpos):
                button.image  = button.ovr
                if mevent==1:
                    button.over=1
                    if button.clicked==0:
                        if not pygame.mixer.get_busy() and button.audio==1:
                            button.click.play()
                            button.clicked=1
                    button.image= button.dn
                else:
                    button.clicked=0
                    if button.over==0:
                        if not pygame.mixer.get_busy() and button.audio==1:
                            button.hover.play()
                            button.over=1
            else:
                button.image= button.up
                button.clicked=0
                button.over=0        


class Momentary(pygame.sprite.Sprite):
    def __init__(self, pos, filename, audio=0):
        pygame.sprite.Sprite.__init__(self)
        
        self.up  = pygame.image.load(str(os.path.abspath(os.path.dirname(sys.argv[0])) + filename + "Up.png")).convert()
        self.dn  = pygame.image.load(str(os.path.abspath(os.path.dirname(sys.argv[0])) + filename + "Dn.png")).convert()
        self.ovr  = pygame.image.load(str(os.path.abspath(os.path.dirname(sys.argv[0])) + filename + "Over.png")).convert()
        self.image = self.up
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.audio=audio
        self.over=0
        self.clicked=0
        self.loadaudio()
        
    def loadaudio(self):
        pygame.mixer.init()
        self.hover = pygame.mixer.Sound(str(os.path.abspath(os.path.dirname(sys.argv[0])) + "\Data\Audio\over.wav"))
        self.click = pygame.mixer.Sound(str(os.path.abspath(os.path.dirname(sys.argv[0])) + "\Data\Audio\click.wav"))
            
    
    def update(self,mpos,mevent):

        if self.rect.collidepoint(mpos):
            self.image  = self.ovr
            if mevent==1:
                self.over=1
                if self.clicked==0:
                    if not pygame.mixer.get_busy() and self.audio==1:
                        self.click.play()
                        self.clicked=1
                self.image= self.dn
            else:
                self.clicked=0
                if self.over==0:
                    if not pygame.mixer.get_busy() and self.audio==1:
                        self.hover.play()
                        self.over=1
        else:
            self.image= self.up
            self.clicked=0
            self.over=0


class Toggle(pygame.sprite.Sprite):
    def __init__(self, pos, filename, audio=0, active=False):
        pygame.sprite.Sprite.__init__(self)
        
        self.up  = pygame.image.load(str(os.path.abspath(os.path.dirname(sys.argv[0])) + filename + "Up.png")).convert()
        self.dn  = pygame.image.load(str(os.path.abspath(os.path.dirname(sys.argv[0])) + filename + "Dn.png")).convert()
        self.ovr  = pygame.image.load(str(os.path.abspath(os.path.dirname(sys.argv[0])) + filename + "Over.png")).convert()
        if active==False:
            self.image = self.up
        else:
            self.image = self.dn
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.over=0
        self.clicked=0
        self.active=active
        self.audio=audio
        self.loadaudio()

    def loadaudio(self):
        pygame.mixer.init()
        self.hover = pygame.mixer.Sound(str(os.path.abspath(os.path.dirname(sys.argv[0])) + "\Data\Audio\over.wav"))
        self.click = pygame.mixer.Sound(str(os.path.abspath(os.path.dirname(sys.argv[0])) + "\Data\Audio\click.wav"))

    def draw(self,surface):
            surface.blit(self.image,self.rect)
            
    def update(self,mpos,mevent):

        if self.rect.collidepoint(mpos):
            #self.image  = self.ovr
            if mevent==1:
                self.over=1
                if self.clicked==0:
                    if not pygame.mixer.get_busy() and self.audio==1:
                        self.click.play()
                        self.clicked=1
                        if self.active==True:
                            self.active=False
                            self.image=self.up
                        else:
                            self.active=True
                            self.image=self.dn
            else:
                self.clicked=0
                if self.over==0:
                    if not pygame.mixer.get_busy() and self.audio==1:
                        self.hover.play()
                        self.over=1
        else:
            self.clicked=0
            self.over=0
        
                

        
                
        
