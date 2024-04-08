import pygame
import sys
import random

# Инициализация модулей pygame
pygame.init()


# Класс, описывающий змейку
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (0, 0, 255)

    # Обновление позиции змейки
    def get_head_position(self):
        return self.positions[0]

    # Определение направления движения
    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    # Обновление всей змейки
    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRIDSIZE)) % WIDTH), (cur[1] + (y * GRIDSIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    # Сброс игры при столкновении змейки самой с собой
    def reset(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    # Отрисовка змейки
    def draw(self, surface):
       for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRIDSIZE, GRIDSIZE))


# Класс, описывающий еду
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 0, 0)
        self.randomize_position()

    # Обновление позиции еды
    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRIDSIZE, random.randint(0, GRID_HEIGHT - 1) * GRIDSIZE)

    # Отрисовка еды
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRIDSIZE, GRIDSIZE))


# Определение параметров игрового окна и объектов
WIDTH = 480
HEIGHT = 480
GRIDSIZE = 20
GRID_WIDTH = WIDTH // GRIDSIZE
GRID_HEIGHT = HEIGHT // GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake()
    food = Food()

    # Главный цикл программы
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn(UP)
                elif event.key == pygame.K_DOWN:
                    snake.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.turn(RIGHT)

        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        snake.draw(surface)
        food.draw(surface)

        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(6)


if __name__ == "__main__":
    main()