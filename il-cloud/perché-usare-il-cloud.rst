**1.2 Perché usare il cloud**
=============================

Il cloud rappresenta un grande cambiamento rispetto alla visione
tradizionale delle pubbliche amministrazioni in materia di risorse IT.
Per una vasta gamma di servizi e sistemi, che vanno dalla sicurezza
informatica alla produttività individuale e all’archiviazione, le
soluzioni cloud rappresentano spesso la soluzione più vantaggiosa per
diversi motivi.

**1.2.1 Riduzione dei costi**
-----------------------------

Le applicazioni che utilizzano risorse hardware on-premise richiedono un
investimento iniziale significativo, anche se il software utilizzato è
gratuito o open source. Oltre ad essere necessari per ospitare anche il
software gestionale più semplice, data center, reti, server, storage e
sistemi operativi richiedono investimenti, tempo e personale dedicato
per garantirne il corretto funzionamento e il continuo aggiornamento nel
rispetto di standard qualitativi e di sicurezza.

Il cloud elimina sia le spese di capitale iniziali necessarie per
l’acquisto di hardware (PaaS, IaaS) e software (SaaS) che i costi legati
alla gestione dei data center locali. Le applicazioni in cloud, infatti,
richiedono investimenti iniziali estremamente limitati e si pagano
generalmente in base al consumo, consentendo così di gestire la crescita
di un servizio in maniera dinamica. La decisione di migrare verso una
nuova soluzione non è, quindi, condizionata da eventuali investimenti
già fatti. Allo stesso tempo, poiché si paga solo il consumo della
risorsa, quando un servizio non è più utilizzato, non è più un costo.

Inoltre, le applicazioni basate su hardware on-premise richiedono un
piano di investimenti che deve tener conto dei prezzi riferiti al
momento della sottoscrizione del contratto e di alcuni anni di
manutenzione e supporto. I costi complessivi, per es. licenze, energia
elettrica, potenza di calcolo, manodopera e così via, raramente
diminuiscono nel corso della durata del servizio. Al contrario, i
servizi cloud tendono ad essere sempre più economici per le dinamiche di
mercato, infatti, la pressione competitiva, l’hardware ottimizzato e
l’aumento dei tassi di utilizzo stanno riducendo progressivamente i
costi delle applicazioni in cloud e delle infrastrutture virtuali.

Infine, i provider di servizi cloud offrono generalmente strumenti di
monitoraggio e alerting che facilitano un controllo continuo e una
gestione efficiente dei costi. È possibile, ad esempio, monitorare più
precisamente i costi associati ai singoli servizi e l’eventuale presenza
di “risorse zombie”, cioè risorse infrastrutturali non usate e che
possono essere spente, risparmiando sul costo associato. Per un
approfondimento su questo tema si veda il capitolo 5.3.8.

In generale, a seconda della categoria di cloud computing scelta (vedi
sopra: SaaS, PaaS, IaaS), del tipo di applicativo da migrare, della
rispettiva strategia di migrazione e del contesto in cui
l’amministrazione opera, la riduzione dei costi sarà più o meno
consistente. Si consiglia di far riferimento al capitolo 3.3 per
pianificare l’ottimizzazione dei costi prima di una migrazione
identificando le aree ed i componenti su cui è possibile ottenere un
vantaggio in termini di costo una volta in cloud rispetto alla
situazione corrente.

**1.2.2 Elasticità reale**
--------------------------

Le soluzioni IT on-premise, anche quando sono scalabili, hanno dei
limiti. Ad esempio, è necessario pianificare investimenti e sforzi
costanti per mantenere i margini sufficienti di scalabilità ed evitare
situazioni di sottodimensionamento, causando disservizi, o
sovradimensionamento, causando uno spreco di risorse e costi maggiori.
Per poter garantire la vera elasticità, è necessario mantenere
costantemente attivo un grande surplus di risorse che rimangono tuttavia
non utilizzate per la maggior parte del tempo.

A differenza delle soluzioni on-premise, i servizi cloud sono davvero
elastici: le risorse di calcolo, storage o rete possono essere consumate
solo quando richiesto e dismesse quando non sono più necessarie,
riducendo la complessità nella pianificazione della capacità
dell’infrastruttura IT.

Ridimensionare le risorse in modo realmente elastico significa, infatti,
fornire la giusta quantità di risorse IT (ad esempio maggiore o minore
potenza di calcolo, risorse di archiviazione e larghezza di banda)
proprio quando è necessario.

Infine, il paradigma cloud non richiede alcun investimento a lungo
termine sull’hardware e non comporta quello spreco di risorse
determinato dalla sottoutilizzazione della capacità.

**1.2.3 Facilità degli aggiornamenti**
--------------------------------------

Le soluzioni IT commerciali o auto-sviluppate in locale richiedono
finanziamenti, risorse umane, impegno e pianificazione per poter essere
aggiornate costantemente. Il supporto e gli aggiornamenti sono attività
costose e complicate da gestire ed è molto difficile per qualsiasi
organizzazione tenere il passo con la costante richiesta di
aggiornamenti e patch di sicurezza. Ne consegue che, spesso, le
infrastrutture della pubblica amministrazione non vengono adeguatamente
aggiornate.

In cloud invece, a seconda della categoria di cloud computing utilizzata
(vedi sopra: SaaS, PaaS, IaaS), la responsabilità di queste dinamiche
viene ridistribuita tra fornitore e amministrazione.

Nello specifico in caso di servizi SaaS, l’aggiornamento del software e
dell’infrastruttura è completamente demandata al fornitore ed incluso
nei costi.

Per servizi PaaS e IaaS invece, la responsabilità dell’amministrazione
ricade nell’ambito della gestione dell’applicativo e degli accessi alle
piattaforme, mentre i fornitori si occupano di garantire l’aggiornamento
delle risorse infrastrutturali e degli ambienti.

**1.2.4 Riduzione complessità del supporto**
--------------------------------------------

I servizi IT tradizionali spesso dipendono dal software installato sul
computer dell’utente. Quest’ultimo deve essere gestito insieme a tutte
le altre applicazioni dell’utente. In molti casi, si rende necessario
soddisfare dipendenze applicative molto specifiche legate alle versioni
del sistema operativo e degli aggiornamenti di sistema affinché il
software funzioni correttamente.

Gli aggiornamenti devono essere testati prima di essere applicati su un
numero elevato di sistemi e, a volte, un’applicazione obsoleta può
rallentare l’adozione di nuovi sistemi operativi e di applicazioni più
moderne.

I servizi cloud sono progettati per essere fruibili tramite internet.
Per rimanere sul mercato, i fornitori devono aggiornare i propri servizi
per supportare le ultime versioni dei browser, i sistemi operativi e le
scelte dei dispositivi dei propri utenti.

Per una pubblica amministrazione che gestisce migliaia di dispositivi,
come laptop, desktop e dispositivi mobili, una qualsiasi soluzione che
riduca la quantità di lavoro necessaria a mantenere il software
aggiornato rappresenta un gran vantaggio.

**1.2.5 Riduzione delle attività manuali a basso valore aggiunto**
------------------------------------------------------------------

I data center on-premise richiedono in genere un impegno notevole
nell'organizzazione e nell'assemblaggio dei
`rack <https://it.wikipedia.org/wiki/Rack_(informatica)>`__, nella
configurazione degli apparati (ad esempio: server, storage, apparati di
networking), nell'applicazione di patch software e altre attività di
gestione IT dispendiose in termini di tempo.

La semplicità con cui si possono aumentare o ridurre le risorse
necessarie in cloud ad esempio, permetterà alle amministrazioni di
alleggerire notevolmente tutte quelle operazioni a basso valore aggiunto
e il lungo iter burocratico necessario per il provisioning di risorse
aggiuntive.

Grazie alla facilità degli aggiornamenti e del supporto semplificato dei
servizi cloud, invece, l’amministrazione non ha bisogno di aggiornare i
sistemi operativi dei server, acquistare hardware, contrattualizzare
personale esterno, pianificare le operazioni o migrare i dati per
ottenere i benefici della tecnologia più recente.

Infine, il cloud facilita l’adozione di pratiche di automazione che
aumentano la ripetibilità di operazioni critiche e permettono di
accelerare i processi di delivery, riducendo al minimo la possibilità di
errori o configurazioni errate aumentando il controllo sui processi. Per
un approfondimento su questo tema si rimanda al capitolo 5.3.9.

**1.2.6 Adeguamento normativo in termini di sicurezza e privacy**
-----------------------------------------------------------------

Amministrare le infrastrutture IT comporta responsabilità non solo di
tipo economico-amministrativo, ma soprattutto di sicurezza e di
protezione dei dati personali. Le recenti normative in materia di
privacy e di sicurezza informatica (ad es.
`GDPR <https://eugdpr.org/>`__ e `misure minime di sicurezza informatica
ICT per la pubblica
amministrazione <https://www.agid.gov.it/it/sicurezza/misure-minime-sicurezza-ict>`__)
impongono infatti anche alle pubbliche amministrazioni l’adozione di
misure tecniche e organizzative adeguate a garantire la sicurezza del
trattamento dei dati.

Molti provider di servizi cloud offrono un’ampia gamma di metodi,
tecnologie e controlli che rafforzano la sicurezza complessiva, grazie
alla protezione dei dati (che possono essere criptati con i più alti
livelli di sicurezza del mercato), dell’applicazione e dell’
infrastruttura da minacce potenziali. I cloud service provider (CSP)
qualificati da AGID e consultabili sul `Cloud
Marketplace <https://cloud.italia.it/marketplace/supplier/market/index.html>`__
hanno infrastrutture e servizi sviluppati secondo criteri di
affidabilità e sicurezza considerati necessari per i servizi digitali
della PA. Ad esempio, i data center dei CSP hanno tutti la
certificazione `ISO/IEC
27001 <https://it.wikipedia.org/wiki/ISO/IEC_27001>`__. Questo e altri
criteri di qualificazione in termini di sicurezza dei CSP possono essere
consultati nel `Kit Percorsi di qualificazione CSP e
SaaS <https://www.agid.gov.it/sites/default/files/repository_files/kit_percorsi_di_qualificazione_id2.pdf>`__.

Nell’ambito della sicurezza, i provider di servizi cloud offrono anche
servizi specifici di disaster recovery (vedi capitolo 5.3.10), che
permettono un ripristino più rapido dei sistemi IT maggiormente critici
senza sostenere le spese di un secondo sito fisico. Questo garantisce la
continuità operativa dell’infrastruttura ed elimina il rischio di
perdita di dati. Inoltre, le applicazioni cloud sono in grado di mettere
a disposizione dell’amministratore strumenti di auditing e controllo
delle informazioni che consentono interventi puntuali all’insorgere di
eventuali problemi.

Certamente non basta dotarsi di soluzioni cloud per assicurare privacy
ai propri utenti e sicurezza delle infrastrutture e servizi IT, bensì
serve un processo continuo di vigilanza e controllo che fin dalla prima
fase di progettazione dei servizi, agisca trasversalmente su tutte le
aree di interesse, e che sia costantemente aggiornato rispetto allo
stato dell’arte delle principali misure di sicurezza.

**1.2.7 Miglioramento dei servizi**
-----------------------------------

| Sfruttando le potenzialità del cloud, le pubbliche amministrazioni
  hanno l’opportunità di migliorare la qualità dei propri servizi, siano
  questi ad uso interno o ad uso del cittadino.
| Grazie al cloud, l’amministrazione può gestire i servizi in maniera
  più efficiente ed efficace, riuscendo a concentrarsi maggiormente
  sulle funzionalità da offrire ai propri utenti.

Prima di tutto, il cloud garantisce un rapido accesso a tutte le
informazioni indipendentemente dalla propria postazione fisica. I dati
sono infatti accessibili ovunque, attraverso una molteplicità di device
e secondo standard di sicurezza elevati, presentato precedentemente.

Inoltre, l’adozione del cloud favorisce l’uso di architetture moderne,
basate su principi tecnologici avanzati come ad esempio il basso
accoppiamento dei componenti e il “design for failure” (per
approfondimento si veda il capitolo 5.4.3), lontani dalla struttura
monolitica degli applicativi legacy. Questo rende gli applicativi molto
più adeguati alle necessità di interoperabilità e comunicazione tra
diversi servizi (e tra le rispettive basi di dati). Le soluzioni SaaS
dei cloud service provider (CSP) qualificati da AGID e consultabili sul
`Cloud
Marketplace <https://cloud.italia.it/marketplace/supplier/market/index.html>`__,
ad esempio, offrono tutte uno strato di interoperabilità fruibile
tramite API. Questo permette di avere maggiore flessibilità nel provare
nuovi servizi o apportare modifiche.

Nel caso un applicativo debba essere scomposto nelle sue parti prima di
essere migrato al cloud (si veda il capitolo 4.1.6 per la strategia di
migrazione Re-architect), l'amministrazione ha la possibilità di usare
questo cambiamento come occasione per ridisegnare il servizio anche nel
suo processo per renderlo più adatto alle esigenze degli utenti (e per
questa finalità si consiglia di consultare le linee guida che si trovano
sul sito di
`designers.italia.it <https://designers.italia.it/guide/>`__).

Infine, grazie alla scalabilità reale del cloud, si ha un miglioramento
dell’accessibilità e della disponibilità dei servizi. Usando applicativi
in cloud, l’amministrazione può assicurarsi che tali applicativi siano
disponibili anche durante i picchi di accesso. Ad esempio, nel caso di
un servizio con picchi di traffico solo in determinati periodi dell’anno
(come il servizio di iscrizione alle scuole elementari dove i genitori
accedono e iscrivono i propri figli solo ad inizio anno) si ha la
sicurezza di non incorrere in downtime o momenti di disservizio durante
i periodi di maggiore carico.

**2. Come iniziare**

Iniziare è spesso lo scoglio più grande da superare quando si decide di
intraprendere una nuova attività o di adottare un nuovo paradigma come
quello cloud. Proprio per questo, l’obiettivo primario è di fornire
delle linee guida che aiutino le pubbliche amministrazioni a fare il
primo passo verso il cloud, e a pianificare efficacemente la migrazione
dei loro servizi.

In questo capitolo, oltre ad informazioni molto operative sui contatti
ed il procurement, offriamo una visione d’insieme sull’approccio da
attuare per iniziare a migrare al cloud l’insieme degli applicativi (e i
rispettivi servizi) che la pubblica amministrazione gestisce. Ogni fase
dell’approccio verrà poi approfondita nei capitoli successivi del
documento.

**2.1 Chi contattare**

Per iniziare il processo di migrazione al cloud operativamente, si
possono contattare i soggetti indicati nel `programma di abilitazione al
Cloud delle
PA <https://cloud.italia.it/projects/cloud-docs/it/latest/cloud-enablement.html>`__\ .

**2.2 Il procurement**

Le indicazioni sul procurement verranno fornite da Consip.

**2.3 Roadmap di una migrazione**

La migrazione dell’intero parco applicativo al cloud è un’operazione
complessa che riguarda aspetti tecnologici, di processo e culturali.

È cruciale per il successo dell’operazione iniziare a beneficiare della
nuova architettura durante il percorso, gradualmente, e non solo al
termine dell’intera transizione.

Per raggiungere questo risultato e contestualmente ridurre i rischi
legati a questa sfida, è fondamentale procedere in modo iterativo ed
incrementale partendo dagli applicativi che traggono un beneficio
significativo dall’adozione del paradigma cloud, che al contempo
rappresentano un rischio ridotto per la continua erogazione dei servizi
supportati e che risultano relativamente semplici da migrare.

Questo approccio permette al team di lavoro di scoprire ed affrontare le
problematiche che emergono strada facendo, senza particolari pressioni
legate alla criticità dell’applicativo. La conoscenza che si sviluppa
nel superare queste sfide è poi di supporto quando si devono affrontare
applicativi a rischio maggiore: la conoscenza acquisita con le
migrazioni precedenti infatti riduce il rischio delle migrazioni
successive.

Le migrazioni iniziali devono anche contribuire a creare l’evidenza del
valore del cloud e la fiducia necessaria a procedere con le successive
migrazioni includendo i cambiamenti che possono essere richiesti a
livello di processi, attività o responsabilità.

Riassumendo la strategia di migrazione da adottare in una roadmap,
ovvero in un percorso che permetta di definire in modo chiaro gli
obiettivi di ogni fase, possiamo identificare tre momenti rilevanti:

1. **Ora**: ovvero la fase iniziale focalizzata sulla creazione dei
   primi casi di successo con applicativi scelti secondo specifici
   criteri di prioritizzazione (vedi capitolo 3.1.2)

2. **Subito dopo**: ovvero una seconda fase con obiettivi da conseguire
   a seguito dell’esperienza fatta nella prima fase e degli
   apprendimenti e della conoscenza maturata su: gli aspetti specifici
   della piattaforma cloud selezionata come destinazione, i vincoli
   incontrati e le problematiche specifiche emerse durante la migrazione
   degli applicativi rispetto al contesto di partenza

3. **Più tardi**: ovvero un’ultima fase in cui si va a concludere il
   processo forti dell’esperienza e dei successi conseguiti nelle fasi
   precedenti

Le tre fasi identificate suggeriscono un approccio multi-fase che può
poi essere adattato alle specifiche realtà.

|image0|

+-----------------------+-----------------------+-----------------------+
| OBIETTIVO:            | OBIETTIVO:            | OBIETTIVO:            |
|                       |                       |                       |
| Creare i **primi casi | Sfruttando le         | Concludere la         |
| di migrazione di      | conoscenze maturate   | **migrazione degli    |
| successo** mostrando  | nella fase            | applicativi           |
| il valore che si      | precedente, creare    | rimanenti**, **più    |
| ottiene dalla nuova   | altri **casi di       | rischiosi e più       |
| infrastruttura        | successo con          | complicati** forti    |
|                       | migrazioni che        | delle esperienze      |
|                       | mostrano l’alto       | precedenti            |
|                       | valore dalla          |                       |
|                       | migrazione**, ma      |                       |
|                       | **più impegnative**   |                       |
|                       | dal punto di vista    |                       |
|                       | del **rischio** o     |                       |
|                       | della **complessità   |                       |
|                       | di esecuzione**       |                       |
+=======================+=======================+=======================+
| COME:                 | COME:                 | COME:                 |
|                       |                       |                       |
| 1. Identificare gli   | 1. Identificare gli   | 1. Per gli            |
|    applicativi che    |    applicativi che    |    applicativi        |
|    possono ottenere   |    possono cogliere   |    restanti,          |
|    maggiore beneficio |    beneficio          |    identificare le    |
|    dall’adozione del  |    dall’adozione del  |    strategie di       |
|    cloud con un       |    cloud con un       |    migrazione         |
|    rischio ridotto    |    rischio medio o    |    applicabili        |
|    per quanto         |    una semplicità di  |                       |
|    riguarda la        |    migrazione media   | 2. Identificare le    |
|    criticità dei      |                       |    strategie di       |
|    servizi che        | 2. Identificare le    |    migrazione         |
|    erogano e la       |    strategie di       |    applicabili        |
|    relativa           |    migrazione         |                       |
|    semplicità di      |    applicabili        | 3. Valutare le        |
|    migrazione         |                       |    competenze         |
|                       | 3. Valutare le        |    necessarie per     |
| 2. Identificare le    |    competenze         |    attuare le         |
|    strategie di       |    necessarie per     |    strategie          |
|    migrazione         |    attuare le         |    identificate       |
|    applicabili        |    strategie          |                       |
|                       |    identificate       | 4. Effettuare la      |
| 3. Valutare le        |                       |    migrazione al      |
|    competenze         | 4. Effettuare la      |    miglior rapporto   |
|    necessarie per     |    migrazione al      |    costi/benefici e   |
|    attuare le         |    miglior rapporto   |    validarne il       |
|    strategie          |    costi/benefici e   |    risultato          |
|    identificate       |    validarne il       |                       |
|                       |    risultato          |                       |
| 4. Effettuare la      |                       |                       |
|    migrazione al      |                       |                       |
|    miglior rapporto   |                       |                       |
|    costi/benefici e   |                       |                       |
|    validarne il       |                       |                       |
|    risultato          |                       |                       |
+-----------------------+-----------------------+-----------------------+

Per iniziare questo percorso, ovvero per identificare gli applicativi da
cui iniziare, pianificarne ed eseguirne la migrazione, suggeriamo di
seguire un approccio articolato in più step (da ripetersi poi in maniera
iterativa e incrementale come illustrato sopra):

1. **Lista degli applicativi e dei servizi attivi**: un primo passo che
   consiste nello stilare una lista degli applicativi attualmente in
   uso, ovvero sia gli applicativi utilizzati abitualmente che quelli
   con accessi saltuari o legati a specifiche necessità. L’obiettivo è
   di avere una visione d’insieme degli applicativi e i rispettivi
   servizi che l’amministrazione gestisce. Si consiglia di svolgere
   questa attività con il responsabile per la trasformazione digitale e
   i responsabili IT dell’amministrazione. Questa prima attività è
   presentata in dettaglio nel capitolo 3.1.1

2. **Prioritizzazione degli applicativi**: identificare gli applicativi
   candidati ad essere migrati nell’immediato classificandoli secondo
   quattro livelli che aiutano una valutazione orientata al valore
   generato, bilanciato rispetto al rischio potenziale ed alla
   difficoltà dell’operazione. L’obiettivo è di razionalizzare il
   panorama degli applicativi e identificare quelli prioritari da cui
   partire con la migrazione al cloud (se confermato dalle fasi
   successive a questa). Si consiglia di svolgere questa attività con il
   responsabile per la trasformazione digitale, il centro di competenza,
   l’unità di esecuzione, i responsabili IT dell’amministrazione,
   interloquendo con i responsabili dei servizi per la valutazione delle
   opportunità e dei rischi. Il framework di prioritizzazione è
   illustrato nel capitolo 3.1.2

3. **Scheda di assessment dell’applicativo**: approfondire gli aspetti e
   le caratteristiche tecnologiche e non degli applicativi identificati
   come prioritari attraverso la compilazione di una scheda di
   assessment. L’obiettivo è di raccogliere ad un sufficiente livello di
   dettaglio le informazioni necessarie a supportare un processo
   decisionale informato sulle possibili strategie da applicare, come
   descritto successivamente. Si consiglia di svolgere questa attività
   con il responsabile per la trasformazione digitale, il centro di
   competenza, l’unità di esecuzione e i responsabili IT
   dell’amministrazione interloquendo con i responsabili dei servizi per
   la valutazione dei bisogni dell’applicativo in analisi. A questa
   parte è dedicato il capitolo 3.2

4. **Identificazione delle strategie di migrazione possibili**:
   identificare quali strategie di migrazione, tra le sei possibili,
   siano più adatte per ciascun applicativo sulla base della scheda di
   assessment. L’obiettivo è di evidenziare le diverse opzioni
   disponibili prima di procedere con la scelta di quale adottare. Si
   consiglia di svolgere questa attività con il responsabile per la
   trasformazione digitale, il centro di competenza, l’unità di
   esecuzione e i responsabili IT dell’amministrazione ed eventuali
   fornitori. Le strategie di migrazione sono trattate nel capitolo 4.1

5. **Analisi costi-benefici**: per ciascuna delle strategie di
   migrazione identificate come possibili per l’applicativo effettuare
   un’analisi costi-benefici per valutarne l’opportunità. L’obiettivo è
   identificare il modello cloud migliore in base al contesto e alle
   circostanze in cui l’amministrazione si trova. Si consiglia di
   svolgere questa attività con il responsabile per la trasformazione
   digitale, il centro di competenza, l’unità di esecuzione e i
   responsabili IT dell’amministrazione. Come svolgere un’analisi
   costi-benefici è spiegato nel capitolo 3.3

6. **Valutazione delle competenze**: uno dei fattori cruciali per il
   successo di un processo di migrazione sono le competenze necessarie.
   Attraverso uno strumento di assessment delle competenze stimoliamo la
   riflessione sulle competenze necessarie rispetto a quelle
   disponibili, coprendo non solo l’ambito tecnologico ma tutti quelli
   che possono essere necessari per il successo del processo di
   migrazione. Si consiglia di svolgere questa attività con il
   responsabile per la trasformazione digitale, il centro di competenza,
   l’unità di esecuzione e i responsabili IT dell’amministrazione. Per
   evitare il rischio lock-in, l’amministrazione deve prendersi carico
   delle responsabilità e delle competenze rispetto sia al centro di
   competenza che ad eventuali fornitori. Questo step comprensivo di
   pianificazione delle competenze e degli aspetti ad esse connessi è
   trattato nelle sezioni 4.2 e 4.4

7. **Scelta della strategia e pianificazione della migrazione**: sulla
   base delle considerazioni fatte con l’analisi costi-benefici e la
   valutazione delle competenze scegliere quale strategia di migrazione
   effettivamente usare. L’obiettivo è di prendere una decisione
   informata e pianificare in maniera adeguata la migrazione. Si
   consiglia di svolgere questa attività con il responsabile per la
   trasformazione digitale, i centri di competenza, l’unità di
   esecuzione, i responsabili IT dell’amministrazione ed eventuali
   fornitori. Le strategie di migrazione e gli altri aspetti da prendere
   in considerazione una volta scelta la strategia di migrazione (ad es.
   SLA richiesti ai fornitori, come evitare il rischio lock-in) sono
   trattati nel capitolo 4

8. **Esecuzione della migrazione**: ovvero il passo cruciale durante il
   quale si esegue l’effettiva migrazione dell’applicativo a più alta
   priorità. In questa fase sarà fondamentale il supporto del centro di
   competenza, in quanto aggregatore di conoscenza quindi in grado sia
   di ricoprire un ruolo di advisor per l’amministrazione durante il
   processo che di consolidare la conoscenza che l’amministrazione
   acquisisce per condividerla poi con l’unità di controllo. Si
   consiglia pertanto di coinvolgerlo continuamente durante l’esecuzione
   della migrazione, insieme al responsabile per la trasformazione
   digitale, ai responsabili IT e ai fornitori. All’esecuzione della
   migrazione sono dedicati due interi capitoli, il 5 e il 6

9. **Check dei risultati**: l’ultimo step riguarda la riflessione sui
   risultati raggiunti e sull’impatto generato dall’operazione di
   migrazione. L’obiettivo è di valutare i progressi fatti e il valore
   ottenuto migrando al cloud anche calcolando e interpretando alcuni
   indicatori di risultato. Si consiglia di svolgere questa attività con
   il responsabile per la trasformazione digitale, il centro di
   competenza e i responsabili IT dell’amministrazione. Gli indicatori
   di risultato post-migrazione sono approfonditi nel capitolo 7

Una visione di alto livello dell’approccio con i macro-obiettivi e i
rispettivi step (attività) è rappresentata nella figura sotto.

|image1|

Una visione in dettaglio dell’approccio è invece rappresentata nelle
immagini seguenti, dove per ogni macro-obiettivo e per i rispettivi step
abbiamo evidenziato anche le persone da coinvolgere e il risultato
(output) atteso.

Primo macro-obiettivo:

|image2|

Secondo macro-obiettivo:

|image3|

Terzo macro-obiettivo:

|image4|

Quarto macro-obiettivo:

|image5|

Quinto macro-obiettivo:

|image6|

| In generale, migrare al cloud richiede un esercizio di gestione e
  orchestrazione del cambiamento che va oltre la semplice e diligente
  applicazione di strumenti e metodologie. Di questo bisogna essere
  coscienti ancor prima di iniziare. La complessità di questo processo
  di trasformazione è insita nella natura della sfida stessa, costituita
  da un insieme di fattori (tecnologia, persone, contesto, pratiche,
  ecc.) connessi tra loro e non separabili nè attaccabili separatamente.
  Una sfida complessa non può essere affrontata con un approccio
  analitico. Essa ha piuttosto bisogno di un approccio emergente e di
  una buona governance che affronti il problema nella sua interezza,
  considerando tutti i fattori coinvolti e osservando l’evoluzione nel
  tempo della relazione tra di essi a seconda della soluzione applicata.
| Di conseguenza, oltre a iniziare il viaggio seguendo un percorso
  predefinito per il fattore tecnologia, le pubbliche amministrazioni
  dovranno al contempo impegnarsi in attività che impattano sugli altri
  fattori correlati, ovvero sui processi, sulle persone e in generale
  sulla cultura dell’organizzazione.

Per esempio, nel Comune di Milano, dove questo percorso verso il cloud è
già stato iniziato, insieme ad una roadmap per migrare diversi servizi è
stato creato e promosso dalla Direzione Sistemi Informativi e Agenda
Digitale un programma di comunicazione per il cambiamento chiamato
“Innesco” per condividere a tutti i livelli nuovi modelli e strumenti
per ripensare la system integration e lo sviluppo applicativo secondo i
paradigmi moderni come quello cloud.

Sulla stessa linea, in Corte dei Conti, è stata introdotta una strategia
di comunicazione mirata a raccontare il valore dei nuovi applicativi su
cloud in maniera semplice e divertente tramite video e animazioni
inviati a tutti i dipendenti con una newsletter settimanale.

.. |image0| image:: ./media/image2.png
   :width: 6.53213in
   :height: 1.02099in
.. |image1| image:: ./media/image9.png
   :width: 6.59167in
   :height: 3.22222in
.. |image2| image:: ./media/image14.png
   :width: 2.80208in
   :height: 3.51389in
.. |image3| image:: ./media/image12.png
   :width: 2.82292in
   :height: 3.65278in
.. |image4| image:: ./media/image13.png
   :width: 3.95833in
   :height: 3.65278in
.. |image5| image:: ./media/image1.png
   :width: 2.41667in
   :height: 3.65278in
.. |image6| image:: ./media/image3.png
   :width: 2.32292in
   :height: 3.65278in
