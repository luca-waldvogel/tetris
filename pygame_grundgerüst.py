import pygame as pg

pg.init()

ZEILEN = 20
SPALTEN = 10
BLOCK_GROESSE = 30

stein_pos = [SPALTEN // 2, 0] # Koodination des Blöckes mitte, ganz oben

grösse = breite, höhe = SPALTEN * BLOCK_GROESSE, ZEILEN * BLOCK_GROESSE
fenster = pg.display.set_mode(grösse)


clock = pg.time.Clock()
zeit = 0 # kontrolliert die Fallzeit des Steins
FPS = 40
def zeichne_stein():
    x, y = stein_pos
    pg.draw.rect(
        fenster,
        (0, 255, 255),  # farbe des Blockes: cyan
        (x * BLOCK_GROESSE, y * BLOCK_GROESSE, BLOCK_GROESSE, BLOCK_GROESSE)
    )
# Zeichenschleife mit FPS Bildern pro Sekunde
while True:
  clock.tick(FPS)
  dt = clock.get_time() #sammle die Zeit bei jede Frame 
  zeit += dt

  if zeit > 500:                      # jede 0.5 sekunde eine Zeile unten
    if stein_pos[1] < ZEILEN - 1:     # wenn noch nicht ganz unten
        stein_pos[1] += 1
    zeit = 0

  fenster.fill('black')
  zeichne_stein()

  for ereignis in pg.event.get():
    if ereignis.type == pg.QUIT or ereignis.type == pg.KEYDOWN and ereignis.key == pg.K_ESCAPE: quit()

  pg.display.flip()
