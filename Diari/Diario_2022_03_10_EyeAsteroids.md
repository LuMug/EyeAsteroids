# EyeAsteroids | Diario di lavoro
##### Alessandro Aloise, Mattia Pasquini, Alessandro Castelli
### Centro Professionale Trevano, 10.03.2022

## Lavori svolti


|Orario        |Lavoro svolto                                               	  |Eseguito da                   |
|--------------|----------------------------------------------------------------- |----------------------------|
|09:05 - 09:15 | Riunione organizzativa del team                        		       |Castelli e Pasquini e Aloise|
|09:15 - 12.20 | Lavoro con libreria per tracciare gli occhi				  	           |Aloise                      |
|09:15 - 10:30 | Ottimizzare il calcolo della perdita della vita dal laser         |Pasquini                    |
|09:15 - 12:20 | Ottimizzare spawn asteroidi direzionandoli verso il centro        |Castelli                    |
|13:15 - 13.40 | Creazione database sql lite                				  	           |Aloise                      |
|13:40 - 14:00 | Comandi per inserire e mostrare i dati per il gioco  	           |Pasquini                    |
|14:00 - 16:15 | Possibilità di inserire nome in game over e mostrare la classifica|Pasquini                    |
|13:40 - 16.20 | Libreria occhi direzione                   				  	           |Aloise e Castelli           |



##  Problemi riscontrati e soluzioni adottate
I problemi riscontrati durante questa giornata:

* Per quanto riguarda la libreria per tracckare gli occhi come nell'ultima giornata di lavoro abbiamo avuto problemi perché il ratio dovrebbe andare da 0 punto più a sisnistra dello schermo a 1 punto più a destra dello schermo. Ma quando andiamo a stampare sulla console il nostro ratio x e y abbiamo notato che non scende mai sotto i 0,5 ma che invece supera i 1 anche di molto fino a arrivare circa a 1,3 /1,4. Dopo tutto il giorno passato a fare test e tentativi, che sono stati: cambiare la webcam per avere una risoluzione più alta e di conseguenza una precisione più alta, spostare la webcam al posto che in alto in basso o al centro. Tutti questi tentativi hanno sempre portato lo stesso risultato per quanto riguarda il range di ratio. Dopo tutti questi tentativi abbiamo provato a togliere andando un -10 ché é presente direttamente nei file originali di calcolo e facendo questa modifica il ratio finalmente scendeva sotto lo 0,5 mano non arrivava più a 1 ma si fermava intorno al 0,7. Dopo tutte queste problematica e dopo aver chiesto consiglio sia al docente Muggiasca che Petrini ci é stato consigliato di scrivere un email direttamente al creatore della libreria. 
* Su pygame non esiste alcun textbox per inserire il nome del giocatore dopo aver finito la partita, ho dovuto far in modo che ascolta la tastiera durante game over, poi viene memorizzato in una variabile e poi si mette il nome che ha scritto con il punteggio nel database. Così da mostrare la classifica dei punteggi.

##  Punto della situazione rispetto alla pianificazione
Leggermente avanti rispetto alla programmazione

## Programma di massima per la prossima giornata di lavoro
Sistemare il problema con il ratio e fare la documentazione
