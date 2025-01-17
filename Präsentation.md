# Präsentation über MergeSort

**Präsentation von:** Yaser  
**Thema:** Mergesort Algorithmus  
**Dauer:** ca. 5 Minuten
![w:600px](Merge-Sort.png)
*[Quelle](https://fullyunderstood.com/pseudocodes/merge-sort/)*

---

### Was ist MergeSort?  

MergeSort ist ein Sortieralgorithmus, der Daten in aufsteigende Reihenfolge bringt.  
Er nutzt das Prinzip **„Teile und Erobere“**, indem er grosse Aufgaben in kleinere, einfacher lösbare Teile zerlegt und diese schrittweise sortiert.  

---

### Warum ist MergeSort wichtig?  
- MergeSort ist einer der effizientesten Sortieralgorithmen mit einer garantierten Laufzeit von **O(n log n)**.  
- Er ist **stabil**, wodurch gleiche Elemente in ihrer Reihenfolge bleiben.  
- Er ist ideal für grosse Datenmengen geeignet.  

### Einsatzmöglichkeiten:  
MergeSort wird oft bei grossen Datenmengen genutzt, z. B. beim Sortieren von **Datenbanken** oder in der **Big-Data-Analyse**.

---

#### Erklärung von MergeSort
Teilen (Divide): 
Zerlege die Liste in zwei kleinere Listen, bis jede Teil-Liste nur noch ein Element enthält.

Erobern (Conquer):
Sortiere jede kleine Liste. Da sie nur ein Element enthält, ist sie bereits sortiert.

Vereinen (Merge):
Füge die sortierten Teil-Listen wieder zusammen, um eine komplett sortierte Liste zu erhalten.

![w:250px](MergesortDeutsch.png)

---

#### Kurzes Beispiel Bild 1
![Unsortiert.png](Unsortiert.png)

---

#### Kurzes Beispiel Bild 2
![Sortiert.png](Sortiert.png)

---

##### Vorteile:
- Effiziente Laufzeit: O(n log n)  
- Stabiler Algorithmus (gleiche Elemente bleiben in Reihenfolge)  
- Gut für große Datenmengen geeignet

![w:750px](Mergesort%20komplex.png)

---

##### Nachteile:
- Braucht zusätzlichen Speicher für das Mergen  
- Etwas komplexer als einfache Sortiermethoden wie Bubble Sort

![w:750px](O%28n%29.png)

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

### Fazit

Merge Sort ist ein starker Algorithmus, besonders für grosse Daten.  
Ich habe dabei gelernt, wie "Teile und Erobere" funktioniert.  
Das Projekt hat mir gezeigt, wie wichtig klare und strukturierte Arbeit ist.

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