import pygame  
import datetime  
import time

pygame.init()  

WIDTH, HEIGHT = 800, 600  
Display = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("MOUSE")  

background = pygame.image.load("clock.png")  
sec_line = pygame.image.load("leftarm.png")
min_line = pygame.image.load("rightarm.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  

min_line  = pygame.transform.scale(min_line, (700,900)) 
sec_line = pygame.transform.scale(sec_line, (60,600))  

CENTER = (WIDTH / 2, HEIGHT / 2)  
def rotate(imag,angle):
    rotated_image = pygame.transform.rotate(imag, angle) 
    rect = rotated_image.get_rect(center=CENTER) 
    Display.blit(rotated_image, rect.topleft) 
    
running = True  
while running:  
    Display.blit(background,(0,0))  
    time_now = time.localtime()
    minut =  time_now.tm_min
    seconds = time_now.tm_sec
    sec_angle = -(seconds * 6 )
    min_angle = -(minut * 6 )
    rotate(sec_line,sec_angle)
    rotate(min_line,min_angle)
    pygame.display.update()  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False   
    pygame.time.delay(1000)  

pygame.quit()