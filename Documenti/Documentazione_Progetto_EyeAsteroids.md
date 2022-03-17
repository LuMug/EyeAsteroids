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
Ecco il nostro Use Case:
![Use case](Progettazione/UseCase.PNG)
> Use case


### Pianificazione

Per la pianificazione alleghiamo il Gantt preventivo da noi stabilito:
![Ganttpreventivo](../Documenti/Gantt/Gantt_Preventivo_Completo.png)
> Gantt preventivo

Come si può notare abbiamo deciso di dediare molto tempo a come sparare con gli occhi dato che é una cosa che non abbiamo mai fatto abbiamo ritenuto opportuno dare questa quantità di tempo.
### Analisi dei mezzi

**Software**
- Python
- GazeTracking
- Pygame

**Hardware**
- Laptop personali
- PC scolastici
- PC dato dai sistemisti
- Webcam

## Progettazione
### Design dei dati e database
La prima versione del databse conteneva due tabelle una player e una score ma in fase di implementazione ci siamo accorti che era davvero inutile avere due tabelle quindi abbiamo deciso di tenerne solo una e di fargli qualche modifica :
![Databae](Progettazione/Database/database.PNG)
> Database

In questa Tabella viene salvati tutti i dati della partita, i dati più imprtanti sono il nome e lo score. Abbiamo deciso di slavare anche la data per eventuali sviluppi futuri.


### Design delle interfacce

### Schermata Home
La prima interfaccia che abbiamo definito è stata quella generale, ovvero l'interfaccia che l'utente avrebbe visto una volta avviato il gioco:
![Progettazione](Progettazione/Interfaccie/home.PNG)
> Schermata home

Siamo andatia vedere la schermata di partenza classica del gioco e l'abbiamo leggermente rivisitata abbiamo deciso di mettere la classifica nella home e di avere due tasti uno per giocare e l'altro per avere semplicemtne le informazioni

### Schermata Info
![Progettazione](Progettazione/Interfaccie/info.PNG)
> Schermata info

Abbiamo pensato a una schermata molto minimalista cercando di tenere lo stesso stile usato nell'resto del gioco, premendo il tasto exit si tornerà alla pagina home


### Schermata di gioco
![Progettazione](Progettazione/Interfaccie/game.PNG)
> Schermata di gioco

Su questo design non c'é molto da dire abbiamo cercato di rispettare il gioco originale.

### Schermata Classifica
![Progettazione](Progettazione/Interfaccie/gameOver.PNG)
> Schermata dove inserire il nome per la classifica

Abbiamo pensato a una schermata molto pulita e intuitiva per quanto riguarda la classifica. Come si può vedere c'é solo un label dove inserire il nome con sotto il proprio punteggio.

![Progettazione](Progettazione/Interfaccie/gameOver2.PNG)
> Schermata game over

Una volta inserito il nome verremo portati a questa schermata dove l'unica cosa che potremmo fare sarà premere il tasto enter per rigiocare oppure chiudere il gioco.


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

### Classe GameObject

Questa classe rappresenta gli oggetti presenti nel gioco in modo generico, che verrà ereditato dagli altri oggetti nel gioco.

Questa classe necessita la posizione con le coordinate, lo sprite per definire l'immagine, il raggio ottenendo la metà larghezza dell'immagine e infine la velocità.

La posizione dell'oggetto non viene definito le coordinate in alto e sinistra dell'immagine come default, ma viene definito le coordinate nel centro dell'immagine per semplificare eventuali rotazioni e collisioni tra gli oggetti che sono a forma del cerchio (per esempio asteroide) che viene implementato manualmente invece dei rettangoli siccome che nella libreria pygame non c'è.

In questa classe ci sono tre metodi:
- `draw(self, surface)`: serve per stampare l'oggetto calcolando la posizione dell'oggetto sottrando il raggio;
- `move(self)`: Aggiorna la posizione dell'oggetto sommando il valore della velocità;
- `collides_with(self, other_obj)`: calcola la collisione tra gli oggetti, calcolando se la distanza tra loro è più piccolo della somma dei raggi di entrambi oggetti.

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


### Sitografia

- https://stackoverflow.com/, *StackOverFlow*, 17.03.2022;
- https://github.com/antoinelame/GazeTracking, *GazeTracking*, 17.03.2022;
- https://www.codingcreativo.it/pygame/, *Pygame*, 24.02.2022;
- https://docs.python.org/3/library/sqlite3.html, *sqlite*, 24.02.2022;
- https://www.sqlitetutorial.net/sqlite-python/, *sqlite*, 24.02.2022;
- https://www.tutorialspoint.com/sqlite/, *sqlite*, 24.02.2022;
- https://www.sqlite.org/datatype3.html, *sqlite*, 24.02.2022;
- https://www.geeksforgeeks.org/python-sqlite-create-table/, *sqlite*, 24.02.2022;
- https://linuxhint.com/create-table-in-sqlite-using-if-not-exists-statement/, *sqlite*, 24.02.2022;
- https://www.pygame.org/docs/ref/rect.html?highlight=collide#pygame.Rect.clipline, *Pygame*, 24.02.2022;
- https://onlinepngtools.com/resize-png, *Modifica gradezza immagini*, 24.02.2022;
- https://www.w3schools.com/python/python_try_except.asp, *Pygame*, 24.02.2022;
- https://www.w3schools.com/python/ref_random_randrange.asp, *Pygame*, 24.02.2022;
- https://stackoverflow.com/questions/36653519/how-do-i-get-the-size-width-x-height-of-my-pygame-.window#:~:text=You%20can%20get%20the%20windows,get_height()%20on%20the%20surface, *Pygame*, 17.02.2022;
- https://app.diagrams.net/ , *Diagrammi*, 17.03.2022;

## Allegati

Elenco degli allegati:

-   Files di progettazione
-   Gantt preventivo
-   Gantt consuntivo
-   Diari di lavoro
-   Codice sorgente
-   Qdc
