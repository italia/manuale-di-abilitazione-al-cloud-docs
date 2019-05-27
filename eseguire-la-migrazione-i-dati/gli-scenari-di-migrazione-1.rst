.. _gli-scenari-di-migrazione-1:

6.3 Gli scenari di migrazione
=============================

Ci sono diversi scenari di migrazione dei dati:

-  migrazione verso la medesima versione di sistema di basi di dati

-  migrazione verso una versione più recente del sistema di gestione di
   basi dati rispetto a quello di origine

-  migrazione verso un nuovo database, in cui il sistema di destinazione
   è un software di gestione di basi dati diverso da quello di origine

-  cambio di applicativo, in cui i dati devono essere trasferiti ad un
   diverso applicativo con un diverso schema di dati

La migrazione può essere un processo eseguito una volta sola (one time
migration) o in modo incrementale (incremental migration). Il secondo
approccio può essere necessario nel caso ci sia la necessità di
mantenere pienamente funzionanti sia il sistema sorgente che il sistema
destinazione per un periodo di tempo limitato.

6.3.1 Migrazione verso lo stesso sistema di gestione delle basi dati
--------------------------------------------------------------------

Nel caso in cui la versione del sistema di gestione della base dati
sorgente e destinazione siano il medesimo, è consigliabile utilizzare
gli strumenti che il sistema stesso mette a disposizione per la
migrazione, come ad esempio lo strumento di dump del database.

Il dump del database sorgente, il suo trasferimento sull’ambiente di
destinazione ed il ripristino permettono di completare la migrazione in
un’unica volta.

La creazione dello schema del database, la migrazione dei dati e la loro
validazione avvengono durante il processo di ripristino.

Utilizzando gli strumenti di backup incrementale del database sorgente,
e conseguente ripristino sul database di destinazione, è invece
possibile ottenere la migrazione dei dati attraverso un processo
incrementale.

6.3.2 Migrazione verso una versione più recente del sistema di gestione delle basi dati
---------------------------------------------------------------------------------------

Nel caso in cui la versione del sistema di gestione della base dati di
destinazione sia più recente rispetto a quella sorgente, è necessario
verificare che vi sia piena compatibilità fra le due versioni in termini
di definizione del database prima di procedere alla migrazione vera e
propria.

Appurata la compatibilità, è consigliabile utilizzare gli strumenti che
il sistema stesso mette a disposizione per la migrazione, come ad
esempio lo strumento di dump del database o di backup incrementale come
descritto nel sottocapitolo precedente.

6.3.3 Migrazione verso un diverso sistema di gestione delle basi dati
---------------------------------------------------------------------

Nel caso in cui si vogliano migrare i dati ad un diverso sistema di
gestione delle basi dati, la problematica principale che si deve
affrontare è legata alle possibili variazioni nei linguaggi di
manipolazione dei dati.

Per gestire la migrazione dei dati è consigliabile utilizzare gli
strumenti forniti direttamente dal cloud provider. Se non sono
disponibili, si possono utilizzare strumenti di terze parti, anche open
source, disponibili sul mercato o servizi che si occupano di fare la
migrazione fra un motore di database ed un altro.

La fase di *conversione* dello schema di dati del sistema sorgente nel
formato supportato dal sistema di gestione di basi di dati di
destinazione *e* la *creazione dello schema* vengono gestite
direttamente dallo strumento fornito dal cloud provider o dallo
strumento di terze parti. Per la conversione si raccomanda di utilizzare
uno degli strumenti disponibili sul mercato, noti come `Schema
Conversion Tool <https://en.wikipedia.org/wiki/Schema_migration>`__\ *.*

La migrazione incrementale in questo scenario non è raccomandabile in
quanto il rischio di corruzione dei dati è molto alto.

6.3.4 Migrazione verso un diverso applicativo
---------------------------------------------

Nel caso in cui si vogliano migrare i dati ad un diverso applicativo si
deve tipicamente affrontare un processo di rimappatura delle
informazioni dal modello del sistema sorgente al modello del sistema
destinazione scrivendo degli script specifici che facciano le
trasformazioni necessarie e generino codice che può essere eseguito sul
sistema destinazione per caricare i dati modificati.

I principali fornitori di soluzioni SaaS forniscono API per le
operazioni di import ed export. In caso non fossero disponibili si
suggerisce di verificare la disponibilità sul mercato di strumenti di
terze parti.
