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

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    for cell in cells:
        pygame.draw.rect(screen, "white", (cell['start_pos'][0],cell['start_pos'][1],190,190))
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()