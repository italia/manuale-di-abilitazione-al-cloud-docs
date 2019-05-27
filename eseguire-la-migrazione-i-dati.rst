6. Eseguire la migrazione: i dati
=================================

La migrazione dei dati è il processo di trasferimento dei dati da un
sistema (sorgente) ad un altro (destinazione) utilizzando strumenti e
tecniche appropriati. Essendo questo uno degli aspetti più critici di
una migrazione al cloud, lo trattiamo approfonditamente in questo
capitolo fornendo esempi e buone pratiche specifiche per i diversi
scenari che la pubblica amministrazione può trovarsi ad affrontare.

Il processo di migrazione dei dati si articola tipicamente secondo
queste fasi:

1. preparazione della migrazione

2. validazione dei dati nel sistema sorgente

3. creazione dello schema dei dati nel sistema destinazione

4. mappatura delle strutture dati del sistema sorgente nel sistema
   destinazione

5. *conversione e trasferimento dei dati* dal sistema sorgente al
   sistema destinazione

6. validazione dei dati migrati nel sistema di destinazione

7. dismissione del sistema sorgente

Ognuna di queste fasi può essere eseguita secondo modalità diverse in
base al tipo di migrazione che si sta effettuando.

Con il costante aumento di dati memorizzati nel sistema sorgente, il
processo di migrazione diventa più complesso ed esposto a rischi come:

-  **perdita dei dati**: quando i dati vengono trasferiti nel sistema di
   destinazione, alcuni di essi potrebbero non venire trasferiti dal
   sistema sorgente

-  **inconsistenza dei dati**: anche quando la migrazione dei dati è
   eseguita in modo efficiente, possono esservi errori semantici come ad
   esempio la migrazione di un dato in una colonna differente sul
   sistema di destinazione. Un altro aspetto cruciale è l’ordine di
   esecuzione delle attività di migrazione che, se non effettuato
   correttamente, può non rispettare le dipendenze fra i dati. Ad
   esempio se dovessimo migrare un insieme di utenti e le loro liste dei
   desideri, le seconde andrebbero migrate dopo i primi

-  **downtime prolungato**: il processo di migrazione può richiedere più
   tempo di quanto pianificato e durante questo processo il sistema
   sorgente non è disponibile

-  **corruzione dei dati**: il sistema di destinazione può applicare
   regole e validazioni differenti da quello sorgente causando possibili
   crash di sistema e generazione di errori per l’utente finale che
   utilizza l’applicativo

-  **interferenze**: se il sistema sorgente o di destinazione sono in
   uso durante il processo di migrazione, le attività in corso possono
   causare degli imprevisti come ad esempio il locking delle tabelle o
   un disallineamento dei dati

Questi rischi possono essere mitigati adottando strumenti e tecniche di
test della migrazione dei dati, come raccomandato nella fase di
`validazione <#la-validazione-1>`__.

.. toctree::
  :maxdepth: 3
  :caption: Indice dei contenuti

  eseguire-la-migrazione-i-dati/la-preparazione-1.rst
  eseguire-la-migrazione-i-dati/buone-pratiche-1.rst
  eseguire-la-migrazione-i-dati/gli-scenari-di-migrazione-1.rst
  eseguire-la-migrazione-i-dati/la-validazione-1.rst
