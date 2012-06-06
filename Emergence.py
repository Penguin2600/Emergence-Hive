import pygame
from pygame.locals import *
from BiotClass import Biot
from math import *

pygame.init()
keys = {pygame.K_SPACE : False} #declare keys we will use

screen = pygame.display.set_mode([800, 800]) #setup a 800x800 screen aka "surface"

pointList = [(0,10),(10,30),(20,15),(22,30)] # list of points.
biot1 = Biot([100,100], [2,3], pointList)  #Make a biot at 100,100 moving x+2 y+3

def get_dist(x1,x2,y1,y2): #random unused function for david's benefit
    
    Scale=20
    Distance = sqrt( pow((x2-x1),2) + pow((y2-y1),2))
    Radius = Distance*Scale
    return Radius


def main():
    for event in pygame.event.get():    #check for keypresses 
        if event.type == pygame.KEYDOWN:
            keys[event.key] = True
        elif event.type == pygame.KEYUP:
            keys[event.key] = False
    if keys[pygame.K_SPACE]:            #this kills the crab
        exit(0)


    biot1.update()                      #update biot          
    screen.fill([0,0,0])                #blank the buffer
    biot1.draw(screen)                        #draw the biot to buffer
    pygame.display.update()             #redraw the screen from buffer (this is slow we could redraw only small areas)


if __name__ == "__main__":

    while 1: #while the programm is running loop the main function  
        main()
        pygame.time.delay(10)#delay 10ms per loop to slow it down a bit
