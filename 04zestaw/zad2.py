import pygame as pg
import sys

from pygame.constants import SCRAP_PPM
pg.init()


def main():
    vx = float(input("skladowa x pretkosci: "))
    vy = float(input("skladowa y pretkosci: "))

    clock = pg.time.Clock()

    pg.display.set_caption('Rzut ukosny / spadek swobodny')
    icon = pg.image.load(r'.\moon.jpg')

    pg.display.set_icon(icon)

    pg.mixer.music.load(r'.\music.mp3')
    pg.mixer.music.play(-1)  # -1 -> nieskonczona petla

    size = width, height = 800, 800
    screen = pg.display.set_mode(size)

    speed = [vx, vy]
    accel = [0, 9.81]
    t = 1/4
    x = width/2
    y = height/2

    image = pg.image.load(r'.\moon.jpg')
    image = pg.transform.scale(image, size)

    surf_center = (
        (width - image.get_width())/2,
        (height - image.get_height())/2
    )

    screen.blit(image, surf_center)

    ball = pg.image.load(r'.\ball.png')
    ball = pg.transform.scale(
        ball, (ball.get_width()//3, ball.get_height()//3))
    screen.blit(ball, (width/2, height/2))
    ballrect = ball.get_rect(center=(width/2, height/2))

    pg.display.flip()

    while True:
        screen.blit(ball, (x, y))
        ballrect = ball.get_rect(center=(x, y))
        clock.tick(60)
        pg.time.delay(50)

        speed[1] += accel[1]*t

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        else:
            x += speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        else:
            y += speed[1]

        screen.blit(image, surf_center)
        screen.blit(ball, ballrect)
        pg.display.flip()


if __name__ == '__main__':
    main()
    pg.quit()
    sys.exit()
