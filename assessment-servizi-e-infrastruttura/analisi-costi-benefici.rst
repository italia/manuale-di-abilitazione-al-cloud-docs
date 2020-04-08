3.3 Analisi costi-benefici
==============================

Determinare costi e benefici del cloud richiede un approccio sistematico
che tenga in considerazione tutti i fattori diretti ed indiretti che impattano
sulla migrazione.

Per un’analisi efficace è opportuno seguire questi passi:

1. definizione del periodo temporale su cui calcolare il ritorno
   sull’investimento (tipicamente 5 anni)

2. verifica dei costi attuali dell’infrastruttura e loro proiezione sul
   periodo temporale

3. stima dei costi dell’infrastruttura cloud e loro proiezione sul
   periodo temporale

4. stima dei costi di migrazione

5. stima dei costi di post-migrazione

6. valutazione dei costi rispetto ai benefici tangibili ed intangibili

Calcolare il costo totale di un servizio IT e compararlo con il
potenziale ritorno economico di una migrazione al cloud costituisce un
compito arduo, e l’analisi dei costi sul cloud computing non fa
eccezione come livello di difficoltà. Un'analisi dettagliata dei
benefici del cloud computing deve includere valutazioni a breve, medio e
lungo termine oltre ai costi di terminazione. A questo riguardo, ci sono
due indicatori chiave da considerare:

**Total Cost of Ownership (TCO)** = Costi iniziali + Costi ricorrenti +
Costi di terminazione

**Ritorno sull’investimento (ROI)** = ((Benefici tangibili + Benefici
intangibili) - TCO) / TCO

I costi nascosti che le organizzazioni potrebbero avere difficoltà a
rilevare in anticipo nello spostarsi ad un servizio cloud includono:

-  il costo per un cambio di provider dovuto ad una variazione
   regolatoria o di linea di condotta: per calcolare gli investimenti
   necessari per cambiare piattaforma di cloud, nel caso in cui problemi
   economici o regolatori lo rendano necessario, le organizzazioni
   devono tener conto di diversi fattori, tra cui il pagamento per
   l’estrazione e la validazione dei dati ed il costo di assunzione di
   risorse IT necessarie per compiere questo lavoro

-  le spese inaspettate dovute all’iniziale migrazione di sistemi:
   migrare verso applicazioni e servizi cloud include anche un numero di
   differenti costi che devono essere presi in considerazione. Le
   amministrazioni pubbliche o le software house, infatti, dovranno
   riscrivere le applicazioni per operare in un ambiente virtualizzato e
   riformattare i dati per adattarli ai formati del SaaS del fornitore

-  il lock-in con uno specifico modello di servizio proprietario: costi
   dovuti al fatto che l’amministrazione non riesce a svincolarsi
   facilmente da una scelta tecnologica precedentemente effettuata (vedi
   capitolo 4.3)

In generale, è importante considerare a livello economico le diverse
opzioni di migrazione al cloud che si possono avere in base alle
caratteristiche di ciò che si vuole migrare: retain, retire,
re-purchase, re-host, re-platform o re-architect (vedi capitolo 4.1 per
approfondire le strategie di migrazione). Ogni alternativa dovrebbe
essere analizzata in dettaglio per decidere il modello cloud migliore in
base al contesto e alle circostanze in cui l’amministrazione si trova.

3.3.1 Verifica dei costi attuali dell’infrastruttura
--------------------------------------------------------

Per calcolare i costi attuali dell’infrastruttura è necessario avere un
approccio olistico e considerare il costo complessivo di utilizzare e
manutenere la soluzione on-premise nel tempo, e non considerare
solamente quanto si paga per l’infrastruttura. Inoltre, questo calcolo
deve includere sia i costi diretti che quelli indiretti.

I **costi diretti** sono relativamente semplici da calcolare, in quanto
sono riportati direttamente a bilancio, e possono essere separati in due
gruppi:

-  un primo gruppo, che comprende i costi legati ad hardware e software:
   quanto si paga (o si è pagato) per i server fisici, le licenze
   software, contratti di manutenzione, le garanzie, le forniture, i
   materiali, i pezzi di ricambio ed il resto. Tutti questi costi devono
   essere pienamente documentati e vi si può accedere attraverso le
   fatture, gli ordini o i pagamenti conservati in contabilità. Si deve
   anche comprendere quanta banda, storage, e capacità del database si
   consuma e/o dettagli infrastrutturali come il numero di server, i
   tipi di database e storage per calcolare la stima dei costi
   infrastrutturali in cloud. Alcuni esempi più specifici sono:

   -  costi di acquisto materiali di consumo

   -  investimento per l’acquisto delle risorse (server, facility ecc)

   -  costi di manutenzione infrastruttura hardware (dischi, schede di
      rete ecc.)

   -  costi per licenze sistemi operativi, macchine virtuali, database,
      antivirus, backup

   -  costi per licenze applicativi

   -  backup di lungo termine periodico di VPS e dati

   -  disaster recovery

-  un secondo gruppo, che comprende invece i costi operativi, di cui
   esempi specifici sono:

   -  costo del lavoro per la manutenzione dei server, database ed altre
      tecnologie

   -  costi di manutenzione delle strutture che ospitano l’hardware,
      come i beni immobiliari, il personale ed altri costi relativi alle
      strutture

   -  costi di manutenzione infrastruttura di alimentazione (gruppi
      continuità, generatori, quadri comandi, ecc.) e di raffreddamento

   -  costi di connettività ad internet (tipo connessione, banda minima
      garantita, fallback in caso di fallimento, ecc.)

   -  costi amministrativi necessari per mantenere e amministrare il
      dipartimento IT. Questi possono includere le risorse da altri
      dipartimenti del proprio ente - personale, acquisti, ragioneria,
      ecc.x - che sono dedicati a gestire lo staff IT interno ed esterno

I **costi indiretti**, benché molto più difficili da calcolare, sono
importanti altrettanto quanto i costi diretti, in quanto possono
rappresentare una fetta importante dei costi complessivi dell’IT. Il
principale costo indiretto è la perdita di produttività degli impiegati
e degli utenti se l’infrastruttura IT non è disponibile. Per calcolare
questi costi, si possono analizzare i file di log per determinare quanto
di frequente i server hanno indisponibilità e per quanto tempo e
moltiplicare quel tempo per un valore medio orario. I costi indiretti
possono essere difficili da stimare, ma sono molto importanti da
considerare, in quanto possono rappresentare una fetta importante dei
costi complessivi dell’IT.

3.3.2 Stima dei costi dell’infrastruttura cloud
---------------------------------------------------

Dopo aver determinato i costi attuali dell'infrastruttura on-premise, è
necessario calcolare i costi potenziali dell'infrastruttura cloud. La
verifica dei costi attuali dovrebbe aver fornito una solida conoscenza
della capacità di rete, di archiviazione e di database necessaria per
eseguire le applicazioni che si desidera migrare al cloud.

I fornitori di infrastrutture cloud hanno ora semplificato le loro
strutture tariffarie in modo che i potenziali clienti possano
comprenderle più facilmente. Sono disponibili molti calcolatori di costi
cloud per dare un'idea dei costi dell'infrastruttura cloud,
indipendentemente dal fatto che si abbia selezionato un fornitore di
servizi cloud ancora.

Utilizzare i calcolatori dei prezzi dei CSP qualificati da AgID nel
Cloud Marketplace, laddove disponibili.

Il primo passo è inserire l'infrastruttura on-premise esistente o
pianificata. Utilizzando il calcolatore di base, si devono inserire le
seguenti informazioni:

-  **server**:

   -  tipo di server

   -  numero di macchine virtuali

   -  core della CPU

   -  memoria in GB

   -  hypervisor, sistema operativo guest e motore DB, se si immette un
      tipo di server

-  **storage**:

   -  tipo di archiviazione

   -  capacità raw di archiviazione

   -  percentuale acceduta raramente (se si utilizza Object Storage)

È possibile aggiungere righe per più server e tipi di archiviazione, se
necessario.

Il calcolatore avanzato chiede maggiori dettagli su server e storage e
prende in considerazione la rete e la forza lavoro IT nel calcolo del
TCO. È importante utilizzare la versione avanzata del calcolatore TCO,
in quanto questi dettagli aiuteranno a calcolare un costo potenziale più
accurato ed olistico.

Dopo aver inserito le informazioni, il calcolatore genera un rapporto
che riepiloga il confronto TCO a tre anni per categorie di costo. È
quindi possibile scaricare un rapporto completo che fornisce dettagliate
ripartizioni dei costi, le ipotesi e la metodologia utilizzata nel
modello di costo e le domande frequenti.

3.3.3 Stima dei costi di migrazione al cloud
------------------------------------------------

Il passo successivo è la stima dei costi coinvolti nell'esecuzione della
migrazione degli applicativi nel cloud. Ecco i componenti da considerare
quando si calcola il costo del processo di esecuzione della migrazione
del cloud:

-  **spostamento dei dati nel cloud**: uno dei passaggi più importanti
   di qualsiasi migrazione. I fornitori di servizi cloud potrebbero
   addebitare commissioni per il trasferimento dei dati ai loro sistemi,
   pertanto è necessario tenere conto di tali costi. Un altro elemento
   costoso potrebbe essere la manodopera necessaria per garantire che i
   dati dell’ente siano sincronizzati correttamente dopo
   l'implementazione sul cloud da sistemi legacy.

È possibile che si debbano realizzare anche soluzioni ponte per
garantire la sincronizzazione dei dati fra on-premise e cloud durante la
migrazione, quindi è necessario impiegare tempo e denaro per queste
operazioni. Ogni scenario è diverso, ma è necessario tenere conto di una
certa quantità di risorse da spendere per assicurarsi che i dati siano
sincronizzati.

-  **integrazione e test delle app**: sfortunatamente, alcune
   applicazioni non sono pronte per il cloud. Sia che si tratti di
   grandi sistemi ERP (`enterprise resource planning <https://it.wikipedia.org/wiki/Enterprise_resource_planning>`_) con funzionalità
   che dipendono da server on-premise o di software legacy in uso da
   anni, è necessario tenere in considerazione i costi di integrazione e
   test di queste app dopo averli spostati nel cloud.

La prima cosa da fare è capire come queste piattaforme interagiscono con
gli attuali sistemi operativi e infrastrutture. Successivamente, è
necessario determinare le modifiche che è necessario apportare affinché
questi sistemi funzionino correttamente nel loro nuovo ambiente cloud.
Quindi è il momento di apportare queste modifiche e testare gli
applicativi. Tutto questo costa tempo e denaro, quindi è necessario
assicurarsi di avere allocato risorse per queste operazioni.

-  **spese di consulenza**: l’organizzazione potrebbe non disporre di
   tutte le competenze e le risorse necessarie per eseguire una
   migrazione al cloud da sola. Una migrazione al cloud può risultare
   complessa e si può aver bisogno di esperienza e competenze esterne di
   supporto. Il contributo di un esterno può essere utile su diversi
   fronti: mappare un approccio strategico, sviluppare un'architettura
   cloud, eseguire il processo di migrazione stessa. Le conoscenze e
   l'esperienza dei consulenti in molti settori e situazioni possono
   essere molto preziose.

-  **licenze:** è importante eseguire una valutazione dei costi-benefici
   associati alla migrazione in cloud di software on-premise sotto
   licenza. Per informazioni più dettagliate si rimanda al capitolo 3.4
   Gestione delle licenze software in cloud.

Una conoscenza approfondita dei punti di forza e di debolezza
dell’amministrazione in relazione al cloud computing e alla migrazione
determina se è necessario l'aiuto di esperti del cloud. Sulla base di
questa conoscenza, è poi possibile approssimare i costi del tempo di
questi esperti in base al livello di assistenza di cui si necessita.

Se si decide che si ha bisogno dell'aiuto di un consulente, è importante
assicurarsi di aver compreso gli aspetti fondamentali da ricercare nella
selezione di un partner per la migrazione al cloud. Il partner può
essere una risorsa inestimabile, quindi ci si dovrà assicurare di
selezionare quello giusto.

Inoltre, si ricorda che le framework di lavoro del programma di
abilitazione al Cloud delle PA sono previsti centri di competenza sul
territorio, ovvero dei soggetti aggregatori di tecnici, esperti e
managers dell’IT per consolidare e potenziare le competenze, il *know
how* e l’esperienza relativa alla gestione dei servizi cloud nelle
amministrazioni. Questi centri saranno il punto di riferimento per le
pubbliche amministrazioni che si apprestano ad iniziare il proprio
percorso verso il cloud.

3.3.4 Stima dei costi post-migrazione
-----------------------------------------

Che cosa si deve pagare dopo aver completato la migrazione al cloud? I
costi di infrastruttura mensili che sono stati calcolati nel secondo
passaggio di analisi (vedi sezione 3.3.2), ovviamente.

Tuttavia, è necessario tenere in considerazione anche i costi diretti e
indiretti necessari per mantenere e migliorare il nuovo ambiente cloud,
in quanto molti di questi continueranno a essere pagati anche dopo il
completamento della migrazione iniziale.

Per determinare un accurato budget post-migrazione, si devono dunque
prevedere costi come: integrazione continua e test di app, formazione,
manodopera, sicurezza e conformità, amministrazione e altro.

3.3.5 Valutazione dei costi rispetto ai benefici tangibili ed intangibili
-----------------------------------------------------------------------------

Dopo aver calcolato tutti i costi, si potrebbe arrivare ad un numero
elevato rispetto a quanto si pensava o ad eventuali costi attuali
(tipicamente solo diretti) che si hanno in mente. Eppure è probabile che
quel numero sia più piccolo di tutti i costi che si stanno attualmente
pagando per l'infrastruttura on-premise.

Ma oltre ai risparmi sui costi, il cloud porta anche un elevato numero
di benefici immateriali che possono essere difficili da misurare
direttamente. Consente ad un’organizzazione di essere più flessibile e
agile in modo da poter testare e lanciare i servizi più velocemente e
reagire meglio alle mutevoli condizioni del mercato. Non ci si deve più
preoccupare di acquistare e configurare nuovi server per gestire la
domanda elevata, dato che è possibile scalare automaticamente i server
cloud istantaneamente. E si ha la tranquillità che la probabilità di un
down degli applicativi è minima grazie all'elevata disponibilità, al
bilanciamento del carico e alle funzionalità di backup dei fornitori
cloud.

Alcuni di questi benefici sono già stati trattati nel capitolo 1.2, ma
approfondiamo qui quelli da tenere in particolare considerazione durante
l’esecuzione di un’analisi costi-benefici.

3.3.5.1 Differenziale dei costi sul cloud rispetto ai costi on-premise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Confrontando i valori dei costi sul cloud e dei costi on-premise sul
periodo considerato, si può identificare il beneficio tangibile creato
dall’ eliminazione dei canoni di manutenzione richiesti dall’hardware di
proprietà e dei periodici acquisti per il rinnovo degli asset, dallo
snellimento delle attività sia tecniche (verifica funzionamento,
segnalazione malfunzionamenti, verifica apparecchiature obsolete) che
amministrative (gare, impegni di spesa, liquidazioni fatture, ecc.),
dalla riduzione dei costi di energia elettrica e tutte le altre voci
impattate dalla migrazione.

3.3.5.2 Dimensionamento reale o elasticità reale
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le soluzioni on premise sono tipicamente dimensionate rispetto alla
capacità necessaria per gestire il massimo carico previsto, sia esso
dovuto ad una crescita del servizio o a situazioni temporanee di picco.
Il provisioning delle macchine virtuali, della banda, della memoria e
della CPU o della spazio di storage sono dimensionati sulla base di
questi valori massimi che si prevedono di dover gestire.

Questo è legato al fatto che le infrastrutture on-premise sono poco
elastiche, ovvero risulta complesso aumentare o diminuirne il
dimensionamento: i tempi per aumentare le risorse a disposizione sono
significativi ed una volta acquisite nuove risorse non è tipicamente
vantaggioso rilasciarle, in particolare se solo per un periodo. Questo
rende l’infrastruttura on premise non dimensionata sul bisogno attuale.

Grazie alla facilità ed alla rapidità di allocazione di nuove risorse su
una piattaforma cloud, il dimensionamento deve essere effettuato sulle
correnti necessità, aumentando o diminuendo le risorse allocate solo in
caso di necessità.

Analizzare l’utilizzo effettivo delle risorse è quindi cruciale per un
corretto dimensionamento della soluzione in cloud. Per questo tipo di
analisi consultare metriche di utilizzo o utilizzare strumenti di
mercato che forniscono questo tipo di analisi.

3.3.5.3 Riduzione dei rischi di disservizio operativo, perdita dati e del rischio reputazionale
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gli applicativi in cloud godono di alta disponibilità, ovvero la
probabilità che i servizi siano indisponibili per problemi
infrastrutturali è molto bassa. Grazie alla possibilità di fare
provisioning delle risorse in tempi molto rapidi è anche possibile
rispondere a situazioni di carico non previste in modo tempestivo. Ciò
impatta il rischio di disservizio con i costi che questo ha associati.

Il rischio di perdita di dati per problemi infrastrutturali come la
rottura di un dispositivo sono altresì praticamente inesistenti,
azzerando i costi, tipicamente molto ingenti, legati alla perdita di
dati.

Grazie ai servizi di backup e ripristino disponibili in cloud è anche
possibile ritornare ad una situazione funzionante con minima perdita di
dati in tempi molto rapidi, nel caso vi siano motivi applicativi o di
violazione dei sistemi di sicurezza che causano una perdita di dati.

Il rischio reputazionale per l’ente causato dai problemi sopra elencati
ed il costo ad esso associato, anche se di difficile quantificazione
economica ma tipicamente elevato nel tempo, è quindi anch’esso ridotto
significativamente.

3.3.5.4 Semplificazione del disaster recovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

L’allestimento di un sito di disaster recovery in cloud è molto semplice
ed i suoi costi sono legati al suo utilizzo effettivo. In base
all’architettura dell’applicativo in cloud, ridondato su più data
center, tale sistema potrebbe diventare implicito.

3.3.5.5 Disponibilità di aggiornamenti, bugfix e miglioramenti più rapida
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Il passaggio in cloud permette aggiornamenti dell’applicativo più rapidi
e questo impatta le attività rendendo sempre disponibile la versione più
aggiornata ed affidabile dell’applicativo senza costi per
l’organizzazione.

Può essere utile valutare anche l’impatto economico di problemi
verificatisi in passato a causa di mancata tempestività nella
risoluzione o opportunità non colte in passato per il medesimo motivo.

3.3.5.6 Adeguamenti normativi su sicurezza e privacy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Amministrare le infrastrutture IT comporta responsabilità di sicurezza e
di protezione dei dati personali. Le recenti normative in materia di
privacy e di sicurezza informatica impongono anche alle pubbliche
amministrazioni l’adozione di misure tecniche e organizzative adeguate a
garantire la sicurezza del trattamento dei dati.

Molti provider di servizi cloud offrono un’ampia gamma di criteri,
tecnologie e controlli che rafforzano la sicurezza complessiva, grazie
alla protezione dei dati (che possono essere criptati con i più alti
livelli di sicurezza del mercato), dell’applicazione e dell’
infrastruttura da minacce potenziali.

Questo permette agli enti di utilizzare soluzioni complete, già mature e
disponibili o, a volte, trarne vantaggio in modo del tutto trasparente
in quanto soluzioni applicate in modo totalmente trasparente dal cloud
provider, senza dover investire soluzioni ad hoc e nelle competenze
necessarie per capire di quello di cui si necessita.

3.3.5.7 Miglioramento del servizio (percezione dell’utente finale)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sfruttando le potenzialità del cloud, le pubbliche amministrazioni hanno
l’opportunità di migliorare la qualità dei propri servizi, siano questi
ad uso interno o ad uso del cittadino.

Grazie al cloud, l’amministrazione può gestire i servizi in maniera più
efficiente ed efficace, riuscendo a concentrarsi maggiormente sulle
funzionalità da offrire ai propri utenti. Questo ha un ritorno economico
in termini di efficacia, efficienza e reputazione dei servizi.
