5.5 La validazione
==================

| Come già descritto precedentemente, il processo di migrazione in cloud
  degli applicativi dell’amministrazione comporterà diversi cambiamenti
  che potrebbero avere un impatto negativo su vari aspetti come
  performance, funzionalità o dati degli applicativi migrati.
| Risulta quindi fondamentale l’utilizzo di pratiche che permettano di
  validare i cambiamenti attuati così da ridurre i rischi associati e
  garantire il corretto funzionamento del sistema.

| La validazione è una pratica che viene applicata in maniera
  continuativa e non solo alla fine di un processo di migrazione, così
  da accorciare il ciclo di feedback e reagire più velocemente in caso
  di problematiche.
| Nel validare la migrazione di uno o più applicativi vengono
  considerati diversi aspetti ad essi associati:

-  **validazione delle funzionalità applicative**

-  **validazione dell’integrità e completezza dei dati** (vedi capitolo
   6)

-  **validazione del mantenimento o miglioramento delle prestazioni**

-  **validazione della sicurezza**

La validazione di tutti questi aspetti passa attraverso l’utilizzo di
diverse tipologie di test che vedremo nel corso del capitolo e che
variano a seconda dell’aspetto da testare.

5.5.1 Tipologie di testing
--------------------------

Il testing del software può essere eseguito in due modi:

-  **manuale:** eseguito da tester che validano manualmente i test case
   senza utilizzare alcuno strumento di automazione. Il testing manuale
   è soggetto al rischio dell’errore umano e richiede un maggiore
   investimento, sia in termini di tempo che di risorse. Tuttavia,
   questo tipo di testing permette l’osservazione umana, che può essere
   utile se l’obiettivo è la facilità d’uso o migliorare l’esperienza
   degli utenti

-  **automatizzato:** eseguito utilizzando strumenti di automazione per
   validare la suite di test case. Il testing automatizzato è più
   affidabile, in quanto viene eseguito da strumenti e/o script, ed è
   anche molto più veloce del testing manuale. Può richiedere un
   investimento per acquisire gli strumenti di testing necessario, ma il
   costo viene solitamente ammortizzato poiché i test vengono eseguiti
   più volte nel corso di un lungo periodo di tempo

In generale, ci sono diverse parti e caratteristiche degli applicativi
che possono essere testate. Per questo motivo, esistono diverse
tipologie di test:

-  **unitari:** solitamente testano unità logiche interne al software e
   create dagli sviluppatori stessi, quindi non visibili ad un utente
   finale, in maniera isolata da tutte le altre unità logiche che
   compongono il sistema.

-  **di integrazione:** testano l’integrazione del core applicativo con
   componenti esterne, come ad esempio i database.

-  **di interfaccia:** testano il funzionamento dell’applicativo
   attraverso la sua interfaccia di utilizzo che sia grafica (UI) o
   programmatica (API)

-  **di sistema:** testano il funzionamento end to end dell’applicativo
   nell’insieme dei suoi componenti

-  **funzionali:** testano che l’applicativo rispetti i requisiti
   funzionali dal punto di vista dell’utilizzatore.

5.5.2 Validazione delle funzionalità
------------------------------------

Sostituire un applicativo con una versione SaaS o migrare lo stesso in
Cloud sono procedure che potrebbero comportare la perdita o il
malfunzionamento di alcune funzionalità precedentemente presenti nella
versione on-premise, causando un disservizio più o meno critico ai suoi
utilizzatori.

La validazione delle funzionalità punta, attraverso test funzionali, a
identificare la presenza o meno di questa tipologia di errori così da
poterli correggere.

La lista delle funzionalità desiderate è testata attraverso la verifica
di input e di output corrispondenti, senza porre l’attenzione su come i
dati vengano processati. I test simulano l’effettivo utilizzo del
sistema dal punto di vista di un utilizzatore e possono essere
effettuati sia manualmente, attraverso operatori che eseguono i
cosiddetti test case, che automaticamente attraverso l’utilizzo di tool
specifici che simulano l’operato di un essere umano.

Nel processo di validazione delle funzionalità vanno tipicamente
considerati i seguenti passi:

1. identificazione della lista di funzionalità desiderate

2. creazione dei test case tramite la definizione di un input e del
   relativo output che ci si aspetta, per ogni funzionalità

3. esecuzione del test case

4. verifica di input e output

5. produzione di un report che evidenzi eventuali problematiche

Il risultato di questa validazione potrà così essere utilizzato nelle
successive iterazioni, per risolvere eventuali problemi sorti nel corso
della migrazione.

5.5.3 Validazione delle prestazioni
-----------------------------------

| Nel caso di migrazione ad applicativi SaaS, garantire alte prestazioni
  è compito del fornitore del servizio.
| In caso di migrazione a servizi PaaS o IaaS invece, spesso si assume
  che semplicemente spostando un applicativo al cloud, questo potrà
  automaticamente beneficiare di tutti i suoi vantaggi, come ad esempio
  la scalabilità, come se il design dell’applicativo fosse già cloud
  native.
| La realtà è che spesso gli applicativi non possono godere appieno del
  nuovo ambiente, in quanto ad esempio la scalabilità offerta dal cloud
  non può sopperire alle prestazioni non ottimali dei software stessi.
| Questo tipo di problema si manifesta chiaramente quando applicativi
  che non hanno mai dato problemi on-premise, smettono di funzionare in
  cloud a causa ad esempio di alti carichi di utilizzo.
| Per questo motivo risulta fondamentale validare le prestazioni degli
  applicativi migrati attraverso l’utilizzo di strumenti di monitoring e
  attraverso specifici test:

-  **di carico:** verificano le prestazioni dell’infrastruttura per un
   determinato carico di utilizzo ed in un determinato periodo di tempo.
   Ad esempio: verifica dei livelli di memoria raggiunti con un carico
   di 1000 utenti simultanei per 5 minuti

-  **di stress:** verificano qual è la capacità massima
   dell’infrastruttura aumentando progressivamente il carico di utilizzo
   su di essa fino al raggiungimento del limite massimo

-  **di picco:** verificano come reagisce l’infrastruttura a carichi
   molto variabili, abbassando o alzando di molto il carico in un
   determinato range di tempo

-  **di connettività:** verificano tramite test automatici e manuali la
   `latenza <https://it.wikipedia.org/wiki/Latenza>`__ dell’applicativo
   migrato rispetto a quello on-premise

Nel processo di validazione delle prestazioni vanno considerati i
seguenti passi:

1. identificazione dei livelli di prestazioni desiderati per metriche
   come ad esempio:

   a. tempi di risposta

   b. throughput

   c. livelli di utilizzo di risorse:

      i.   CPU

      ii.  memoria

      iii. storage su disco

      iv.  network

2. definizione dei tipi di test da attuare e dei dati da utilizzare
   (piano di test)

3. configurazione degli strumenti di monitoraggio dei livelli di
   prestazioni identificati

4. esecuzione dei test tramite strumenti appositi

5. analisi dei risultati e tuning delle risorse

5.5.4 Validazione della sicurezza
---------------------------------

Le responsabilità per la sicurezza in cloud ricade fondamentalmente
sotto due categorie: quella associata al cloud service provider che
dovrà assicurarsi di rendere l’infrastruttura sicura e quella di chi
fruisce dei servizi che dovrà assicurarsi che gli applicativi utilizzino
tutte le misure necessarie garantire la sicurezza, argomento di cui
parleremo in questo sottocapitolo.

Migrare in cloud gli applicativi, apre ad uno spettro di rischi che
vanno considerati tramite l’applicazione di alcune pratiche:

-  | **sicurezza pre-migrazione:** prima di migrare risulta critico
     eseguire una review di tutti gli account e relativi permessi di
     accesso ai dati, così da evitare credenziali scadute che potrebbero
     compromettere la sicurezza una volta in cloud.
   | È inoltre molto importante avere una procedura per lo smaltimento
     delle risorse on-premise, una volta che non saranno più necessarie,
     avendo cura di eliminare qualunque dato già migrato, se non più
     necessario

-  | **identity management:** tra i vari servizi delle più moderne
     piattaforme cloud, vi è la possibilità di controllare l’accesso ad
     ogni informazione e risorsa messa a disposizione dal provider. Una
     gestione così dettagliata permette di essere molto flessibili ma
     richiede molta attenzione nel tenere traccia di chi può accedere e
     fare cosa.
   | È quindi buona norma consultare la documentazione dei provider
     cloud che dovrebbero fornire le buone pratiche relative agli
     strumenti di identity management messi a disposizione

-  **test di penetrazione:** questi test, effettuabili tramite strumenti
   appositi o da fornitori specifici, permettono di effettuare un check
   di tutte le vulnerabilità più comuni in cloud su più livelli:

   -  applicativo: testando le interfacce grafiche (UI) e programmatiche
      (API)

   -  dati: testando il loro accesso tramite applicativo o direttamente
      da database

   -  rete: testando se e quanto la rete protegge l’accesso ai dati

   -  normative: verificando quanto l’infrastruttura è conforme alle
      normative in vigore

-  **crittografia del dato:** è importante verificare di avere sempre
   attivato la crittografia dei dati, sia su database che su storage,
   così da evitare visibilità di questi ultimi in caso di violazione
   della sicurezza
