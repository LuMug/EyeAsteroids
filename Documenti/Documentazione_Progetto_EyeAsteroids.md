1. [Introduzione](#introduzione)

  - [Informazioni sul progetto](#informazioni-sul-progetto)

  - [Abstract](#abstract)

  - [Scopo](#scopo)

1. [Analisi](#analisi)

  - [Analisi del dominio](#analisi-del-dominio)

  - [Analisi dei mezzi](#analisi-dei-mezzi)

  - [Analisi e specifica dei requisiti](#analisi-e-specifica-dei-requisiti)

  - [Use case](#use-case)

  - [Pianificazione](#pianificazione)

1. [Progettazione](#progettazione)

  - [Design dell’architettura del sistema](#design-dell’architettura-del-sistema)

  - [Design dei dati e database](#design-dei-dati-e-database)

1. [Implementazione](#implementazione)

1. [Test](#test)

  - [Protocollo di test](#protocollo-di-test)

  - [Risultati test](#risultati-test)

  - [Mancanze/limitazioni conosciute](#mancanze/limitazioni-conosciute)

1. [Consuntivo](#consuntivo)

1. [Conclusioni](#conclusioni)

  - [Sviluppi futuri](#sviluppi-futuri)

  - [Considerazioni personali](#considerazioni-personali)

1. [Sitografia](#sitografia)

1. [Allegati](#allegati)


## Introduzione

### Informazioni sul progetto
- Allievi coinvolti nel progetto: Alessandro Aloise, Mattia Pasquini, Alessandro Castelli
- Classe: I3BB,I3AC Scuola Arti e Mestieri Trevano, sezione Informatica.
- Docenti responsabili: Luca Muggiasca.
- Data inizio: 27 gennario 2022
- Data di fine: 05 maggio 2022.

### Abstract

> *Everyone at least once has heard of the famous retro game Asteroids. Today more than ever we are returning to fashion retro games, it often happens to hear of new game rooms that are opened with the presence of cabinets. For this reason we want to give a touch of novelty to a game that has made history. For this reason we decided to create this version of the game where you will no longer have to move the ship with the classic knob but simply with the look. This version does not want to change anything in terms of graphics compared to the original in fact it will be as faithful as possible to the original.Our product will be a more technological and advanced version of the original videogame, but to keep the originality we decided to have a dedicated machine with a ranking like the real game on which you can play one at a time and try to improve your score.*

### Scopo

Lo scopo del progetto è di creare un videogame che riprenda l’iconico Asteroids, nel quale una navicella posta al centro dello schermo non deve farsi colpire dagli asteroidi che si avvicinano a lei. La navicella potrà solamente ruotare su se stessa. La particolarità di questa versione del gioco sarà che la navicella dovrà essere guidata con gli occhi dal giocatore.



## Analisi

### Analisi del dominio

  È stato richiesto di creare il videogame Asteroids che dovrà essere giocato tramite gli occhi. La navicella deve essere fissa al centro e poter sparare tramite lo sguardo del giocatore inoltre. Il videogame deve contere una classifica come il gioco origine. Deve inoltre essere presenti vari livelli di difficoltà, in fine devono essere presenti vari tipi di asteroidi.

  Deve essere inoltre allestita una macchina dedicata per il suo corretto funzionamento e in modo che più persone possano giocarci.


### Analisi e specifica dei requisiti
|              |**ID: Req-001**                       |
|--------------|--------------------------------------|
|**Nome**      |La navicella deve ruotare su se stessa|
|**Priorità**  | 1                                    |
|**Versione**  | 1.1                                  |
|**Note**      | Sempre al centro del frame           |

|              |**ID: Req-002**                           |
|--------------|------------------------------------------|
|**Nome**      |Poter saprare con lo sguardo sparo singolo|
|**Priorità**  | 1                                        |
|**Versione**  | 1.1                                      |
|**Note**      |                                          |

|              |**ID: Req-003**              |
|--------------|-----------------------------|
|**Nome**      |Poter sparare con la tastiera|
|**Priorità**  | 2                           |
|**Versione**  | 1.1                         |
|**Note**      | (extra)                     |

|              |**ID: Req-004**                           |
|--------------|------------------------------------------|
|**Nome**      |Diverse difficoltà in base al tempo.      |
|**Priorità**  | 1                                        |
|**Versione**  | 1.1                                      |
|**Note**      | Più il tempo passa più diventa difficile |

|              |**ID: Req-005**                      |
|--------------|-------------------------------------|
|**Nome**      |Essere fedele alla versione originale|
|**Priorità**  | 2                                   |
|**Versione**  | 1.1                                 |
|**Note**      | (extra)                             |

|              |**ID: Req-006**                             |
|--------------|--------------------------------------------|
|**Nome**      |Avere un database dove salvare la classifica|
|**Priorità**  | 2                                          |
|**Versione**  | 1.1                                        |
|**Note**      | Ci può essre più volte lo stesso nome      |

|              |**ID: Req-007**                    |
|--------------|-----------------------------------|
|**Nome**      |Generare gli asteroidi in movimento|
|**Priorità**  | 1                                 |
|**Versione**  | 1.1                               |
|**Note**      |  |

|              |**ID: Req-008** |
|--------------|----------------|
|**Nome**      |Punteggio       |
|**Priorità**  | 1              |
|**Versione**  | 1.1            |
|**Note**      |                |

|              |**ID: Req-009**  |
|--------------|-----------------|
|**Nome**      |Macchina dedicata|
|**Priorità**  | 1               |
|**Versione**  | 1.1             |
|**Note**      |                 |

|              |**ID: Req-010**            |
|--------------|---------------------------|
|**Nome**      |Asteroidi multipli         |
|**Priorità**  | 1                         |
|**Versione**  | 1.1                       |
|**Note**      | Più tipolgie di asteroidi |



### Use case

I casi d’uso rappresentano l’interazione tra i vari attori e le
funzionalità del prodotto.

### Pianificazione

Prima di stabilire una pianificazione bisogna avere almeno una vaga idea
del modello di sviluppo che si intende adottare. In questa sezione
bisognerà inserire il modello concettuale di sviluppo che si seguirà
durante il progetto. Gli elementi di riferimento per una buona
pianificazione derivano da una scomposizione top-down della problematica
del progetto.

La pianificazione può essere rappresentata mediante un diagramma di
Gantt.

Se si usano altri metodi di pianificazione (es scrum), dovranno apparire
in questo capitolo.

### Analisi dei mezzi

Elencare e *descrivere* i mezzi disponibili per la realizzazione del
progetto. Ricordarsi di sempre descrivere nel dettaglio le versioni e il
modello di riferimento.

SDK, librerie, tools utilizzati per la realizzazione del progetto e
eventuali dipendenze.

Su quale piattaforma dovrà essere eseguito il prodotto? Che hardware
particolare è coinvolto nel progetto? Che particolarità e limitazioni
presenta? Che hw sarà disponibile durante lo sviluppo?

## Progettazione

Questo capitolo descrive esaustivamente come deve essere realizzato il
prodotto fin nei suoi dettagli. Una buona progettazione permette
all’esecutore di evitare fraintendimenti e imprecisioni
nell’implementazione del prodotto.

### Design dell’architettura del sistema

Descrive:

-   La struttura del programma/sistema lo schema di rete...

-   Gli oggetti/moduli/componenti che lo compongono.

-   I flussi di informazione in ingresso ed in uscita e le
    relative elaborazioni. Può utilizzare *diagrammi di flusso dei
    dati* (DFD).

-   Eventuale sitemap

### Design dei dati e database

Descrizione delle strutture di dati utilizzate dal programma in base
agli attributi e le relazioni degli oggetti in uso.

### Schema E-R, schema logico e descrizione.

Se il diagramma E-R viene modificato, sulla doc dovrà apparire l’ultima
versione, mentre le vecchie saranno sui diari.

### Design delle interfacce

Descrizione delle interfacce interne ed esterne del sistema e
dell’interfaccia utente. La progettazione delle interfacce è basata
sulle informazioni ricavate durante la fase di analisi e realizzata
tramite mockups.

### Design procedurale

Descrive i concetti dettagliati dell’architettura/sviluppo utilizzando
ad esempio:

-   Diagrammi di flusso e Nassi.

-   Tabelle.

-   Classi e metodi.

-   Tabelle di routing

-   Diritti di accesso a condivisioni …

Questi documenti permetteranno di rappresentare i dettagli procedurali
per la realizzazione del prodotto.

## Implementazione

In questo capitolo dovrà essere mostrato come è stato realizzato il
lavoro. Questa parte può differenziarsi dalla progettazione in quanto il
risultato ottenuto non per forza può essere come era stato progettato.

Sulla base di queste informazioni il lavoro svolto dovrà essere
riproducibile.

In questa parte è richiesto l’inserimento di codice sorgente/print
screen di maschere solamente per quei passaggi particolarmente
significativi e/o critici.

Inoltre dovranno essere descritte eventuali varianti di soluzione o
scelte di prodotti con motivazione delle scelte.

Non deve apparire nessuna forma di guida d’uso di librerie o di
componenti utilizzati. Eventualmente questa va allegata.

Per eventuali dettagli si possono inserire riferimenti ai diari.

## Test

### Protocollo di test

Definire in modo accurato tutti i test che devono essere realizzati per
garantire l’adempimento delle richieste formulate nei requisiti. I test
fungono da garanzia di qualità del prodotto. Ogni test deve essere
ripetibile alle stesse condizioni.


|Test Case      | TC-001                               |
|---------------|--------------------------------------|
|**Nome**       |Import a card, but not shown with the GUI |
|**Riferimento**|REQ-012                               |
|**Descrizione**|Import a card with KIC, KID and KIK keys with no obfuscation, but not shown with the GUI |
|**Prerequisiti**|Store on local PC: Profile\_1.2.001.xml (appendix n\_n) and Cards\_1.2.001.txt (appendix n\_n) |
|**Procedura**     | - Go to “Cards manager” menu, in main page click “Import Profiles” link, Select the “1.2.001.xml” file, Import the Profile - Go to “Cards manager” menu, in main page click “Import Cards” link, Select the “1.2.001.txt” file, Delete the cards, Select the “1.2.001.txt” file, Import the cards |
|**Risultati attesi** |Keys visible in the DB (OtaCardKey) but not visible in the GUI (Card details) |


### Risultati test

Tabella riassuntiva in cui si inseriscono i test riusciti e non del
prodotto finale. Se un test non riesce e viene corretto l’errore, questo
dovrà risultare nel documento finale come riuscito (la procedura della
correzione apparirà nel diario), altrimenti dovrà essere descritto
l’errore con eventuali ipotesi di correzione.

### Mancanze/limitazioni conosciute

Descrizione con motivazione di eventuali elementi mancanti o non
completamente implementati, al di fuori dei test case. Non devono essere
riportati gli errori e i problemi riscontrati e poi risolti durante il
progetto.

## Consuntivo

Consuntivo del tempo di lavoro effettivo e considerazioni riguardo le
differenze rispetto alla pianificazione (cap 1.7) (ad esempio Gannt
consuntivo).

## Conclusioni

Quali sono le implicazioni della mia soluzione? Che impatto avrà?
Cambierà il mondo? È un successo importante? È solo un’aggiunta
marginale o è semplicemente servita per scoprire che questo percorso è
stato una perdita di tempo? I risultati ottenuti sono generali,
facilmente generalizzabili o sono specifici di un caso particolare? ecc

### Sviluppi futuri
  Migliorie o estensioni che possono essere sviluppate sul prodotto.

### Considerazioni personali
  Cosa ho imparato in questo progetto? ecc

## Bibliografia

### Bibliografia per articoli di riviste
1.  Cognome e nome (o iniziali) dell’autore o degli autori, o nome
    dell’organizzazione,

2.  Titolo dell’articolo (tra virgolette),

3.  Titolo della rivista (in italico),

4.  Anno e numero

5.  Pagina iniziale dell’articolo,

### Bibliografia per libri


1.  Cognome e nome (o iniziali) dell’autore o degli autori, o nome
    dell’organizzazione,

2.  Titolo del libro (in italico),

3.  ev. Numero di edizione,

4.  Nome dell’editore,

5.  Anno di pubblicazione,

6.  ISBN.

### Sitografia

1.  URL del sito (se troppo lungo solo dominio, evt completo nel
    diario),

2.  Eventuale titolo della pagina (in italico),

3.  Data di consultazione (GG-MM-AAAA).

**Esempio:**

-   http://standards.ieee.org/guides/style/section7.html, *IEEE
    Standards Style Manual*, 07-06-2008.

## Allegati

Elenco degli allegati, esempio:

-   Diari di lavoro

-   Codici sorgente/documentazione macchine virtuali

-   Istruzioni di installazione del prodotto (con credenziali
    di accesso) e/o di eventuali prodotti terzi

-   Documentazione di prodotti di terzi

-   Eventuali guide utente / Manuali di utilizzo

-   Mandato e/o Qdc

-   Prodotto

-   …
