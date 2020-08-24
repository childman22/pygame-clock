import pygame, sys, time

#general setup
pygame.init()
clock = pygame.time.Clock()

#setting up the main window
screen_width = 200
screen_height = 100
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('time')

#colours
bgcolour = (0, 0, 0)
font_colour = pygame.Color('springgreen')

#fonts
pygame.font.init()
myfont = pygame.font.SysFont(None, 54)

while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #getting the time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    textsurface = myfont.render(current_time, False, font_colour)

    #visuals
    screen.fill(bgcolour)
    screen.blit(textsurface,(25,25))

    #updating the window
    pygame.display.flip()
    clock.tick(60)
