import pygame, time


black = (0,0,0)

pygame.init()
Res = [700,500]
win = pygame.display.set_mode(Res, pygame.RESIZABLE)

x = 250
y = Res[1] - 100
radius = 15
vel_x = 10
vel_y = 10
jump = False

prevTime = time.time()

def updateRes():
  global Res
  newW = pygame.display.Info().current_w
  newH = pygame.display.Info().current_h
  Res[0]=newW
  Res[1]=newH
  
  

run = True
while run:
    updateRes()
    win.fill(black)
    pygame.draw.circle(win, (255, 255, 255), (int(x), int(y)), radius)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Movement
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and x > 0:
        x -= vel_x
    if userInput[pygame.K_RIGHT] and x < Res[0]:
        x += vel_x

    #Jump
    if jump is False and userInput[pygame.K_UP]:
        jump = True
    if jump is True:
        y -= vel_y*4
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10

    pygame.time.delay(30)
    pygame.display.update()