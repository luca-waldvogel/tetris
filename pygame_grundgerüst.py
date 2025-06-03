import pygame as pg

ZEILEN = 20
SPALTEN = 10
BLOCK_GROESSE = 30

# pygame ab Version 2.0 wird benötigt
# Installation im Terminal mit
#   --> pip install pygame (windows)
#   --> pip3 install pygame (mac)
#   --> sudo apt-get install python3-pygame (Linux Debian/Ubuntu/Mint)

stein_pos = [SPALTEN // 2, 0] # Koodination des Blöckes mitte, ganz oben

pg.init()
größe = breite, höhe = SPALTEN * BLOCK_GROESSE, ZEILEN * BLOCK_GROESSE
fenster = pg.display.set_mode(größe)


clock = pg.time.Clock()
zeit = 0 # es überprüft die Zeit vom Block
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
  fenster.fill('black')
  zeichne_stein()

  for ereignis in pg.event.get():
    if ereignis.type == pg.QUIT or ereignis.type == pg.KEYDOWN and ereignis.key == pg.K_ESCAPE: quit()

  pg.display.flip()
