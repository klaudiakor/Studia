import pygame
from random import randint
import sys

from pygame import key
from pygame.constants import KEYDOWN

pygame.init()

# kolory
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)
score_table = [0]


class Rakietka(pygame.sprite.Sprite):
    # klasa Rakietka dziedziczy z klasy "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy najpierw konstruktor klasy bazowej (Sprite)
        # dzięki metodzie super() dziedziczymy wszystkie elementy klasy bazowej
        super().__init__()

        # przekazanie koloru Rakietka oraz szerokości i wysokości, kolor tła i ustawienie go na przezroczyste
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysuję Rakietka jako prostokąt
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x > 600:
            self.rect.x = 600


class Pilka(pygame.sprite.Sprite):
    # klasa Pilka dziedziczy ze "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy konstruktor klasy bazowej
        super().__init__()

        # przekazujemy rozmiary, kolor, przezroczystość
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysowanie piłki (jako prostokącika)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # losowanie prędkości
        self.velocity = [randint(-8, 8), randint(4, 8)]

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[1] = -self.velocity[1]
        self.velocity[0] = randint(-8, 8)


def game_over_info(score):
    font = pygame.font.Font(None, 74)
    font2 = pygame.font.Font(None, 30)
    text1 = font.render("GAME OVER", 1, BIALY)
    text2 = font.render("SCORE: " + str(score), 1, BIALY)
    text3 = font.render(
        "MAX SCORE: " + str(max(score_table)), 1, BIALY)
    text4 = font2.render("PRESS C TO PLAY AGAIN", 1, BIALY)
    text1_rec = text1.get_rect(center=(700/2, 150))
    text2_rec = text2.get_rect(center=(700/2, 200))
    text3_rec = text3.get_rect(center=(700/2, 250))
    text4_rec = text4.get_rect(center=(700/2, 440))

    screen.fill(CZARNY)
    screen.blit(text1, text1_rec)
    screen.blit(text2, text2_rec)
    screen.blit(text3, text3_rec)
    screen.blit(text4, text4_rec)
    pygame.display.flip()


def game_over(score):
    screen.fill(CZARNY)
    game_over_info(score)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # zamknięcie okienka
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_c:
                    score_table.append(score)
                    graj()


def graj():
    rakietka = Rakietka(BIALY, 100, 10)
    rakietka.rect.x = 200
    rakietka.rect.y = 470

    pileczka = Pilka(BIALY, 10, 10)
    pileczka.rect.x = 345
    pileczka.rect.y = 0

    # lista wszystkich widzalnych obiektów potomnych z klasy Sprite
    all_sprites_list = pygame.sprite.Group()

    # dodanie obu rakietek i piłeczki do listy
    all_sprites_list.add(rakietka)
    all_sprites_list.add(pileczka)
    # zaczynamy właściwy blok programu
    kontynuuj = True

    # służy do kontroli liczby klatek na sekudnę (fps)
    clock = pygame.time.Clock()

    # Początkowe wyniki graczy
    score = 0

    # -------- GLÓWNA PĘTLA PROGRAMU -----------
    while kontynuuj:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # zamknięcie okienka
                kontynuuj = False

        # ruchy obiektów Rakietkas klawisze strzałka góra dół lub klawisz w s
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rakietka.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            rakietka.moveRight(5)

        # aktualizacja listy duszków
        all_sprites_list.update()

        # sprawdzenie czy piłeczka nie uderza w którąś ścianę
        # i odpowiednie naliczenie punktu jeśli minie rakietkę A lub B i uderzy w ścianę za n
        if pileczka.rect.x >= 690:
            pileczka.velocity[0] = -pileczka.velocity[0]
        if pileczka.rect.x <= 0:
            pileczka.velocity[0] = -pileczka.velocity[0]
        if pileczka.rect.y > 490:
            game_over(score)
            #pileczka.velocity[1] = -pileczka.velocity[1]
        if pileczka.rect.y < 0:
            pileczka.velocity[1] = -pileczka.velocity[1]

        # sprawdzenie kolizji piłeczki z obiektem rakietkaA lub rakietkaB
        if pygame.sprite.collide_mask(pileczka, rakietka):
            score += 1
            pileczka.bounce()

        # RYSOWANIE
        # czarny ekran
        screen.fill(CZARNY)

        # narysowanie obiektów
        all_sprites_list.draw(screen)

        # wyświetlanie wyników
        font = pygame.font.Font(None, 74)
        text = font.render(str(score), 1, BIALY)
        screen.blit(text, (349, 10))

        # odświeżenie / przerysowanie całego ekranu
        pygame.display.flip()

        # 60 klatek na sekundę
        clock.tick(60)


# definiujemy rozmiary i otwieramy nowe okno
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

graj()

# koniec
pygame.quit()
