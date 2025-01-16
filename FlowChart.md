## Flow Chart


```mermaid
graph TD
    Start((Start))
    Teile[Teile die Liste in zwei Hälften]
    LinkeHaelfte[Sortiere die linke Hälfte rekursiv]
    RechteHaelfte[Sortiere die rechte Hälfte rekursiv]
    Merge[Füge die sortierten Hälften zusammen]
    Ende((Sortierte Liste zurückgeben))
    
    Start --> Teile
    Teile --> LinkeHaelfte
    LinkeHaelfte --> RechteHaelfte
    RechteHaelfte --> Merge
    Merge --> Ende


