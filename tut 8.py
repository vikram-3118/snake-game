import  pygame

pygame.init()

#color
white =(255,255,255)
red=  (255,0,0)
black= (0,0,0)

screen_width = 900
screen_height = 600

pygame.display.set_caption("snake of vikbro")

## GAME SPECIFIC VARIABLE
exit_game = False
game_over = False
gameWindow = pygame.display.set_mode((screen_width,screen_height))

#  game loop

while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:         ### we can quit game now  loop come outside
            exit_game=True

    gameWindow.fill(white)
    pygame.display.update()

pygame.quit()
quit()








