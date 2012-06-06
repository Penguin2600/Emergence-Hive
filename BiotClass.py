import pygame

class Biot():
    def __init__(self, location, velocity, points): #initialize (contructor)
        self.location=location
        self.velocity=velocity
        self.points=points
        self.deltapoints=[] #array for delta points

    def update(self):

        self.location[0]+=self.velocity[0]  #do x movement
        self.location[1]+=self.velocity[1]  #do y movement

    def draw(self, surface):
        #pygame.draw.lines(Surface, color, closed, pointlist, width=1): return Rect
        
        self.deltapoints=[] # do position offsets
        for point in self.points:
            x=point[0]+self.location[0]
            y=point[1]+self.location[1]
            self.deltapoints.append((x,y))
            
        pygame.draw.lines(surface, (255,0,0), False, self.deltapoints, 1)
