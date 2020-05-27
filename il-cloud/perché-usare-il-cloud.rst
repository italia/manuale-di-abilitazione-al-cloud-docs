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

Molti cloud service provider (CSP) offrono un’ampia gamma di metodi,
tecnologie e controlli che rafforzano la sicurezza complessiva, grazie
alla protezione dei dati (che possono essere criptati con i più alti
livelli di sicurezza del mercato), dell’applicazione e dell’
infrastruttura da minacce potenziali. I CSP
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

I CSP offrono anche
servizi specifici di disaster recovery (vedi capitolo 5.3.10), che
permettono di ripristinare più rapidamente i sistemi IT maggiormente critici
senza sostenere le spese di un secondo sito fisico. Questo migliora la
continuità operativa dell’infrastruttura e mitiga il rischio di
perdita di dati. Inoltre, le applicazioni cloud mettono solitamente
a disposizione strumenti di auditing e controllo
delle informazioni che consentono di intervenire puntualmente in caso
di problemi.

Certamente la responsabilità finale della sicurezza e dell'integrità
dei dati è sempre dell'amministrazione:
gli strumenti cloud possono semplificare
la stesura e la messa in campo di piani di sicurezza e continuità operativa
ma non li sostituiscono.

Non basta dotarsi di soluzioni cloud per assicurare privacy
ai propri utenti e sicurezza delle infrastrutture e servizi IT, bensì
serve un processo continuo di vigilanza e controllo che
agisca trasversalmente su tutte le aree di interesse
fin dalla prima fase di progettazione dei servizi;
e che sia costantemente aggiornato rispetto allo
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
