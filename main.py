import pygame  # importáljuk a modult
import sys
from random import randint   # random modulból importáljuk a randintet

# * konstansok  /változó nevét nagy betűvel írjuk ezzel jelezzük, hogy konstans/
SCREEN_SIZE = WIDTH, HEIGHT = (1280, 720)
NUMBER_OF_PEOPLE = 10
PERSON_SPEED = 15
PERSON_COLOR_CLEAR = (200, 150, 0)
PERSON_COLOR_INFECTED = (200, 0, 0)
PERSON_COLOR_IMMUNE = (0, 150, 0)
PERSON_AURA = 20


# * inicializálás /kezdeti feltételek létrehozása/
pygame.init()  # pygame indítása
# kijelző létrehozása, méretezése
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Járvány szimulátor 1.0")  # ablak címe
fps = pygame.time.Clock()
pause = False


# * Person osztály létrehozása
class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = randint(-1, 1)
        self.dy = randint(-1, 1)

    def move(self):
        if randint(1, 30) == 1:
            self.dx = randint(-1, 1)
        if randint(1, 30) == 1:
            self.dy = randint(-1, 1)

        if PERSON_AURA < self.x + self.dx < WIDTH - PERSON_AURA:
            self.x += self.dx
        if PERSON_AURA < self.y + self.dy < HEIGHT - PERSON_AURA:
            self.y += self.dy


def modify(people):
    for person in people:
        person.move()


def draw(people):
    screen.fill((20, 20, 20))

    for person in people:
        pygame.draw.circle(
            screen,
            PERSON_COLOR_CLEAR,
            (person.x, person.y),
            PERSON_AURA,
            0
        )

    pygame.display.update()
    fps.tick(PERSON_SPEED)


# * emberek létrehozása
main_people_list = [Person(randint(50, WIDTH-50), randint(50, HEIGHT-50))
                    for i in range(NUMBER_OF_PEOPLE)]


# * fő programrész

# ezzel oldjuk meg, hogy ne zátja be rögtön az ablakot:
while True:  # végtelen ciklus
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
    if not pause:
        modify(main_people_list)
        draw(main_people_list)
