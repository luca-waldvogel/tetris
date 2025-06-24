# M426 Tetris
# Tetris in Python

Ein klassisches Tetris-Spiel, programmiert als Gruppenprojekt mit `pygame`.  
Das Spiel bietet ein vollständiges Spielerlebnis inklusive Musik, Punktesystem, Pausenfunktion und animiertem "Soft Drop".

---

## Features

- Klassisches Tetris-Gameplay mit zufälligen Formen  
- Punktezähler  
- Pausenfunktion (`P`)  
- Game-Over-Bildschirm mit Neustartoption (`R`)  
- Musik im Hintergrund (`sound/Tetris.mp3`)  
- Game Over Sound (`sound/game_over.mp3`)  
- Automatische Beschleunigung des Spiels über Zeit  

---

## ▶So startest du das Spiel

### Voraussetzungen installieren

Installiere `pygame`, falls noch nicht vorhanden:

```bash
pip install pygame
```

---

## Das Projekt besteht aus mehreren Modulen

```
├── main.py               # Hauptprogramm (Spiel-Loop)
├── config.py             # Spielfeld-Größe
├── field.py              # Spiellogik & Spielfeld
├── piece.py              # Tetris-Steine
├── ui.py                 # Score & UI-Anzeige
├── sound/
│   ├── Tetris.mp3        # Hintergrundmusik
│   └── game_over.mp3     # Game Over Sound
└── README.md             # Dieses Dokument
```

---

## Steuerung 

| Taste       | Funktion                      |
| ----------- | ----------------------------- |
| `←` / `→`   | Stein bewegen                 |
| `↓`         | Stein schneller fallen lassen |
| `↑`         | Stein rotieren                |
| `Leertaste` | Stein sofort fallen lassen    |
| `P`         | Spiel pausieren / fortsetzen  |
| `R`         | Neustart nach Game Over       |
| `ESC`       | Spiel beenden                 |

---

## Mitwirkende

- Luca Waldvogel  
- Deepthi Chalackal  
- Lidija Srejic  
- Oguzhan Cetinkaya  
- Milena Schürch  

---

## Hinweise 

- Musik- und Sounddateien müssen im Verzeichnis `sound/` vorhanden sein.  
- Bei Fehlern mit `pygame.mixer`: Stelle sicher, dass die Audioausgabe auf deinem System korrekt konfiguriert ist.
git 

---
