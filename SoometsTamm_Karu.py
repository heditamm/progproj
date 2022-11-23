import pygame
import time
import random
from pygame.locals import *

punktid = 0
 
#ekraan
(width, height) = (1200, 800)
pygame.font.init()
font = pygame.font.SysFont("Arial", 25)

mustikas_kiirus = 5
mesilane_kiirus = 5
karu_kiirus = 7
pygame.display.set_caption("Karu mäng")
bg_img = pygame.image.load("taust.jpg")
bg_img = pygame.transform.scale(bg_img, (width, height))

screen = pygame.display.set_mode((width, height))

pygame.display.flip()

#pildid
mustikasimg = pygame.image.load("mustikas.png")
mustikas_x=random.randint(50,750)
mustikas_y=random.randint(0,15)
mustikas_laius=100
mustikas_kõrgus=100
mustikas=pygame.transform.scale(mustikasimg,(mustikas_laius,mustikas_kõrgus))

johvikas = pygame.image.load("johvikas.png")
poldmari = pygame.image.load("poldmari.png")
mesilaneimg = pygame.image.load("mesilane.png")
mesilane_x=random.randint(50,750)
mesilane_y=random.randint(0,15)
mesilane_laius=100
mesilane_kõrgus=100
mesilane=pygame.transform.scale(mesilaneimg,(mesilane_laius,mesilane_kõrgus))


karu = pygame.image.load("karu.png")
karu = pygame.transform.scale(karu,(300,300))


#Kell
kell = pygame.time.Clock()

karu_x = 20
karu_y= 600


finished = False
while not finished:
    kell.tick(60)
    screen.blit(bg_img,(0, 0))
    #liikuv karu
    nupud = pygame.key.get_pressed()
    if nupud[pygame.K_a]:
        karu_x = karu_x-karu_kiirus
    if nupud[pygame.K_d]:
        karu_x=karu_x+karu_kiirus
    mustikas_rect=screen.blit(mustikas,(mustikas_x,mustikas_y))
    mesilane_rect=screen.blit(mesilane,(mesilane_x,mesilane_y))
    screen.blit(karu, (karu_x, karu_y))
    
    pygame.display.flip()
    
    #kui vajutad risti siis läheb kinni
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    
    karu_rect = karu.get_rect(center=(karu_x,karu_y))
    if karu_rect.colliderect(mustikas_rect):#kontrollib kas lähevad kokku
        mustikas_x=random.randrange(0,width)
        mustikas_y=-75
        punktid+=1
    
    if karu_rect.colliderect(mesilane_rect):
        punktid = 0
        pygame.quit()
        quit()
        #tekst = font.render("Mäng läbi!", True, (255,255,255))

    
    if punktid == 10:
        punktid = 0
        pygame.quit()
        quit()
        
        
    mesilane_y=mesilane_y+mesilane_kiirus
    if mesilane_y>height:
        mesilane_x=random.randrange(0,width)
        mesilane_y=-25
    mustikas_y = mustikas_y + mustikas_kiirus
    if mustikas_y > height:
        mustikas_x=random.randrange(0,width)
        mustikas_y=-25
"""
running = True
while running:
    screen.blit(bg_img,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()"""

pygame.quit()


