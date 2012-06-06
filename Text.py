import pygame

class Print(pygame.sprite.Sprite):
    def __init__(self,text,pos=(0,0),color=[0,0,0],size=12):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.topleft=pos             
        
                

        
                
        
