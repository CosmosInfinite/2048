import pygame
import logic

#Initialise pygame
pygame.init()

#Fonts
Font = pygame.font.Font("OpenSans-Regular.ttf", 20)
mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

# State Variable
play=True
#ColorDict
color_tile={
  "2":(255, 251, 133),
  "4":(247, 240, 37),
  "8":(252, 174, 38),
  "16":(255, 102, 0),
  "32":(230, 116, 50),
  "64":(255, 38, 0)
}
#Set screen size
screen=pygame.display.set_mode((400,600))

#Set title and icon
pygame.display.set_caption("2048")
icon=pygame.image.load("2048.png")
pygame.display.set_icon(icon)

state=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [2,0,0,0]]
while True:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      break
    if event.type==pygame.KEYDOWN and not play:
      if event.key==pygame.K_RETURN:
        play=True
        state=[[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [2,0,0,0]]
    if event.type==pygame.KEYDOWN and play:
      if event.key==pygame.K_UP:
        state=logic.move(state,"UP")
        state=logic.action(state,"UP")
        state=logic.rand_gen(state)
      if event.key==pygame.K_DOWN:
        state=logic.move(state,"DOWN")
        state=logic.action(state,"DOWN")
        state=logic.rand_gen(state)
      if event.key==pygame.K_LEFT:
        state=logic.move(state,"LEFT")
        state=logic.action(state,"LEFT")
        state=logic.rand_gen(state)
      if event.key==pygame.K_RIGHT:
        state=logic.move(state,"RIGHT")
        state=logic.action(state,"RIGHT")
        state=logic.rand_gen(state)
      
  screen.fill((255,255,255))
  score=str(logic.score(state))
  scorel=mediumFont.render("Score:",True,(0,0,0))
  scored=mediumFont.render(score,True,(0,0,0))
  score_Rect=pygame.Rect(40,10,190,190)
  pygame.draw.rect(screen,((247, 240, 37)), score_Rect)
  screen.blit(scorel,(45,60))
  screen.blit(scored,(45,90))
  tile_size=80
  tile_origin=(40,240)
  tiles = []
  big_rect=pygame.Rect(tile_origin[0],tile_origin[1],332,332)
  for i in range(4):
    row = []
    for j in range(4):
      rect = pygame.Rect(tile_origin[0] +j*tile_size+(j+1)*3,tile_origin[1] + i * tile_size+(i+1)*3,tile_size,tile_size)
      if state[i][j]==0:
        pygame.draw.rect(screen, (220,220,220), rect)
      elif state[i][j]<128:
        pygame.draw.rect(screen,color_tile[str(state[i][j])],rect)
      else:
        pygame.draw.rect(screen,color_tile["2"],rect)

      if state[i][j]!=0:
        move = mediumFont.render(str(state[i][j]), True,(0,0,0))
        moveRect = move.get_rect()
        moveRect.center = rect.center
        screen.blit(move, moveRect)
      row.append(rect)
    tiles.append(row)
  if logic.check_end(state):
    game = mediumFont.render("GAME", True,(255,0,0))
    over = mediumFont.render("OVER", True,(255,0,0)) 
    screen.blit(game,(270,60))
    screen.blit(over,(270,90))
    restart =  mediumFont.render("press enter to restart", True,(0,0,0))
    screen.blit(restart,(40,200)) 
    play=False
  else:
    goal = mediumFont.render("GOAL:", True,(0,255,0))
    reach = mediumFont.render("REACH 2048", True,(0,255,0))
    screen.blit(goal,(270,60))
    screen.blit(reach,(240,90))

  pygame.display.update()