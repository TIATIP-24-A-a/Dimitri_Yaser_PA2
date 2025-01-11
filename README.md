# Projektarbeit: MergeSort Yaser

## Übersicht 
Dieses File dient als Dokumentation unserer Arbeit.
In diesem Projekt beschäftigen wir uns mit dem MergeSort-Algorithmus, einem effizienten, rekursiven Sortierverfahren. Ziel ist es, eine Liste von Elementen (typischerweise Zahlen) in aufsteigender Reihenfolge zu sortieren. MergeSort hat eine durchschnittliche und auch worst-case Laufzeit von O(n log n) und ist damit deutlich schneller als einfache Sortierverfahren wie der Insertion- oder Selection-Sort für große Datenmengen.

**Kernpunkte unseres Projekts:**
- Implementierung des MergeSort-Algorithmus in Python
- Nutzung rekursiver Teilung der Liste
- Zusammenführen (Merge) der Teillisten in sortierter Reihenfolge
- Einfache Tests, um die Korrektheit zu überprüfen

## Recherche
- Merge, rebase, or cherry-pick to apply changes
- quelle: https://www.jetbrains.com/help/pycharm/apply-changes-from-one-branch-to-another.html

## Projektbeschreibung

### Hintergrund

MergeSort ist ein auf "Teile und Herrsche" (Divide and Conquer) basierender Sortieralgorithmus. Der Algorithmus teilt die Liste wiederholt in zwei Hälften, sortiert diese Hälften rekursiv und führt sie anschließend sortiert zusammen.

### Testing
- Wir haben mit Hilfe mehrerer Tests unsern Algorithms auf seine Funktionalität geprüft.
- Alle Tests wurden erfolgreich absolviert


**Wesentliche Schritte von MergeSort:**

1. **Teilen (Divide)**:  
   Ist die Liste länger als ein Element, wird sie in zwei ungefähr gleich große Hälften geteilt.
   
2. **Rekursiv sortieren (Conquer)**:  
   Die beiden Hälften werden mittels MergeSort jeweils einzeln sortiert.
   
3. **Zusammenführen (Combine/Merge)**:  
   Die beiden bereits sortierten Teillisten werden in einer Merge-Operation elementweise verglichen und in aufsteigender Reihenfolge zu einer finalen, sortierten Liste zusammengefügt.

### Anforderungen

- Eingabe: Eine unsortierte Liste von Elementen (typischerweise Zahlen: int oder float).
- Ausgabe: Eine sortierte Liste in aufsteigender Reihenfolge.

## Protokoll 

### 23.12.2024
- Recherche zum MergeSort-Algorithmus vertieft: Fokus auf "Teile und Herrsche"-Ansatz.
- Erstellen eines neuen GitHub-Repositories für das Projekt.
- Python-Skript erstellt, um eine erste Basis für den MergeSort-Algorithmus zu legen.
- Funktion implementiert, die eine Liste in zwei Hälften teilt.
### 27.12.2024
- Algorithmus zur Rekursion hinzugefügt: MergeSort kann nun Teillisten sortieren.
- Funktionalität zum Zusammenführen (Merge) der sortierten Teillisten programmiert.
- Erste Tests mit kleinen Integer-Listen erfolgreich durchgeführt.
- Dokumentation begonnen: Beschreibung des Algorithmus und seiner Funktionsweise.
### 30.12.2024
- Tests erweitert: Zusätzliche Tests mit Floating-Point-Zahlen und Strings durchgeführt.
- Fehlersuche und Debugging: Kleinere Fehler in der Merge-Funktion behoben.
- Laufzeit des Algorithmus mit Listen unterschiedlicher Größen analysiert.
### 03.01.2025
- Markdown-Dokumentation aktualisiert: Algorithmus, Tests und Ergebnisse dokumentiert.
- Diagramme zur Visualisierung des Algorithmus mit Mermaid erstellt.
- Ergebnisse und Fortschritte auf GitHub hochgeladen. 
### 07.01.2025
- Weitere Tests durchgeführt: Algorithmus auf Sonderfälle wie leere Listen und Listen mit einem Element getestet.
- Präsentation vorbereitet: Folien erstellt und Struktur festgelegt.
- MergeSort-Dokumentation finalisiert und auf GitHub aktualisiert.

### Fazit
MergeSort war ein spannender Algorithmus, den wir programmieren und besser verstehen konnten. Wir haben gelernt, wie "Teile und Herrsche" funktioniert und warum MergeSort bei grossen Datenmengen effizient ist.

Die Arbeit im Team hat uns geholfen, uns gegenseitig zu unterstützen und die Aufgaben zu teilen. Insgesamt war das Projekt eine gute Erfahrung, bei der wir nicht nur Programmieren, sondern auch Teamarbeit und das Dokumentieren von Ergebnissen geübt haben.



