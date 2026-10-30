---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Zeitreihen"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Heteroskedastizität


## Kurzdefinition

- Strukturelle Heteroskedastizität liegt vor, wenn die Renditevarianz nicht vom Preisniveau abhängt, ein ADF auf Rohpreisen aber eine davon unabhängige, endliche Preisvarianz unterstellt.
- Heteroskedastizität von Intraday-Zeitbars entsteht aus der ungleichmäßigen Natur von Tickdaten.

## Kernaussagen

- Wird die Null des ADF auf Rohpreisen verworfen, gelten die Preise als stationär mit endlicher Varianz.
- Damit die Preisvarianz konstant bleibt, muss die Renditevolatilität bei steigenden Preisen fallen und bei fallenden Preisen steigen.
- Ein ADF auf Rohpreisen nimmt damit an, dass die Renditevarianz nicht invariant zum Preisniveau ist.
- Ist die Renditevarianz tatsächlich invariant zum Preisniveau, ist das Modell auf Rohpreisen strukturell heteroskedastisch.
- Bei Logpreisen bedingen die Preisniveaus den Mittelwert der Renditen, nicht ihre Volatilität.
- Wenn der Renditebetrag viele Ausgänge annehmen kann, verwirft Binärcodierung Information, besonders bei Intraday-Zeitbars.
- Ein teilweiser Ausgleich ist die Abtastung nach einem subordinierten stochastischen Prozess.
- Trade Bars und Volume Bars enthalten eine feste Zahl von Trades oder Trades für ein festes Volumen.
- In dieser marktgesteuerten, nicht chronologischen Uhr wird in aktiven Phasen häufiger und in ruhigen Phasen seltener gesampelt.
- Diese Abtastung regularisiert die Verteilung des Renditebetrags und senkt den Bedarf an einem großen Alphabet.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Für Strukturbruchtests auf langen Reihen mit Blasen und Einbrüchen sind Logpreise den Rohpreisen vorzuziehen.
- Der Unterschied fällt bei kleinen Stichproben mit einem Niveau-Faktor nahe 1 oft kaum ins Gewicht, SADF regressiert aber über Jahrzehnte, und Blasen erzeugen zwischen Regimes deutlich verschiedene Niveaus.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Advances in Financial Machine Learning.pdf, S. 286–305 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-016-p286-p305|S. 286–305]]

## Verwandte Themen
