import pygame
import math
pygame.init() #inicjalizacja pygame

WIDTH, HEIGHT = 900, 800  #rozmiar okna
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #
pygame.display.set_caption("Solar system simulation v1") #nazwa okienka

white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)
brown = (255, 204, 153)
red = (188, 39, 50)
grey = (80, 78, 81)

class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    scale = 250 / AU   #1AU = 100 pikseli
    TIMESTEP = 3600*24   #1dzień w sekundach

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0


    def draw(self, win):
        x = self.x * self.scale + WIDTH / 2
        y = self.y * self.scale + HEIGHT / 2

        pygame.draw.circle(win, self.color, (x, y), self.radius)


    def przyciaganie(self, other):
        other_x, other_y = other


def main():   #pętla, zeby okienko wyswietlalo sie caly czas
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, yellow, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1*Planet.AU, 0, 16, blue,5.9742 * 10**24)

    mars = Planet(-1.524* Planet.AU,0, 12 , red, 6.39 * 10 **23)

    mercury = Planet(0.387 * Planet.AU, 0, 8, grey, 3.30 *10**23)

    venus = Planet(0.723*Planet.AU,0, 14 , brown, 4.8685 * 10**24)



    planets = [sun, earth,mars, venus, mercury]

    while run:
        clock.tick(60)      #odswiezanie okna na sekune
        #WIN.fill(white)     wypelnienie ekranu kolorem
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(WIN)




        pygame.display.update()

    pygame.quit()

main()



