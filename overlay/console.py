import pygame
from time import sleep

running = 1

LEFT = 1
CENTER = 2
RIGHT = 3
QUIT = 4
PREVIEW = 5
SEND = 6

def show():
    screen = pygame.display.set_mode((640, 400), pygame.FULLSCREEN)
    ret = 4

    while True:
        event = pygame.event.poll()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            ret = LEFT
            break
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            ret = RIGHT
            break
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == CENTER:
            ret = CENTER
            break
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            ret = QUIT
            break
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            ret = PREVIEW
            break
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            ret = SEND
            break
        sleep(0.1)
        
    pygame.display.quit()
    return ret

if __name__ == "__main__":
    show()
