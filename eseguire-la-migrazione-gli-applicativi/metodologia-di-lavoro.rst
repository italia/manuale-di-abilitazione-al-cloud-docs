5.1 Metodologia di lavoro 
==========================

La migrazione al cloud è una sfida di tipo tecnologico ma, in modo
rilevante, anche culturale e di processo.

La metodologia di lavoro, ovvero l’insieme di quelle pratiche con cui il
team approccia e gestisce l’analisi, la progettazione e l'effettiva
migrazione al cloud degli applicativi, rientra a pieno titolo tra i
fattori da considerare a livello culturale e di processo.

5.1.1 Team cross-funzionale
---------------------------

Il team di progetto deve includere tutte le competenze necessarie per
poter eseguire le attività relative alla migrazione e trovare le
soluzioni necessarie durante l’esecuzione.

Questo team cross-funzionale deve comprendere non solo competenze
tecniche ma anche competenze normative, di processo, di comunicazione o,
in senso più generale, necessarie ad affrontare le principali
problematiche che si possono manifestare nell’esecuzione
dell’iniziativa.

5.1.2 Iteratività e incrementalità 
-----------------------------------

Tutte le fasi di un piano di migrazione devono essere *iterative* ed
*incrementali* rispetto ad un insieme *prioritizzato* di azioni che si
vogliono intraprendere sia nel caso si stia definendo il piano di
migrazione degli applicativi, sia nel caso si stia eseguendo una
specifica migrazione.

Nel caso si stia definendo il piano di migrazione è opportuno:

1. prioritizzare gli applicativi secondo i criteri suggeriti in questo
   documento

2. identificare la strategia di migrazione per l’applicativo a priorità
   più alta

3. analizzare i gap di competenze necessarie per eseguire la migrazione

4. se la fattibilità tecnica, operativa e di competenze è confermata,
   procedere con l’esecuzione della migrazione oppure passare
   all’analisi dell’applicativo con priorità successiva

5. nel caso si sia eseguita la migrazione, alla luce dei risultati
   ottenuti, rivedere la prioritizzazione effettuata inizialmente

6. con il passare del tempo possono altresì mutare delle condizioni che
   hanno definito la prioritizzazione o l’analisi di dettaglio di un
   applicativo (es. valore generato da un applicativo, identificazione
   di applicativi non ancora censiti, ...). Per questo motivo è
   consigliabile rivedere con cadenza regolare l’elenco degli
   applicativi da migrare e ripartire con il processo dall’inizio

Nel caso si stia eseguendo una specifica migrazione è opportuno che:

1. le iterazioni siano di poche settimane (una o due)

2. al termine di ogni iterazione, si mostri il progresso attraverso il
   rilascio di piccole modifiche incrementali che mantengano
   l’applicativo funzionante

3. il risultato dell’iterazione sia validato con gli stakeholder del
   progetto per ottenere un riscontro con cadenza regolare
   sull’avanzamento dell’attività. Ciò consente di intercettare problemi
   o opportunità di miglioramento con tempestività riducendo
   significativamente il costo di correzione del problema e permettendo
   di riprioritizzare le azioni da intraprendere sulla base
   dell’opportunità identificata

4. l’elenco delle attività sia riprioritizzato rispetto ai nuovi
   problemi da fissare e/o alle nuove opportunità emerse

5.1.3 DevOps
------------

Sviluppatori, sistemisti e tester devono adottare un approccio operativo
conforme alle pratiche
`DevOps <https://it.wikipedia.org/wiki/DevOps>`__ per garantire
comunicazione, collaborazione e integrazione tra sviluppatori e addetti
alle operations.

DevOps risponde all'interdipendenza tra sviluppo software e IT
operations, ed aiuta un'organizzazione a sviluppare in modo più rapido
ed efficiente prodotti e servizi software.

Un’amministrazione pubblica può trovarsi in uno di questi scenari per un
applicativo:

1. controlla le attività di sviluppo (dev) e di deployment/messa in
   produzione (ops)

2. controlla le attività di deployment/messa in produzione (ops) e
   delega ad un soggetto terzo lo sviluppo (dev)

3. delega ad un soggetto terzo sia le attività di sviluppo che di
   deployment

4. acquista una soluzione di mercato e ne gestisce il deployment sulla
   propria infrastruttura

5. acquista una soluzione erogata da terze parti

Nei primi tre scenari si raccomanda di prevedere pratiche DevOps a
livello organizzativo e/o contrattuale. Nello scenario 4. si suggerisce
di richiedere evidenza delle pratiche adottate dal produttore prima
dell’acquisto e di lavorare congiuntamente per la realizzazione di un
processo integrato di deployment. Nello scenario 5. si raccomanda di
richiedere evidenza delle pratiche adottate dal produttore prima
dell’acquisto.

5.1.4 Collaborazione e confronto continuo
-----------------------------------------

Le parti interessate, o stakeholders, ed il team di progetto devono
congiuntamente definire:

-  gli **obiettivi**

-  gli **indicatori** per la loro misurazione

-  il **valore** che si vuole generare per gli utenti finali

all’inizio dell’iniziativa di migrazione e mantenerli aggiornati durante
l’esecuzione a fronte delle criticità ed i punti di attenzione che via
via emergeranno.

Le parti interessate devono altresì validare i risultati presentati al
termine di ogni iterazione dal team di progetto in modo da identificare
il prima possibile elementi che richiedono correzioni o variazioni e
discutere le criticità emerse che condizionano il raggiungimento dei
risultati attesi, fino a ridefinire gli obiettivi o il valore atteso se
necessario.

Figure rilevanti da coinvolgere nel processo sono i rappresentanti degli
utenti finali che beneficeranno degli effetti della migrazione, sia che
questa impatti i processi sia che questa riguardi solo i dati. Il loro
coinvolgimento favorisce la validazione dei risultati, la comprensione,
l’accettazione e la diffusione fra gli altri utenti del processo di
cambiamento in atto.

È importante sottolineare che l’aspetto cruciale è l’interazione fra gli
individui piuttosto che i processi e gli strumenti usati.

Una volta avviato il progetto, il team (probabilmente composto sia da
dipendendenti della pubblica amministrazione che da fornitori) dovrà
gestirsi e coordinarsi autonomamente.

Per facilitare la collaborazione, le seguenti pratiche dovrebbero essere
adottate e adattate a seconda del contesto:

-  **visualizzazione del lavoro in corso:** tramite una Kanban board
   fisica o digitale che permetta di avere visione complessiva del
   lavoro programmato, in corso e concluso per l’iterazione corrente

-  **stand-up giornaliero**: un breve meeting di 5-15 minuti (a seconda
   della dimensione del team) da organizzare al mattino durante il quale
   ciascun membro del team dà un breve aggiornamento sui progressi ed
   eventuali blocchi del giorno precedente e sintetizza gli obiettivi
   per la sua giornata

-  **showcase alla fine di ogni iterazione**: un incontro di circa
   un’ora da organizzare alla fine di ogni iterazione (ogni una o due
   settimane) durante il quale si presentano i risultati raggiunti e il
   valore prodotto nell’iterazione corrente e si discute il piano per
   l’iterazione successiva integrando eventuali feedback.

-  **retrospettiva**: un altro meeting ricorrente di circa un’ora da
   organizzare alla fine di ogni iterazione durante il quale il team ha
   l’occasione di analizzare, in retrospettiva appunto, l’iterazione
   appena conclusa con l’obiettivo di migliorare continuamente sia il
   processo che l’esecuzione, tenendo in considerazione i feedback di
   ciascun membro del team

5.1.5 Miglioramento continuo
----------------------------

La pratica della retrospettiva è stata introdotta per rispondere alla
necessità di effettuare riflessioni regolari sull’andamento del
progetto, in modo da correggerne il funzionamento prima che sia finito.
Questo in contrasto con le tradizionali review post-mortem, che danno
informazioni utilizzabili solo in progetti seguenti e che non aiutano
dunque a raggiungere il successo nei progetti in corso.

La retrospettiva è conosciuta come pratica della metodologia Agile in
quanto uno dei principi del `manifesto
Agile <https://agilemanifesto.org/>`__ è incentrato proprio sulla
riflessione in team: "Ad intervalli regolari il team riflette su come
diventare più efficace, dopodichè regola e adatta il proprio
comportamento di conseguenza."

Lo scopo generale di una retrospettiva è stimolare l’analisi e la
riflessione e incoraggiare il miglioramento continuo. In particolare,
gli obiettivi sono:

-  aumentare il livello di interazione e condivisione del team

-  identificare cosa è andato bene e cosa non ha funzionato in relazione
   a processi, strumenti e dinamiche di gruppo

-  discutere e scoprire opportunità di miglioramento e definire un piano
   d’azione per implementarlo

-  enfatizzare e dare uguale tempo di valutazione e condivisione a ciò
   che andato bene. È importante concentrarsi sul positivo e
   identificare ciò che è andato bene in modo da continuare a farlo

La retrospettiva è un modo per spronare i membri del team a riflettere
su quello che succede intorno a loro nel corso del progetto e ad
identificare azioni che possano migliorare sia il processo che
l’esecuzione. In concreto, si tratta di un incontro di circa un’ora che
si tiene alla fine di una iterazione durante il quale il team riflette
su quanto accaduto durante l’iterazione appena trascorsa e individua le
azioni per migliorare la successiva. Si consiglia di eseguire la
retrospettiva con regolarità includendo sia il team tecnico
dell’amministrazione che il team tecnico del fornitore.

Per eseguire una retrospettiva efficace è importante trovare la tecnica
ed il formato più adatto al contesto. Per approfondire puoi consultare il libro di Esther
Derby “Agile Retrospectives: Making Good Teams Great”
o altre risorse disponibili online, come ad esempio `questo
articolo <http://www.marioconcina.it/blog/come-fare/5-tecniche-di-retrospettive-agile.html>`__.
