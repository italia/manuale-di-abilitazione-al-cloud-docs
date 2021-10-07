5.3 Buone pratiche
==================

5.3.1 Scalabilità
-----------------

La scalabilità è la capacità di un applicativo di gestire i carichi di
operatività: è la possibilità di adattare le risorse, aumentandole o
diminuendole, in base al bisogno, on demand.

Le piattaforme cloud, in base al livello di integrazione di un
applicativo, forniscono un’esperienza di gestione più semplice, rapida e
mirata sia per incrementare le risorse quando il traffico lo richiede
che per ridurle quando la necessità non è più presente mentre in caso di
applicativi SaaS la gestione della scalabilità è demandata al fornitore
del servizio che se ne occupa in completa autonomia.

Applicativi in cloud si adattano meglio all’evoluzione dei bisogni del
servizio finale.

La scalabilità di un applicativo può essere:

-  | orizzontale, ovvero la capacità di supportare maggiore traffico
     aggiungendo ulteriori macchine all’insieme già attivo.
   | A seconda del livello di servizio offerto dal cloud provider sarà
     ad esempio possibile aggiungere e rimuovere macchine virtuali o
     container applicativi senza doversi occupare direttamente
     dell’infrastruttura sottostante, oppure, tramite i più avanzati
     servizi di autoscaling, fornire delle policy specifiche sulla base
     delle quali il CSP provvederà ad aumentare o ridurre il numero di
     macchine o container necessari così da garantire il livello di
     servizio desiderato.

-  verticale, ovvero la capacità di supportare maggiore traffico
   aggiungendo più risorse alle macchine già attive. La scalabilità
   verticale non rende un sistema fault tolerant: applicativi che
   funzionano utilizzando una singola macchina smettono di funzionare se
   quella macchina ha un down time. Anche in questo caso a seconda del
   livello di servizio offerto dal cloud provider sarà ad esempio
   possibile aumentare o ridurre risorse come CPU, memoria o storage
   riavviando gli applicativi o nei servizi più avanzati applicando una
   modifica a caldo, cioè senza dover riavviare.

5.3.2 Disponibilità
-------------------

La disponibilità di un applicativo è la sua capacità di essere
funzionante nel momento in cui vi è necessità di utilizzo. La
disponibilità si misura in uptime e le piattaforme cloud offrono
meccanismi innovativi per ottenere disponibilità molto elevate, prossime
al 100%.

La disponibilità di un applicativo è ottenuta con:

-  il deploy di più istanze per ogni servizio:

   -  i componenti dell’applicativo, meccanismo di autenticazione
      compreso, devono essere deployati su più istanze per evitare un
      unico punto di vulnerabilità, *single point of failure*

   -  almeno un’istanza per ogni componente (load balancer, application
      server, database) deve essere presente in *due zone differenti*

   -  se possibile, avere una capacità garantita in regioni separate,
      cioè aree territoriali formate da data center indipendenti tra
      loro, spesso suddivise a loro volta in zone di disponibilità
      fisicamente separate ma collegate tra loro da connessioni ad alta
      affidabilità, prestazioni e ridondanza;

   -  i dati devono essere replicati tra le region, se necessario, per
      avere un meccanismo di *failover*, ovvero la sostituzione della
      region non più funzionante con quella funzionante in caso di
      guasto o interruzione anomala

-  il deploy dell’applicativo su più region per evitare che, nel caso di
   un applicativo deployato in una sola region, se questa diventa
   indisponibile anche l’applicativo è indisponibile, impattando
   l’uptime degli SLA

-  testando ed automatizzando il deploy utilizzando tool e scripts che
   aggiornano e validano la configurazione ed automatizzano il
   deployment. Anche gli aggiornamenti devono essere realizzati in modo
   automatizzato. Assicurarsi di aver rafforzato e ristretto le
   politiche di deployment al fine di minimizzare i cambiamenti manuali
   apportanti da operatori.

5.3.3 Resilienza
----------------

La resilienza è la capacità di gestire i malfunzionamenti limitandone
l’impatto e gestendo il degrado in modo graduale e ripristinare
successivamente il corretto funzionamento del sistema.

Per ottenere servizi resilienti è cruciale:

-  Identificare i malfunzionamenti e ripristinare il corretto
   funzionamento in modo rapido ed efficace

-  isolare i componenti in modo che il malfunzionamento di uno non
   impatti gli altri

-  suddividere i servizi in gruppi, includendo in ogni gruppo tutti
   quelli necessari, ed allocare le risorse separatamente per ogni
   gruppo in modo che un malfunzionamento non impatti i servizi esterni
   allo specifico gruppo

-  includere i servizi necessari in un gruppo sulla base di requisiti
   tecnici o funzionali

La resilienza di un applicativo in cloud è superiore grazie a:

-  ridondanza

-  autoscaling, ovvero abilitando la disponibilità di un applicativo in
   più zone, l’autoscaling aiuta a dimensionare la capacità sulla base
   della richiesta effettiva:

   -  scaling policies (CPU, memoria)

   -  scaling programmato

-  monitoring per verificare che il comportamento corrisponda a quello
   atteso

-  replication, ovvero la possibilità di replicare i servizi importante
   per assicurarsi che sia disponibili in qualsiasi momento

La resilienza di un applicativo è ottenuta seguendo queste best
practice:

-  analizzare continuamente il sistema per identificare i
   malfunzionamenti, il loro impatto e le modalità di ripristino del
   funzionamento atteso

-  utilizzo di load balancer per distribuire il carico

-  utilizzo di più zone per la disponibilità

-  monitoraggio dello stato di salute delle dipendenze e degli endpoint

-  progettare il proprio applicativo secondo i principi del design for
   failure

-  preparare la documentazione per il failover ed il fallback, ovvero
   una soluzione alternativa nel caso quella principale non sia
   disponibile

5.3.4 Sicurezza 
----------------

Le piattaforme cloud, diversamente dalle soluzioni on-premise, sono
intrinsecamente caratterizzate dalla condivisione di risorse, ponendo
quindi maggiore criticità agli aspetti di sicurezza.

Problematiche come data leakage (ovvero trasmissione non autorizzata di
dati dall’interno di un applicativo ad un destinatario esterno), un
controllo debole degli accessi, attacchi DDoS, data breaches (ovvero
dati sensibili, protetti o riservati vengono consultati, copiati,
trasmessi, rubati o utilizzati da un soggetto non autorizzato), la
perdita di dati per errori o negligenza, la gestione delle identità e
della privacy devono essere tenute in forte considerazione.

Per mitigare questi rischi, le piattaforme cloud forniscono un insieme
di policy, controlli e regole che assieme proteggono l’infrastruttura
con misure specificatamente destinate alla sicurezza.

La sicurezza di un applicativo può essere migliorata seguendo queste
best practice:

-  mettere in sicurezza tutte le risorse, non solo quelle esposte verso
   l’esterno, *edge layer* (es. utilizzando una connessione TLS sicura
   anche nelle comunicazioni con altri applicativi)

-  proteggere i dati memorizzati, *data in rest*, in qualsiasi forma
   digitale (es. database, data warehouse, spreadsheet, archivi, nastri,
   backup, dispositivi mobile, ecc.) attraverso la criptazione

-  mitigare attacchi DDoS utilizzando il livello di network della
   piattaforma cloud;

-  utilizzare una lista di accessi sicuri per reti, applicativi e dati

-  eseguire un’analisi periodica delle vulnerabilità e i penetration
   test

-  utilizzare *two factor authentication* (2fa) e configurare un
   meccanismo di *single sign on* (SSO)

-  installare antivirus e anti-malware per i nodi e il networking

-  abilitare il monitoring ed il logging per il networking, gli
   applicativi ed i dati

-  connettere on-premise con cloud utilizzando sempre un link dedicato
   ed una VPN sul link pubblico

5.3.4.1 Sicurezza del dato
~~~~~~~~~~~~~~~~~~~~~~~~~~

Con la conservazione dei dati in cloud, è importante valutare il livello
di protezione dei propri applicativi e quali modifiche o controlli
debbano essere implementati per poter operare in sicurezza. A riguardo,
si consiglia di mettere in pratica le seguenti best practices:

-  criptazione dei dati prima di passare al cloud

-  criptazione dei dati memorizzati nei dischi utilizzando AES (Advanced
   Encryption Standards) 256

-  utilizzo del Key-Manager fornito dalla piattaforma cloud per la
   memorizzazione dei dati sensibili come credenziali, token per le API,
   certificati SSL, chiavi private

-  controllare gli accessi sulla base del ruolo degli utenti

-  proteggere tutti i canali di comunicazione con un certificato SSL

5.3.5 Data Privacy
------------------

I dati sono un aspetto molto critico per un’organizzazione e conservarli
in cloud impone l’adozione di misure per mantenerli sicuri e sotto il
proprio controllo visto che vengono effettivamente memorizzati in modo
distribuito su diverse macchine e sistemi di storage.

La data privacy viene garantita tramite questi aspetti:

-  data integrity, impedendo che persone o applicativi non autorizzati
   possano modificare o cancellare i dati. Questo può essere ottenuto
   attraverso l’implementazione di meccanismi di controllo degli
   accessi, sistemi di controllo delle versioni dei dati che impediscano
   la perdita del dato originale a seguito di modifiche o cancellazione,
   l’utilizzo di *checksum* per verificare l’integrità;

-  data confidentiality, proteggendo i dati contro l’accesso non
   autorizzato o il furto. Questo può essere ottenuto attraverso
   l’implementazione di meccanismi di controllo degli accessi e
   criptazione dei dati;

-  data availability, assicurando la disponibilità e l’accessibilità dei
   dati quando è necessario. Questo può essere ottenuto attraverso le
   misure disponibili in cloud come SLA per alta affidabilità,
   ridondanza e business continuity.

5.3.6 Autenticazione ed autorizzazione
--------------------------------------

L’autenticazione, l’autorizzazione e l’auditing in cloud permettono di
avere il controllo dell’applicativo quando questo è deployato in cloud.

L’autenticazione è il processo di conferma dell’identità di un utente in
cui l’applicativo determina chi sta accedendo in base all’utilizzo di
credenziali valide. Tipicamente l’autenticazione è fatta utilizzando
username e password, ma esistono altri metodi di autenticazione:

1. *Single Factor*: è il metodo di autenticazione più elementare,
   comunemente utilizzato per accedere un sistema come un sito web
   attraverso delle credenziali (es. username e password)

2. *Multi Factor:* è un metodo di autenticazione che fornisce l’accesso
   ad un utente solo dopo aver presentato con successo due o più
   dimostrazioni della propria identità sulla base di: conoscenza
   (qualcosa che l’utente e solo lo specifico utente sa), possesso
   (qualcosa che l’utente e solo lo specifico utente ha) e inerenza
   (qualcosa che l’utente e solo lo specifico utente è)

3. *Two Factor* (2FA)*:* conosciuto anche come verifica in due passaggi
   o autenticazione con doppio fattore, è un tipo, o un sottoinsieme di
   multi-factor authentication. È un modo di confermare l’identità
   dichiarata dagli utenti utilizzando la combinazione di due diversi
   fattori fra:

   a. qualcosa che loro conoscono

   b. qualcosa che loro posseggono

   c. qualcosa che sono

L’autenticazione con due fattori aggiunge un livello di sicurezza agli
applicativi rendendo più difficile ottenerne l’accesso per chi prova ad
attaccarli.

5.3.7 Interoperabilità
----------------------

Durante un processo di migrazione si deve considerare l’opportunità di
adeguare l’applicativo al 
“\ `Nuovo modello di
interoperabilità <https://www.agid.gov.it/it/infrastrutture/sistema-pubblico-connettivita/il-nuovo-modello-interoperabilita>`__\ ”
per renderlo più facilmente integrabile con gli altri enti.

Nel caso di strategia di migrazione re-purchase, ovvero nel caso di
acquisto di servizi SaaS, l’interoperabilità è un criterio che deve
essere preso in considerazione:
se il SaaS acquisito si interfaccia direttamente con altre amministrazioni,
deve farlo in conformità alle
`Linee guida sull'interoperabilità tecnica, <https://docs.italia.it/italia/piano-triennale-ict/lg-modellointeroperabilita-docs>`__
alternativamente l'ente dovrà sviluppare sopra il SaaS un livello di interoperabilità.

Tutti i servizi presenti sul `cloud
Marketplace <https://cloud.italia.it/marketplace/>`__
di AgID, la piattaforma che espone i servizi e le infrastrutture
qualificate, sono compatibili con altri
servizi e infrastrutture cloud dello stesso tipo mediante l’utilizzo di
standard aperti (ad esempio Open Virtualization Format) ed opportune
API.

Nel caso di strategia di migrazione re-platform, re-architect e/o per lo
sviluppo di nuovi applicativi cloud-native, invece, le Pubbliche
Amministrazioni devono seguire le
`Linee guida sull'interoperabilità tecnica. <https://docs.italia.it/italia/piano-triennale-ict/lg-modellointeroperabilita-docs>`__
che garantisce la
collaborazione tra le Pubbliche Amministrazioni e verso soggetti terzi.

5.3.8 Monitoraggio e alerting
-----------------------------

E’ essenziale che l’intera infrastruttura funzioni in modo efficiente e
che le risorse del cloud vengano utilizzate in modo efficace. Per questo
motivo, esistono tecniche di misurazione e controllo che permettono di
monitorare la stabilità e le prestazioni di un’infrastruttura.

Le metriche più usate si basano sia su dati degli applicativi (come
attività degli utenti) che su dati del sistema (come registro degli
eventi).

Soprattutto in ottica di infrastruttura e applicativi cloud, i
principali dati da monitorare sono:

-  Azioni fallite e riuscite eseguite dagli utenti

-  Disponibilità dell’applicativo

-  Performance dell’applicativo

-  Integrità dei file

-  Tentativi falliti e riusciti di accesso ai dati e alle risorse

-  Attività sospette e illecite

-  Informazioni di base sull’infrastruttura (CPU, RAM, disco, network,
   performance)

-  Costi (budget) del cloud provider scelto

Tra le varie metriche basate sui dati di cui sopra, ce ne sono tre
fondamentali da considerare per misurare la disponibilità,
l’affidabilità e la resilienza di un applicativo e valutare i rischi
connessi:

-  Tempo medio al guasto (conosciuto come MTTF, mean time to failure),
   che misura il tempo medio del verificarsi di un guasto o
   malfunzionamento del sistema, ovvero il tempo medio di uptime

-  Tempo medio tra i guasti (conosciuto come MTBF, mean time between
   failures), che misura il tempo medio di attesa tra un guasto e il
   successivo

-  Tempo medio di ripristino (conosciuto come MTTR, mean time to
   repair), che misura il tempo necessario a riparare un componente o
   una parte guasta del sistema

Per la scelta di un sistema di monitoraggio, si consiglia di:

1. Analizzare l’infrastruttura e definire i requisiti di monitoraggio
   per il proprio ambiente e applicativo

2. Allocare un budget specifico per il monitoring e comparare i costi
   delle soluzioni offerte sul mercato per trovare la soluzione che
   soddisfa i requisiti di funzionalità e di budget

3. Eseguire un test pilota del sistema di monitoraggio su un applicativo
   per verificare le funzionalità in uno scenario reale

In generale, un sistema di monitoraggio deve essere semplice da usare e
fornire una chiara visualizzazione delle informazioni, che devono essere
rese immediatamente esplicite.

I sistemi di monitoraggio disponibili sul mercato sono solitamente
strumenti:

-  offerti da terze parti, ovvero da fornitori di hardware e software,
   che hanno soluzioni di monitoraggio compatibili con i loro prodotti

-  offerti dai cloud provider, che includono il pacchetto di
   monitoraggio come parte delle loro soluzioni SaaS

-  open source, ovvero soluzioni di monitoring create dalla comunità,
   che possono essere usate senza pagare alcun costo

Il sistema di alerting (o di allarme), invece, è un meccanismo che
genera messaggi specifici ad uno stato del sistema e li recapita ad un
determinato destinatario.

L’alerting è un servizio trasversale rispetto al monitoraggio ed è per
questo spesso offerto direttamente dai sistemi di monitoraggio. Nella
maggior parte dei casi, è perciò importante configurare i criteri di
avviso all’interno del sistema di monitoraggio per ricevere notifiche
quando si verificano eventi particolari o quando certe metriche violano
le regole definite.

Esempi di notifiche da configurare in ottica cloud possono essere:

-  violazione di una policy delle attività ammesse sul sistema

-  violazione di una policy sui file

-  utenza compromessa nel caso ci sia un’alta probabilità che un’utenza
   sia stata utilizzata in modo non autorizzato

-  nuovo utente amministratore

-  nuovo luogo di accesso per un amministratore

5.3.9 Automazione
-----------------

Come anticipato nel capitolo 5.1, le pratiche
`DevOps <https://developers.italia.it/it/devops/>`__ rispondono
all'interdipendenza tra sviluppo software e IT operations, ed aiutano
un'organizzazione a sviluppare e gestire in modo più rapido ed
efficiente prodotti e servizi software. L’obiettivo è quello di `creare
una
cultura <https://www.digital4.biz/white-paper/forrester-6-tendenze-che-influenzeranno-le-strategie-devops-nei-prossimi-anni_43672157144.htm?__hstc=212895371.9f4238a62197b7846b6fd32be7828223.1552386161803.1553187821467.1553536660708.8&__hssc=212895371.1.1553536660708&__hsfp=916113050>`__
in cui la consegna del software possa avvenire in maniera veloce,
frequente e affidabile, utilizzando l’automazione ove possibile.

L’automazione aumenta la ripetibilità di operazioni critiche e permette
di accelerare i processi di delivery, di ridurre al minimo la
possibilità di errori o cattive configurazioni aumentando il controllo
sui processi. Tutto ciò che viene coinvolto dall’automazione
(infrastruttura, ambiente, configurazione, piattaforma, build, test,
processo, ecc.) dev’essere definito sotto forma di codice.

I processi che più beneficiano dall’automazione in cloud sono:

-  **provisioning dell’infrastruttura:** la grande elasticità
   dell’infrastruttura messa a disposizione dal cloud, che si traduce ad
   esempio con la possibilità di scalare ambienti da alcune macchine
   virtuali a centinaia sulla base del carico, porta con sé un costo
   operativo e un rischio di errore se legato a processi manuali.

Risulta quindi fondamentale tradurre questi processi sotto forma di
codice, così da applicarli una, dieci o mille volte in maniera
completamente automatica, creando degli script che permettano di
realizzare un ambiente con migliaia di macchine virtuali al mattino e
allo stesso tempo spegnerlo alla sera.

| È qui che entra in gioco una pratica denominata *infrastructure as
  code*, che consente appunto di gestire e fare provisioning delle
  risorse infrastrutturali necessarie tramite file di configurazione
  processabili automaticamente da strumenti specifici.
| I vantaggi principali di questa pratica sono:

-  riduzione del rischio di errore umano insito in un processo manuale

-  velocità e ripetibilità del processo

-  possibilità di fare `controllo di
   versione <https://it.wikipedia.org/wiki/Controllo_versione>`__ sul
   codice che rappresenta l’infrastruttura, così da avere uno storico
   dei cambiamenti

-  possibilità di riutilizzare script e configurazioni in ambienti e
   progetti diversi

-  possibilità di costruire pipeline di automazione che includano anche
   la parte infrastrutturale

-  esistenza di veri e propri registri con template di infrastrutture
   già pronti

-  | **distribuzione o deployment:** tramite l’utilizzo di strumenti
     specifici è possibile automatizzare i processi ripetibili che
     compilano, impacchettano, distribuiscono e configurano il software
     dell’applicativo per poi rilasciarlo su ambienti di test o
     produzione, creando le cosiddette pipelines di build e rilascio.
   | I vantaggi di questo approccio e del suo utilizzo in cloud sono:

   -  riduzione dei tempi di rilascio del software e di nuove
      funzionalità o correzioni di bug

   -  riduzione del rischio di errore umano insito in un processo
      manuale

   -  possibilità di integrare tutta una serie di test automatici che
      validino il software sotto vari aspetti, ad esempio funzionale o
      di sicurezza, per garantire il rilascio solo se tutti i pre
      requisiti sono rispettati

   -  integrazione di strumenti di continuous integration e deployment
      con i provider cloud

   -  possibilità di creare pipelines con servizi completamente gestiti
      dai provider cloud e con template pre-compilati presenti su
      marketplace appositi

-  | **gestione automatica dei disservizi:** la maggior parte dei
     provider cloud offre diversi servizi per il monitoraggio e logging
     dell’infrastruttura e degli applicativi, i quali espongono le
     informazioni sullo stato del sistema attraverso apposite API.
   | Questo permette di creare script con policy per la gestione
     automatica di situazioni critiche. Ad esempio è possibile creare
     script che reagiscono quando i tempi di risposta di un servizio
     superano una certa soglia, andando a scalare automaticamente le
     risorse in modo da distribuire il carico.
   | I benefici di questo approccio sono i seguenti:

   -  monitoring automatico dei livelli desiderati di servizio con
      generazione di alert in caso di valori fuori scala

   -  possibilità di creare script automatici che implementino azioni
      correttive o che informino gli amministratori di sistema per poter
      intervenire tempestivamente

   -  velocità di reazione ai problemi e conseguente risoluzione degli
      stessi

   -  possibilità di implementare policy per la gestione della sicurezza

5.3.10 Disaster recovery
------------------------

Un disastro è una situazione derivante da un evento, naturale o
provocato dall’uomo, per via della quale la capacità dell’organizzazione
di fornire servizi ai propri utenti è seriamente minacciata o
compromessa.

Una strategia di *disaster recovery* deve definire i possibili livelli
di disastro e identificare la criticità dei sistemi e delle
applicazioni, individuando quali di questi sono più o meno vitali per la
salvaguardia delle attività. Un piano di disaster recovery deve
stabilire sia misure preventive di sicurezza che misure correttive in
caso di emergenza. Inoltre, deve pianificare chiaramente le fasi per
ripristinare l’infrastruttura, i sistemi e i dati nel minor tempo
possibile e con il minimo sforzo da parte del team.

Il cloud computing porta un approccio completamente diverso al disaster
recovery: la virtualizzazione dei server, la disponibilità di data
center distribuiti in varie aree geografiche ed i servizi specifici per
il disaster recovery permettono un ripristino più rapido dei sistemi IT
più importanti senza sostenere le spese di un secondo sito fisico.

I piani di disaster recovery in cloud traggono molti benefici rispetto a
quelli tradizionali:

-  la virtualizzazione dei server e la containerizzazione degli
   applicativi permettono di includere tutto ciò che è necessario per il
   funzionamento in un singolo pacchetto software che può essere
   copiato, o di cui se ne può fare il backup, in un diverso data center
   e ripristinato in un tempo dell’ordine dei minuti riducendo
   significativamente i tempi di ripristino rispetto agli approcci
   tradizionali

-  i sistemi in cloud scalano in modo più semplice, sia in modo
   verticale che orizzontale

-  i costi sono legati all’utilizzo effettivo e non c’è necessità di
   investimenti iniziali

-  l’ampia banda e le alte prestazioni dei dischi per l’I/O solitamente
   disponibili sulle soluzioni cloud rendono il ripristino più rapido

-  possono sfruttare la ridondanza geografica (ovvero la replica dei
   contenuti su data center distribuiti) offerta dai cloud provider

-  i cloud provider offrono i loro servizi da diverse *region* del mondo
   permettendo la scelta del posto più appropriato per i propri bisogni
   di disaster recovery

Le diverse strategie di disaster recovery beneficiano significativamente
del cloud computing:

1. **backup e restore**: in cui si effettua il backup dei server
   virtualizzati o degli applicativi containerizzati ed i loro dati su
   un diverso data center o su una diversa *region* in cloud e, nel caso
   si verifichi la necessità e in base al disastro verificatosi, si
   ripristinano sullo stesso data center/region o su uno differente

2. **pilot light**: in cui si mantiene in cloud, in una *region* o data
   center differente, un ambiente funzionante ma con risorse minime dei
   componenti più critici (ad es. il database mantenuto allineato
   attraverso mirroring o replica) e, quando è necessario effettuare il
   recovery, si procede con il provisioning delle componenti non ancora
   attive ed a scalare il sistema in modo opportuno per supportare il
   traffico di produzione

3. **warm standby**: in cui si mantiene in cloud, in una *region* o data
   center differente, un ambiente pienamente funzionante ma con risorse
   minime di tutti i componenti e, quando è necessario effettuare il
   recovery, si procedere a scalare il sistema in modo opportuno per
   supportare il traffico di produzione

4. **soluzione multi-sito**: in cui si mantiene in cloud, in una region
   o data center differente, un secondo ambiente pienamente funzionante,
   dimensionato per supportare il traffico di produzione ed attivo nella
   ricezione di quest’ultimo

La strategia di *disaster* recovery più opportuna va definita in
funzione dei tempi di ripristino desiderati, della quantità di dati che
è accettabile poter perdere
(`RPO <https://it.wikipedia.org/wiki/Recovery_Point_Objective>`__) e dei
costi da sostenere per adottare le misure necessarie per ottenere tali
obiettivi.

5.3.11 Backup
-------------

Al fine di ridurre al minimo le perdite di informazioni in caso di
problemi inaspettati durante la migrazione al cloud, deve essere
implementata una comprensiva strategia di backup e ripristino, con test
periodici del ripristino per assicurarsi che quest’ultimo funzioni
correttamente.

La strategia di backup si articola su diversi aspetti, quali:

-  l’entità di cui si effettua il backup:

   -  backup dell’applicativo, ovvero della sua immagine

   -  backup del database, ovvero un backup dello schema del database e
      dei dati contenuti

-  la frequenza temporale:

   -  **giornaliero**, ovvero un backup incrementale dell’applicativo,
      che viene implementato utilizzando strumenti di pianificazione del
      backup ed eseguito ogni giorno sul cloud

   -  **settimanale**, ovvero un backup completo dell’applicativo
      (inclusivo di tutti i dati del progetto, compresi i repository dei
      software di gestione), che viene eseguito sul cloud

-  la quantità di dati salvati:

   -  **backup completo**: la più semplice e completa forma di backup
      che copia tutti i dati verso un dedicato sistema di
      memorizzazione. È semplice mantenere il versioning di backup
      completo, ma il tempo di esecuzione è crescente al crescere della
      quantità di dati da trattare

   -  **backup incrementale**: la copia dei soli dati che sono cambiati
      dal backup precedente sulla base del timestamp di modifica del
      file e della data dell’ultimo backup. Un backup incrementale è
      inferiore in dimensione rispetto ad uno completo e quindi occupa
      meno spazio nel dispositivo di memorizzazione e richiede minor
      tempo di esecuzione, per cui può essere pianificato più
      frequentemente. Al contempo, il recovery del sistema richiede più
      tempo in quanto tutte gli incrementi dall’ultimo backup completo
      vanno ripristinati e, se uno dei backup incrementali non è andato
      a buon fine, il ripristino è incompleto

   -  **backup differenziale**: la copia di tutti i file che sono
      cambiati rispetto all’ultimo backup completo. Questo approccio
      richiede meno spazio di memorizzazione rispetto al backup
      incrementale e per il restore sono necessari solo l’ultimo backup
      completo e quello differenziale, ma il tempo di esecuzione è
      superiore rispetto al backup incrementale

-  il periodo di conservazione dei dati:

   -  è importante definire una politica di conservazione dei dati che
      definisca i tempi minimi di mantenimento dei backup, oltre i quali
      è opportuno dismettere le informazioni in modo da liberare lo
      spazio di memorizzazione da loro utilizzato

   -  la politica di conservazione deve garantire il ripristino dei dati
      corretti e della giusta quantità di dati nel sistema in caso di
      perdita di dati

   -  la politica di conservazione deve trattare diversamente
      l’archiviazione dei dati dal backup dei dati: i dati archiviati
      non sono più attivamente in uso ma sono necessari per una
      conservazione di lungo periodo per consultazione o adeguamento
      alle normative. I dati archiviati sono memorizzati su dispositivi
      di memorizzazione più economici e devono essere semplici da
      ricercare

   -  per un’appropriata creazione e realizzazione della politica di
      conservazione il team IT ed il team legale devono collaborare, in
      quanto il team legale ha maggiore consapevolezza della durata per
      cui i dati devono essere conservati

   -  `object storage <https://en.wikipedia.org/wiki/Object_storage>`__
      sono, tra i servizi disponibili in cloud, utilizzati
      frequentemente per la conservazione sul lungo periodo dei dati in
      quanto risultano più economici di soluzioni on-premise e
      garantiscono una migliore protezione dei dati

   -  i dati sono in costante aumento non solo nei dispositivi di
      memorizzazione primari, ma anche in quelli di backup e di
      archiviazione. I dispositivi di backup rappresentano in
      particolare un aggravio economico quando la stessa informazione è
      salvata più volte. La definizione di una politica di conservazione
      dei dati è un modo per ridurre la dimensione dei backup ed,
      eventualmente, automatizzare la rimozione di alcuni insiemi di
      dati. Tuttavia, insiemi diversi di dati possono avere tempistiche
      di conservazione diverse, per cui una buona politica, volta ad
      ottimizzare occupazione e costi, deve considerare anche dove un
      certo insieme di dati debba essere conservato

Le procedure di backup e restore traggono vantaggio dall’essere
effettuate su una piattaforma cloud:

-  durabilità dei dati grazie alla ridondanza dei dispositivi di storage

-  flessibilità e scalabilità grazie alla possibilità di aumentare le
   risorse per il backup in pochi minuti

-  efficienze di costo grazie alle tariffe a consumo

-  sicurezza e compliance grazie al controllo degli accessi, la
   crittazione e gli strumenti di auditing

Per impostare la desiderata politica di backup è raccomandato l’utilizzo
degli strumenti dedicati offerti dal cloud service provider.
