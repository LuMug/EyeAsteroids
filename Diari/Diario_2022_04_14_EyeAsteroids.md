# EyeAsteroids | Diario di lavoro
##### Alessandro Aloise, Mattia Pasquini, Alessandro Castelli
### Centro Professionale Trevano, 14.04.2022

## Lavori svolti


|Orario        |Lavoro svolto                                               	    |Eseguito da        |
|--------------|----------------------------------------------------------------- |-------------------|
|09:05 - 09:20 | Riunione 		  												                          |Aloise, Castelli e Pasquini|
|09:20 - 11:35 | Impostare la scelta dell'uso del mouse o webcam				          |Pasquini e Aloise|
|11:35 - 16:15 | Documentazione e pulizia del codice e ottimizzazione		 	        |Pasquini e Castelli|
|11:35 - 16:15 | Ricerca libreria											 	                          |Pasquini e Castelli|
|16:15 - 16.30 | Diario				   						  					                          |Pasquini|


##  Problemi riscontrati e soluzioni adottate
I problemi riscontrati durante questa giornata:

* Pc fornito dalla scuola molto lento
* Dava degli errori nel codice, perché non era gestito bene le coordinate.
Nel ciclo for each nel metodo `_draw_game()`, mancava il parametro `coordinate` nel metodo `draw()` perchè il metodo `_get_game_objects()` ritorna sia gli asteroidi che navicella ma il metodo `draw()` di navicella possiede anche il parametro coordinata mentre gli asteroidi no.
```py

for game_object in self._get_game_objects():
    game_object.draw(self.screen)

```
quindi abbiamo risolto creando l'attributo `coordinates`, ecco il codice seguente:

```py
for asteroid in self.asteroids:
    asteroid.draw(self.screen)

self.spaceship.draw(self.screen, self.coordinates)
```
L'attributo `coordinates` è un modo comodo per gestire le coordinate del mouse oppure webcam a dipendenza dell'attributo `status_webcam`.
L'attributo `status_webcam` è utile per assegnare se si vuole utiizzare webcam oppure mouse, è un attributo booleana. Valore `True` se si vuole utilizzare webcam altrimenti è `False` se si vuole usare il mouse. Per fare il toggle su questo attributo si deve cliccare il tasto [c] quando se sei nella schermata home oppure nella schermata informazioni.

##  Punto della situazione rispetto alla pianificazione
Leggermente avanti rispetto alla programmazione

## Programma di massima per la prossima giornata di lavoro
Continuare la documentazione
