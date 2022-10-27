import pygame, time, threading

class color():
  black = (0,0,0)
  white = (255,255,255)
  red =(255,0,0)
  green = (0,255,0)
  blue = (0,0,255)

pygame.init()
Res = [700,500]
win = pygame.display.set_mode(Res, pygame.RESIZABLE)

x = 100
y = 10
radius = 15
vel_x = 10
vel_y = 10
jump = False

moveRight,moveLeft, bounce  = False, False, False

prevTime = time.time()

def updateRes():
  global Res
  newW = pygame.display.Info().current_w
  newH = pygame.display.Info().current_h
  Res[0]=newW
  Res[1]=newH

def gravity():
      #Jump
      global Res, y, vel_y, radius
    
      if y + radius * 2 <= Res[1]:
          y += vel_y*4
      if y + (radius * 2) >= Res[1]:
        y = Res[1] - radius

#set pos to the position of something and set sizex and y to the size of the item, insert any pos  to itemPos and it will check if that pos is inside the other, if so it will return True else False
def colide(pos, sizex, sizey, itemPos):

  if itemPos[0] >= pos[0] and itemPos[0] <= (pos[0] + sizex):
    if itemPos[1] >= pos[1] and itemPos[1] <= (pos[1] + sizey):
          return True
    else:
      return False
  else:
    return False


def drawLine(pos1, pos2):
      pygame.draw.line(win, color.red, pos1, pos2, 2)

def goto(endPos):
      global x,y,vel_y, vel_x
      if y >= 0 and y <= Res[1]:
        if x >= endPos[0]:
             x -= vel_x

      
        elif x <= endPos[0]:
              x += vel_x

        elif x == endPos[0]:
          pass

      
        if y >= endPos[1]:
              y -= vel_y
      
        elif y <= endPos[1]:
              y += vel_y

        elif y == endPos[1]:
          pass









#work on latter .TODO
def Console():
  while True:
        command = input("~$: ")
        print(list(command))
        if command.startswith()=="circle":
              print(command)
              command.pop(0)
              print(command)
        elif command == "":
              break

  
  
def main():
  hasClicked = False
  tryMove = False
  global x,y, Res, radius, vel_y, vel_x, win, jump, moveLeft,moveRight, bounce
  run = True
  nextMousePos = []
  while run:
      updateRes()
      win.fill(color.black)
      #print(x,y, nextMousePos, vel_x, vel_y, hasClicked, tryMove)
      pygame.draw.circle(win, color.white, (int(x), int(y)), radius)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False
  
      # Movement
      userInput = pygame.key.get_pressed()
      if moveLeft and x > 0:
          x -= vel_x
      if moveRight and x < Res[0]:
          x += vel_x
  
      
  
      



      if colide((x-radius,y-radius),radius*2,radius*2, pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            latestMousePos = pygame.mouse.get_pos()
            hasClicked = True

      elif hasClicked and pygame.mouse.get_pressed()[0]:
        nextMousePos = pygame.mouse.get_pos()
        nextMousePos = (round(nextMousePos[0],-1),round(nextMousePos[1],-1))

        hasClicked = False

      if hasClicked:
        drawLine((x,y), pygame.mouse.get_pos())
        tryMove = True

      if nextMousePos:
        if (x,y) != nextMousePos and tryMove:
              goto(nextMousePos)
              if nextMousePos == (x,y):
                tryMove = False

      pygame.time.delay(30)
      pygame.display.update()




      


if __name__ == "__main__":
  #ConsoleTread = threading.Thread(target=Console)
  #ConsoleTread.start()
  main()