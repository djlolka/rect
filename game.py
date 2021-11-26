import pygame

try:
    a, b = input().split()
except:
    print('Неправильный формат ввода')


def draw(screen):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (int(a), int(b)), width=5)
    pygame.draw.line(screen, (255, 255, 255), (0, int(b)), (int(a), 0), width=5)


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

