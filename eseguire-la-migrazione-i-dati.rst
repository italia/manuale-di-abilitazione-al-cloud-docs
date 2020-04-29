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
base al tipo di migrazione.

All'aumentare dei dati memorizzati nel sistema sorgente, il
processo di migrazione diventa più complesso ed esposto a rischi come:

-  **perdita dei dati**: alcuni dati presenti nel sistema sorgente
   potrebbero non essere trasferiti correttamente nel sistema di destinazione;

-  **inconsistenza dei dati**: anche una migrazione apparentemente corretta
   può nascondere delle insidie.
   Un dato potrebbe finire in una colonna differente, o l'ordine di esecuzione delle attività
   di migrazione potrebbe non rispettare le relazioni tra i dati;
   dovendo  migrare un insieme di utenti e le loro liste dei desideri,
   le seconde andrebbero migrate dopo i primi;

-  **downtime prolungato**: il processo di migrazione può richiedere
   più tempo di quanto pianificato e durante questo processo
   il sistema sorgente non è disponibile;

-  **corruzione dei dati**:  regole di validazione e di codifica differenti tra il sistema sorgente
   e quello di destinazione possono rendere indisponibili le applicazioni
   e generare errori anche permanenti,
   specie se vengono rilevati durante l'utlizzo degli applicativi.
   Questo può impattare anche sugli utenti finali;

-  **interferenze**: se il sistema sorgente o di destinazione sono in
   uso durante il processo di migrazione, possono
   verificarsi dei contenziosi sull'accesso e la modifica delle risorse
   (eg. locking delle tabelle) o un disallineamento dei dati.

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
