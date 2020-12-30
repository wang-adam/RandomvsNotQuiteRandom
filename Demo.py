import pygame, sys
from pygame.locals import *
import random
from array import *
import math
from tkinter import * 

BLACK = (0,0,0)
WHITE = (255,255,255)

root = Tk() 

window_width = root.winfo_screenwidth()-50
window_height = root.winfo_screenheight()-100
point_thickness = 3
display_surf = pygame.display.set_mode((window_width,window_height))

#Main Function
def main():
    pygame.init()
    global display_surf
    display_surf = pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption('Random vs Fake Random')

#Draws the black window and divider line. 
def drawArena():
    display_surf.fill((0,0,0))
    #Draw outline of arena
    pygame.draw.rect(display_surf, BLACK, ((0,0),(window_width,window_height)))
    #Draw center line
    pygame.draw.line(display_surf, WHITE, ((window_width/2),0),((window_width/2),window_height),4)

#Draws the random points on the left side of the divider.
def drawRandom():
    xcor = random.randint(0,(window_width-1)//2)
    ycor = random.randint(0,window_height)
    pygame.draw.circle(display_surf,WHITE,(xcor,ycor),point_thickness)


#Set of all not-so-random points
past_points = set()

#Draws the "random" points such that they are at least a minimum distance away from each other. 
def drawFakeRandom(past_points, min_distance):
    drawn = False
    while not drawn:
        farEnough = True
        xcor = random.randint((window_width+1)//2, window_width)
        ycor = random.randint(0,window_height)
        for point in past_points:
            oldxcor = point[0]
            oldycor = point[1]
            dis = abs(math.dist((oldxcor,oldycor),(xcor,ycor)))
            if dis < min_distance:
                farEnough = False
                break
        if farEnough:
            pygame.draw.circle(display_surf,WHITE,(xcor,ycor),point_thickness)
            new_point = (xcor,ycor)
            past_points.add(new_point)
            drawn = True
                


drawArena()

#How many points/calls to the random and no-so-random functions.
for i in range(500):
    drawRandom()
    drawFakeRandom(past_points,17)

#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            sys.exit()    
    pygame.display.update()


if __name__=='__main__':
    main()
