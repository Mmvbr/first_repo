import pygame
from pygame.draw import circle, rect, polygon
pygame.init()

FPS = 30

screen = pygame.display.set_mode((400, 400))
screen.fill((255,255,255))
circle(screen,(255,255,0),(200,200),100)
circle(screen,(255,0,0),(150,170),20)
circle(screen,(255,0,0),(240,170),20)
circle(screen,(0,0,0),(150,170),5)
circle(screen,(100,0,0),(300,10),5)
circle(screen,(0,0,0),(240,170),5)
rect(screen, (0, 0, 0), (150, 250, 100, 10))
polygon(screen,(0,0,0),[(170,160),(170,140),(100,150),(110,180)])
polygon(screen,(0,0,0),[(400-170,160),(400-170,140),(400-95,150),(400-110,190)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
