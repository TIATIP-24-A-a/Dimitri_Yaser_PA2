# Projektarbeit: MergeSort Yaser Dimitri

## Übersicht
Dieses File dient als Dokumentation unserer Arbeit.
In diesem Projekt beschäftigen wir uns mit dem MergeSort-Algorithmus, einem effizienten, rekursiven Sortierverfahren. Ziel ist es, eine Liste von Elementen (typischerweise Zahlen) in aufsteigender Reihenfolge zu sortieren. MergeSort hat eine durchschnittliche und auch worst-case Laufzeit von O(n log n) und ist damit deutlich schneller als einfache Sortierverfahren wie der Insertion- oder Selection-Sort für große Datenmengen.

**Kernpunkte unseres Projekts:**
- Implementierung des MergeSort-Algorithmus in Python
- Nutzung rekursiver Teilung der Liste
- Zusammenführen (Merge) der Teillisten in sortierter Reihenfolge
- Einfache Tests, um die Korrektheit zu überprüfen

## Projektbeschreibung

### Hintergrund

MergeSort ist ein auf "Teile und Herrsche" (Divide and Conquer) basierender Sortieralgorithmus. Der Algorithmus teilt die Liste wiederholt in zwei Hälften, sortiert diese Hälften rekursiv und führt sie anschließend sortiert zusammen.

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
