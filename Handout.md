# Handout: MergeSort

## Definition
MergeSort ist ein effizienter Sortieralgorithmus, der das Prinzip "Teile und Herrsche" (Divide and Conquer) verwendet. Er zerlegt eine Liste rekursiv in kleinere Teile, sortiert diese und führt sie anschließend wieder zusammen.

---

## Funktionsweise
1. **Teilen (Divide):**  
   - Die Liste wird in zwei Hälften geteilt, bis jede Teil-Liste nur noch ein Element enthält.
   
2. **Sortieren (Conquer):**  
   - Jede Teilliste wird rekursiv sortiert.
   
3. **Zusammenführen (Merge):**  
   - Die sortierten Teillisten werden miteinander verschmolzen, sodass eine vollständig sortierte Liste entsteht.

**Beispiel:**
Unsortierte Liste: [8, 3, 5, 1]  
1. Teilen: [8, 3] und [5, 1]  
2. Sortieren: [3, 8] und [1, 5]  
3. Mergen: [1, 3, 5, 8]

---

## Vorteile
- Sehr effizient bei großen Datensätzen mit einer Laufzeit von \( O(n \log n) \).
- Funktioniert unabhängig davon, ob die Liste unsortiert oder teilweise sortiert ist.
- Stabiler Algorithmus: Gleiche Werte behalten ihre ursprüngliche Reihenfolge.

---

## Nachteile
- Benötigt zusätzlichen Speicherplatz für die Teillisten.
- Kann bei kleinen Datensätzen weniger effizient sein als einfache Algorithmen.

---

## Vergleich mit anderen Algorithmen
- **BubbleSort / InsertionSort:**  
  - Laufzeit von \( O(n^2) \), daher langsamer bei grossen Listen.  
- **QuickSort:**  
  - Meist ähnlich effizient wie MergeSort, aber nicht stabil.

---

## Fazit
MergeSort ist ein leistungsstarker Algorithmus, der sich besonders für grosse Datenmengen eignet. Obwohl er zusätzlichen Speicher benötigt, ist er eine ausgezeichnete Wahl, wenn Stabilität und Effizienz wichtig sind.

---

## Quellen
1. MergeSort Algorithmus – Wikipedia: [https://de.wikipedia.org/wiki/MergeSort](https://de.wikipedia.org/wiki/MergeSort)
