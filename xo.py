# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

cells = [
    {'start_pos':(0,0), 'x_checked':False, 'o_checked':False, 'end_pos':(190,190)},
    {'start_pos':(200,0), 'x_checked':False, 'o_checked':False, 'end_pos':(390,190)},
    {'start_pos':(400,0), 'x_checked':False, 'o_checked':False, 'end_pos':(590,190)},

    {'start_pos':(0,200), 'x_checked':False, 'o_checked':False, 'end_pos':(190,390)},
    {'start_pos':(200,200), 'x_checked':False, 'o_checked':False, 'end_pos':(390,390)},
    {'start_pos':(400,200), 'x_checked':False, 'o_checked':False, 'end_pos':(590,390)},

    {'start_pos':(0,400), 'x_checked':False, 'o_checked':False, 'end_pos':(190,590)},
    {'start_pos':(200,400), 'x_checked':False, 'o_checked':False, 'end_pos':(390,590)},
    {'start_pos':(400,400), 'x_checked':False, 'o_checked':False, 'end_pos':(590,590)},
]
combinations=[
    [0,1,2],
    [3,4,5],
    [6,7,8],

    [0,3,6],
    [1,4,7],
    [2,5,8],

    [0,4,8],
    [2,4,6],

]

def get_winner(combinations):
    for combo in combinations:
        if cells[combo[0]][f'{player}_checked'] and cells[combo[1]][f'{player}_checked'] and cells[combo[2]][f'{player}_checked']:
            print("we have a winner")
            break   
                

pos = (0,0)
player = "x"
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    for cell in cells:
        pygame.draw.rect(screen, "white", (cell['start_pos'][0],cell['start_pos'][1],190,190))

        if  cell['start_pos'][0]<pos[0]<cell['end_pos'][0] and cell['start_pos'][1]<pos[1]<cell['end_pos'][1] and  (not cell['o_checked'] and not cell['x_checked']):
            
            cell[f'{player}_checked']=True
            get_winner(combinations)
            if player =="x":
                player="o"
            else:
                player="x"


            pos=(0,0)
            

        if cell['o_checked']:
            pygame.draw.circle(screen,'red',(cell['start_pos'][0]+95,cell['start_pos'][1]+95), 60)
            pygame.draw.circle(screen,'white',(cell['start_pos'][0]+95,cell['start_pos'][1]+95), 50)
        if cell['x_checked']:
            pygame.draw.line(screen, 'blue', cell['start_pos'], cell['end_pos'], 10)
            pygame.draw.line(screen, 'blue', (cell['end_pos'][0],cell['start_pos'][1]), (cell['start_pos'][0],cell['end_pos'][1]), 10)
    
    
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()