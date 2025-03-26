
import pygame
import random

pygame.init()

szerokosc_okna = 500
wysokosc_okna = 700
okno = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
pygame.display.set_caption("Flappy Birdzik")

tlo = pygame.image.load('flappy bird background.jpg')
tlo = pygame.transform.scale(tlo, (szerokosc_okna, wysokosc_okna))
ptak_obraz = pygame.image.load('pngegg.png')
ptak_obraz = pygame.transform.scale(ptak_obraz, (80, 60))

bialy = (255, 255, 255)
czarny = (0, 0, 0)
zielony = (0, 255, 0)
czerwony = (255, 0, 0)
blekitny = (135, 206, 250)

ptak_x = 50
ptak_y = 300
predkosc_ptaka = 0
grawitacja = 0.5
skok = -10
wysokosc_podlogi = 570


rura_szerokosc = 60
rura_x = 400
rura_wysokosc = random.randint(100, 400)
przestrzen_miedzy_rurami = 150
predkosc_rur = 3

punkty = 0
czcionka = pygame.font.Font(None, 36)

fps = 60
zegar = pygame.time.Clock()


def rysuj():
    okno.blit(tlo, (0,0))
    pygame.draw.rect(okno, zielony, (rura_x, 0, rura_szerokosc, rura_wysokosc))
    pygame.draw.rect(okno, zielony, (rura_x, rura_wysokosc + przestrzen_miedzy_rurami, rura_szerokosc, wysokosc_podlogi - rura_wysokosc - przestrzen_miedzy_rurami))
    okno.blit(ptak_obraz, (ptak_x - 20, ptak_y - 15))
    tekst = czcionka.render(f"Punkty: {punkty}", True, czarny)
    okno.blit(tekst, (10, 10))
    pygame.display.update()


def narysuj_przycisk(tekst, x, y, szer, wys, kolor, kolor_tekst):
    pygame.draw.rect(okno, kolor, (x, y, szer, wys), border_radius=15)
    tekst_render = czcionka.render(tekst, True, kolor_tekst)
    okno.blit(tekst_render, (x + (szer - tekst_render.get_width()) // 2, y + (wys - tekst_render.get_height()) // 2))


def ekran_poczatkowy():
    okno.blit(tlo, (0, 0))
    narysuj_przycisk("Start", (szerokosc_okna - 200) // 2, wysokosc_okna // 2 - 60, 200, 50, zielony, czarny)
    pygame.display.update()


def ekran_przegranej():
    okno.blit(tlo, (0, 0))
    tekst_wynik = czcionka.render(f"Osiągnięty wynik: {punkty}", True, czarny)
    okno.blit(tekst_wynik, ((szerokosc_okna - tekst_wynik.get_width()) // 2, wysokosc_okna // 4))

    narysuj_przycisk("Zagraj ponownie", (szerokosc_okna - 200) // 2, wysokosc_okna // 2 - 60, 200, 50, zielony, czarny)
    narysuj_przycisk("Wyjście", (szerokosc_okna - 200) // 2, wysokosc_okna // 2 + 20, 200, 50, zielony, czarny)
    pygame.display.update()


def gra():
    global ptak_y, predkosc_ptaka, rura_x, rura_wysokosc, punkty
    ptak_y = 300
    predkosc_ptaka = 0
    rura_x = 400
    rura_wysokosc = random.randint(100, 400)
    punkty = 0
    dziala = True

    while dziala:
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                pygame.quit()
                exit()
            if zdarzenie.type == pygame.KEYDOWN:
                if zdarzenie.key == pygame.K_SPACE:
                    predkosc_ptaka = skok

        predkosc_ptaka += grawitacja
        ptak_y += int(predkosc_ptaka)
        rura_x -= predkosc_rur

        if rura_x + rura_szerokosc < 0:
            rura_x = szerokosc_okna
            rura_wysokosc = random.randint(100, 400)
            punkty += 1

        if ptak_y >= wysokosc_podlogi - 15:
            dziala = False

        if (rura_x < ptak_x < rura_x + rura_szerokosc) and (
                ptak_y < rura_wysokosc or ptak_y > rura_wysokosc + przestrzen_miedzy_rurami):
            dziala = False

        rysuj()
        zegar.tick(fps)

    ekran_przegranej()


def main():
    ekran_poczatkowy()
    while True:
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                pygame.quit()
                exit()
            if zdarzenie.type == pygame.MOUSEBUTTONDOWN:
                x, y = zdarzenie.pos
                if (szerokosc_okna - 200) // 2 <= x <= (szerokosc_okna - 200) // 2 + 200:
                    if wysokosc_okna // 2 - 60 <= y <= wysokosc_okna // 2 - 10:
                        gra()
                    if wysokosc_okna // 2 + 20 <= y <= wysokosc_okna // 2 + 70:
                        pygame.quit()
                        exit()

        pygame.display.update()


if __name__ == "__main__":
    main()
