## Flow Chart

```mermaid
flowchart TD
    Start --> Teile["Teile die Liste in zwei Hälften"]
    Teile --> LinkeHaelfte["Linke Hälfte"]
    Teile --> RechteHaelfte["Rechte Hälfte"]
    LinkeHaelfte --> SortiereLinks["Sortiere linke Hälfte rekursiv"]
    RechteHaelfte --> SortiereRechts["Sortiere rechte Hälfte rekursiv"]
    SortiereLinks --> Merge["Füge die sortierten Hälften zusammen"]
    SortiereRechts --> Merge
    Merge --> Ende["Sortierte Liste"]

