# Präsentation über MergeSort

**Präsentation von:** Yaser  
**Thema:** Mergesort Algorithmus  
**Dauer:** ca. 5 Minuten
![w:600px](Merge-Sort.png)
*[Quelle](https://fullyunderstood.com/pseudocodes/merge-sort/)*

---
## Was ist MergeSort?
Merge Sort ist ein **Sortieralgorithmus**, der auf dem Prinzip **Teile und Erobere** (Divide and Conquer) basiert. 
  1. **Teilen (Divide):** Zerlege die Liste in zwei kleinere Listen, bis jede Teil-Liste nur noch ein Element hat.  
  2. **Erobern (Conquer):** Sortiere diese kleinen Listen (einzelne Elemente sind schon sortiert).  
  3. **Vereinen (Merge):** Füge die sortierten Teil-Listen wieder zusammen, dabei entsteht eine komplett sortierte Liste.
![w:300px](fotogroesse-powerpoint-titel.png)
*[Quelle](ttps://www.npridik.de/scharfe-bilder-powerpoint/)*
---

## Warum dieses Vorgehen?

- **Vorteile:**  
  - Effiziente Laufzeit: O(n log n)  
  - Stabiler Algorithmus (gleiche Elemente bleiben in Reihenfolge)  
  - Gut für große Datenmengen geeignet
- **Nachteile:**  
  - Braucht zusätzlichen Speicher für das Mergen  
  - Etwas komplexer als einfache Sortiermethoden wie Bubble Sort
![w:350px](mit_systemischem_vorgehen_souveraen_entscheiden_h.jpg)
*[Quelle](https://www.projektmagazin.de/artikel/mit-systemischem-vorgehen-souveraen-entscheiden_1098373)*
---
#### Kurzes Beispiel
| ![Bild 1](MergesortDeutsch.png) | ![Bild 2](img_mergesort_long.png)    |
|---------------------------------|--------------------------------------|
*[Quelle](https://de.wikipedia.org/wiki/Mergesort)*

---

### Coding Test Unit Test
- ich habe den Code in **PyCharm** geschrieben getestet und mit **Git** versioniert. Jede Änderung ist ein eigener Commit.

```Python
import unittest

from mergesort import mergesort


class MyTestCase(unittest.TestCase):
    def test_sorting(self):
        a = [99, 88, 77, 33, 11]  # Arrange
        result = mergesort(a)  # Act
        self.assertEqual([11,33,77,88,99], result)  # Assert
```
---

## Fazit

<span style="font-size: 14px;">Merge Sort ist ein leistungsstarker Algorithmus, der besonders gut für grosse Datenmengen geeignet ist. Durch dieses Projekt habe ich gelernt, wie der Algorithmus funktioniert und warum das "Teile-und-Erobere"-Prinzip so effektiv ist. Außerdem hat es mir geholfen, meine Fähigkeit zur strukturierten und organisierten Arbeit zu verbessern.</span>

---

## Quellen
- [Introduction to Algorithms (CLRS)](https://mitpress.mit.edu/books/introduction-algorithms)  
- [Python Dokumentation](https://docs.python.org)  
- [pytest Dokumentation](https://docs.pytest.org/)
- [Wikipedia](https://de.wikipedia.org/wiki/Mergesort)
---

## Danke fürs Zuhören!

### Falls ihr Fragen habt, beantworte ich diese gerne.

![240_F_1152303874_kQKC0WtyYvJD3rMIBxa7rqiQlrbOQJ7b.jpg](240_F_1152303874_kQKC0WtyYvJD3rMIBxa7rqiQlrbOQJ7b.jpg)
*[Quelle](https://stock.adobe.com/de/search?k=thumbs+up+emoji)*