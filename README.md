# Prüfungsverteilungprogramm für Prüfungen bei der IHK

Das Szenario für das das Programm gemacht worden ist:

Es sind 2 Prüfungstage bestimmt worden. Nicht alle Korrektoren sind an beiden Prüfungstagen anwesend.
Diese Daten wurden beim Ermitteln der Prüfungstage im Prüfungsausschuss abgestimmt und fix gesetzt.

Es geht nun darum die Prüfungsteilnehmer auf die 2 Tage optimal zu verteilen und der IHK einen Einladungsplan und eine Verteilrichtlinie als PDF zu erstellen.

- Es geht davon aus, dass die Korrektoren sowohl die Klausuren als auch die Dokumentationen eines bestimmten Prüflings korrigieren.
- Es müssen immer mindestens 3 Korrektoren zur Prüfung anwesend sein.
- Es müssen immer 2 Korrektoren eine Klausur/Dokumentation korrigiert haben.
- Es muss immer mindestens ein aktiver (Korrektor dieser Klausur/Dokumentation) Korrektor am Prüfungstag anwesend sein.

Es müssen zu jedem Prüfungstag die Prüfungsteilnehmer so aufgeteilt werden,
dass obige Bedingungen so erfüllt werden, dass die Korrektoren ungefähr eine ähnliche Anzahl Arbeiten korrigieren.


## Erforderliche Eingabedaten

### Korrektorenliste in utf8 (z.B. korrektorenliste.txt):
```
Korrektor1
Korrektor2
Korrektor3
Korrektor4
```

### Prüflingsliste in utf8 (z.B. prueflinge.txt):
```
Achenbach, Felix (1000001)
Bergmann, Lina (1000002)
Caspers, Jonas (1000003)
Dreher, Miriam (1000004)
Elsen, Paul (1000005)
Fritsch, Hannah (1000006)
Gärtner, Leo (1000007)
Hübner, Sophie (1000008)
Iversen, Max (1000009)
Jakobsen, Lara (1000010)
Kleinert, Tim (1000011)
Lindholm, Marie (1000012)
Mertens, Elias (1000013)
Neumann, Jana (1000014)
Ott, Fabian (1000015)
Pohl, Amelie (1000016)
```

Die Prüfungsliste kann auch als Datei direkt auf das mittlere Feld der Prüflinge per Drag-And-Drop gezogen werden.
Die Korrektoreniste muss allerdings über das Menü eingelesen werden.

### Einlesen / Abspeichern
Unter dem Menü Datei kann man jeweils diese Daten einlesen.
Mit Datei/Session speichern/einlesen kann die aktuelle Konfiguration abspeichern (nicht die kompletten korrektorenliste, sondern nur die verwendeten Korrektoren)

### Einstellungen
Im Einstellungsmenü kann man für die beiden Tage (im Moment geht das nur für beide Tage gleichzeitig) die Prüfungszeiten und Prüfungsdauer einstellen.
Die Mittagspause wird dann automatisch berechnet und angezeigt.

Nach der Einstellung muß die Aufteilung im Hauptdialog erneut erfolgen.


