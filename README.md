# Keep Running Buddy!

**Ein einfaches 2D-Spiel in Pygame, bei dem du versuchen musst, ankommenden Hindernissen auszuweichen.**  
Das Spiel ist noch in einer frühen Entwicklungsphase, soll aber später ein schnelles Cyberpunk-Jump’n’Run-Erlebnis bieten.

## Idee & Ziel
- **Gameplay:**  
  Dein Charakter läuft automatisch, während von rechts Hindernisse (z. B. Schnecken oder später andere Cyber-Elemente) ins Bild kommen. Deine Aufgabe ist es, diese rechtzeitig zu überspringen oder ihnen auszuweichen.
  
- **Verlieren:**  
  Sobald du von einem Hindernis getroffen wirst, ist das Spiel vorbei.
  
- **Thema & Design:**  
  Das gesamte Spiel soll einen futuristischen Cyberpunk-Look erhalten, inklusive neondurchfluteten Hintergründen und stylischen Charakteren.

## Aktueller Stand
- Hintergrund- und Bodengrafik sind implementiert.
- Ein einfaches Hindernis (Snail) bewegt sich von rechts nach links.
- Der Spielercharakter ist bereits sichtbar und auf dem Boden positioniert.
- Punkte-/Score-Anzeige ist vorbereitet (momentan nur ein Text).

## Nächste Schritte
- **Springen implementieren:**  
  Der Charakter soll auf Tastendruck springen können, um Hindernissen auszuweichen.
  
- **Mehr Hindernisse & Animationen:**  
  Weitere Hindernisarten hinzufügen, Animationen für den Spielercharakter einbauen.

- **Kollisionsabfrage:**  
  Treffen von Hindernissen soll das Spiel beenden (Game Over-Screen oder -Logic).

- **Score-System:**  
  Punktesystem für erfolgreich übersprungene Hindernisse oder zurückgelegte Distanz.

## Installation & Ausführung

1. **Python & Pygame installieren:**  
   Stelle sicher, dass Python 3.x installiert ist.  
   Installiere Pygame mit:
   ```bash
   pip install pygame

