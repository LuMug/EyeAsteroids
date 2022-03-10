# EyeAsteroids | Diario di lavoro
##### Alessandro Aloise, Mattia Pasquini, Alessandro Castelli
### Centro Professionale Trevano, 24.02.2022

## Lavori svolti


|Orario        |Lavoro svolto                                               	  |Eseguito da        |
|--------------|----------------------------------------------------------------- |-------------------|
|09:05 - 09:15 | Spiegare ad Aloise cosa è stato fatto settimana scorsa  		      |Castelli e Pasquini|
|09:15 - 16.30 | Lavoro con libreria per tracciare gli occhi				  	          |Aloise             |
|09:15 - 12.20 | Generazione asteroidi continuo								  	                |Castelli           |
|09:15 - 10:50 | Implementato classe Laser									                      |Pasquini           |
|10:50 - 11:35 | Stampa laser dalla coordinata del mouse		    	  	 	          |Pasquini           |
|11:35 - 12:20 | Collisione tra laser e asteroidi 							                  |Pasquini           |
|13:15 - 14:45 | Generazione asteroidi continuo all'esterno dell'interfaccia      |Castelli           |
|13:15 - 14:00 | Navicella ruotabile in funzione delle coordinate del mouse       |Pasquini           |   
|14:00 - 15:15 | Implementare la durata della vita degli asteroidi con laser      |Pasquini           |  
|15:00 - 15:30 | Punteggio                                                        |Castelli           |  
|15:30 - 16:00 | Risoluzione dei problemi di github                               |Castelli e Pasquini|
|16:00 - 16:30 | Diario                                                           |Castelli e Pasquini|    


##  Problemi riscontrati e soluzioni adottate
I problemi riscontrati durante questa giornata:

* La durata degli asteroidi non è ottimale, è poco preciso. Bisogna creare un nuovo attributo nella classe Asteroid.
* Come scritto nei lavori svolti, abbiamo avuto problemi con GitHub, non riusciva ad eseguire il comando `git push` perchè c'è stato un problema con merge. Risolto copiando un file rinominandolo in `startgame.pyBKP` e poi eseguito il `commit` e `push`. E poi rinominato in `startgame.py`.
* Non riuscivamo ad eseguire la demo del GazeTracking
* Per quanto riguarda la libreria degli occhi ci siamo accorti che ci forniva solo le cordine della pupilla e non il punto dove si sta guardando. Per sistemare questo problema abbiamo dovuto usare il radio e le percentuali ma ci siamo accorti che per quanto riguarda la precisione verticale é molto scarsa perché ha pochi punti per fare le proprozioni.
``` py
  x = (gaze.horizontal_ratio())*width
  y =(gaze.vertical_ratio())*height
```

##  Punto della situazione rispetto alla pianificazione
Leggermente avanti rispetto alla programmazione

## Programma di massima per la prossima giornata di lavoro
Ottimizzare la durata della vita degli asteroidi
