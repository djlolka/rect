import pygame

try:
    a, b = input().split()
except:
    print('Неправильный формат ввода')


def draw(screen):
    screen.fill((0, 0, 0))
    screen.fill(pygame.Color('red'), pygame.Rect(1, 1, int(a) - 1, int(b) - 1))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Крест')
    if a.isdigit() and b.isdigit():
        size = width, height = int(a), int(b)
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    else:
        print('Неправильный формат ввода')

