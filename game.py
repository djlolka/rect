import pygame

a = input()
b = input()


def draw(screen):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (int(a), int(b)), width=5)
    pygame.draw.line(screen, (255, 255, 255), (0, int(b)), (int(a), 0), width=5)


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    pygame.display.set_caption('Крест')
    # размеры окна:
    if a.isdigit() and b.isdigit():
        size = width, height = int(a), int(b)
        screen = pygame.display.set_mode(size)
        # формирование кадра:
        # команды рисования на холсте
        draw(screen)
        # ...
        # смена (отрисовка) кадра:
        pygame.display.flip()
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
    else:
        print('Неправильный формат ввода')

