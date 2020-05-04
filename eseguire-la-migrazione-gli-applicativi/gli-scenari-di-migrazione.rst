5.4 Gli scenari di migrazione
=============================

5.4.1 Virtualizzazione
----------------------

La virtualizzazione consiste nell'eseguire un'istanza virtuale
di un sistema informatico attraverso un livello che astrae l'hardware fisico.
Su un unico server fisico (host) è possibile eseguire più sistemi operativi con relative librerie e applicazioni. 

La virtualizzazione offre isolamento mantenendo i programmi in
esecuzione all'interno di una macchina virtuale al sicuro dai processi
che si svolgono in un'altra macchina virtuale sullo stesso host.

La virtualizzazione permette di applicare la strategia di migrazione
di Re-host (“Lift and Shift” ) indicata nella sezione 4.1.4.
Questa strategia è particolarmente
adatta a migrare un’applicazione legacy su una piattaforma cloud in
quanto, invece di spostare progressivamente e separatamente nel tempo
i componenti di un applicativo, sposta l’intero ambiente in un colpo solo,
con tutto l’insieme di complesse dipendenze.

Le principali fasi di una migrazione Re-host sono:

1. identificare le macchine virtuali da migrare

2. identificare i prerequisiti come il sistema operativo che può essere
   supportato nel cloud computing (Linux o Windows)

3. controllare l'elenco dei formati di immagine che sono supportati in
   cloud (formato raw, VHD, VMDK)

4. per iniziare e condurre la migrazione, è necessario installare gli
   strumenti cloud-cli (command line interface), tipicamente forniti dal
   cloud provider, sulla macchina su cui risiedono le immagini di
   origine

5. preparare le macchine virtuali ed esportare le macchine virtuali dal
   loro ambiente virtuale

6. prevedere i tempi di downtime, informare tutte le parti interessate e
   pianificare temporalmente l’attività

7. importare l'immagine della macchina virtuale in cloud e controllare
   lo stato dell'importazione. Una volta che l'importazione è stata
   eseguita correttamente, avviare le macchine virtuali in cloud e
   verificare lo stato dell'istanza

5.4.2 Containerizzazione
------------------------

La containerizzazione è un tipo di strategia di virtualizzazione che è
emersa come alternativa alla virtualizzazione tradizionale basata su
`hypervisor <https://it.wikipedia.org/wiki/Hypervisor>`__.

Come per quest'ultimo, la virtualizzazione basata su container prevede
la creazione di parti virtuali specifiche di un'infrastruttura hardware,
ma a differenza dell'approccio tradizionale, che divide completamente
queste macchine virtuali dal resto dell'architettura, la
containerizzazione crea solo contenitori separati a livello di sistema
operativo. Nella containerizzazione, il sistema operativo è condiviso
dai diversi contenitori anziché clonato per ogni macchina virtuale.

La soluzione open source
`Docker <https://it.wikipedia.org/wiki/Docker>`__ offre una piattaforma
di virtualizzazione dei contenitori che si presta come buona alternativa
agli approcci basati su hypervisor.

La containerizzazione delle applicazioni è un metodo di virtualizzazione
a livello di sistema operativo utilizzato per distribuire ed eseguire
applicazioni distribuite senza avviare un'intera macchina virtuale per
ogni app. Più applicazioni o servizi isolati vengono eseguiti su un
singolo host e accedono allo stesso
`kernel <https://it.wikipedia.org/wiki/Kernel>`__ del sistema operativo.

I container funzionano su sistemi bare-metal, istanze cloud e macchine
virtuali, su Linux, Windows e Mac, permettendo la portabilità di
un’immagine da un sistema all’altro senza variazioni.

I container di applicazioni includono i componenti di runtime, ad
esempio file, variabili di ambiente e librerie, necessari per eseguire
il software desiderato. I container di applicazioni consumano meno
risorse di una distribuzione comparabile su macchine virtuali perché i
contenitori condividono risorse senza un sistema operativo completo per
supportare ciascuna app. L'insieme complessivo di informazioni da
eseguire in un container è l'immagine. Il motore del container
distribuisce queste immagini sugli host.

La containerizzazione delle applicazioni funziona con microservizi e
applicazioni distribuite, poiché ogni container opera indipendentemente
dagli altri e utilizza risorse minime dall'host. Ogni microservizio
comunica con gli altri attraverso le API delle applicazioni, con lo
strato di virtualizzazione del contenitore in grado di scalare i
microservizi per soddisfare la crescente domanda di un componente
dell'applicazione e distribuire il carico.

Questa configurazione incoraggia anche la flessibilità. Ad esempio, se
uno sviluppatore desidera una variazione dall'immagine standard, può
creare un contenitore che contiene solo la nuova libreria. Per
aggiornare un'applicazione, uno sviluppatore apporta modifiche al codice
nell'immagine del contenitore, quindi esegue il re-deploy dell'immagine
per l'esecuzione sul sistema operativo host.

La containerizzazione offre una serie di vantaggi:

-  piattaforma multi-cloud: uno dei principali vantaggi dei container è
   che possono operare su diverse piattaforme di cloud provider, creando
   una piattaforma multi cloud

-  condivisione dello stesso sistema operativo: i container condividono
   lo stesso kernel del sistema operativo dell'host. Pertanto, i
   container possono essere più efficienti di una VM che richiede
   l'esecuzione di un sistema operativo separato

-  test e CI / CD: i container mantengono invariato l’ambiente di
   esecuzione di un’applicazione in tutti i suoi passaggi ad ambienti
   diversi come tipico per approcci di continuous integration e
   continuous deploy

-  portabilità: i container hanno una portabilità migliore rispetto ad
   altre tecnologie di hosting. Possono muoversi verso qualsiasi
   sistema. La configurazione del container è anche portatile in quanto
   è solo un file da condividere

-  versionamento: questa è una delle parti più importanti del ciclo di
   sviluppo del software. Docker offre il controllo della versione che
   semplifica il ripristino a un'immagine precedente se si interrompe
   l'installazione

-  costo: i container sono anche economici. Nonostante gli investimenti
   in memoria, CPU e storage, è possibile supportare molti container
   sulla stessa infrastruttura

-  velocità: i container girano più velocemente delle macchine virtuali,
   il che è molto importante per le applicazioni distribuite

I container consentono di suddividere le applicazioni in microservizi
più piccoli e gestibili. Ogni microservizio è autosufficiente e può
essere modificato e aggiornato da solo senza la necessità di toccare gli
altri servizi. Ad esempio, se è necessario effettuare un aggiornamento,
è necessario modificare e compilare solo i servizi interessati anziché
ricompilare l'intera applicazione.

`Kubernetes <https://kubernetes.io/>`__ può essere utilizzato per
gestire (tecnicamente detto “orchestrare”) questi singoli servizi. Per
sfruttare tutti i vantaggi dei container e di Kubernetes, valutare le
applicazioni legacy per capire se possono essere suddivise in moduli:
non tutte le applicazioni legacy possono essere suddivise in moduli più
piccoli.

I seguenti passaggi possono aiutare nella valutazione:

-  non aggiungere altro alle applicazioni legacy. Iniziare da zero,
   riscrivendo anche le applicazioni legacy nell'architettura dei
   microservizi, è sicuramente una scelta valida, soprattutto se è stata
   presa la decisione di adottare completamente i container

-  se le applicazioni legacy non possono essere scomposte in moduli, la
   cosa più semplice da fare potrebbe essere semplicemente racchiudere
   l'applicazione in un unico contenitore

-  la semplice suddivisione delle applicazioni in container non le rende
   automaticamente scalabili. È necessaria una pianificazione adeguata
   per determinare come devono essere eseguiti questi singoli container.
   Kubernetes crea container dentro a
   `pod <https://kubernetes.io/docs/concepts/workloads/pods/pod/#what-is-a-pod>`__
   ed offre un
   `DaemonSet <https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/>`__,
   che è un modo automatico per creare pod di contenitori man mano che
   vengono aggiunti più nodi server. L'utilizzo di tali funzionalità per
   scalare con i microservizi deve essere considerato in anticipo

5.4.3 Ristrutturare l’applicativo
---------------------------------

La ristrutturazione di un applicativo per renderlo più adatto a
sfruttare le potenzialità delle piattaforme cloud può essere fatta a
diversi livelli di profondità:

-  riducendo le dipendenze da sistemi esterni

-  sostituendo componenti con le versioni cloud native

-  riprogettando le strutture interne dell’applicativo e trasformandolo
   per assumere un’architettura più idonea ad un’efficace erogazione del
   servizio associato

Qualunque sia lo scenario che motiva la modifica a livello di codice
sorgente dell’applicativo è opportuno seguire dei principi moderni di
progettazione del software che aiutino quest’ultimo ad essere sempre più
adattabile alle continue evoluzioni del bisogno degli utenti e del
servizio associato.

In accordo con le `linee
guida <https://carta-dei-principi-tecnologici-del-procurement.readthedocs.io/it/latest/>`__
definite dal Codice dell’Amministrazione Digitale e dal Piano Triennale,
l’obiettivo è quello di sviluppare servizi che:

-  soddisfino le esigenze degli utenti/cittadini

-  siano facilmente manutenibili

-  siano capaci di evolvere in base alle esigenze dei cittadini e al
   progresso tecnologico

-  siano indipendenti da singole componenti architetturali di terze
   parti

-  diminuiscano le situazioni di dipendenza da un ristretto numero di
   fornitori (lock-in)

Affinché gli applicativi della Pubblica Amministrazione possano
sfruttare i benefici del cloud è necessario che adottino principi di
progettazione moderni per:

-  ottenere architetture in grado di sfruttare appieno le potenzialità
   delle piattaforme cloud

-  considerare le differenze rispetto alla situazione on-premise

5.4.3.1 Basso accoppiamento
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Affinché gli applicativi della Pubblica Amministrazione possano
sfruttare i benefici del cloud è necessario che adottino architetture
moderne in linea con i principi secondo cui le piattaforme cloud
funzionano.

Uno delle architetture meno adatte all’uso in cloud è l’architettura
monolitica, in cui gli applicativi sono sviluppati e distribuiti come
una singola entità e:

-  crescono in complessità (n. di dipendenze interne\ **)** al crescere
   della ricchezza funzionale

-  richiedono il test dell’intera applicazione per la verifica d’impatto
   di un cambiamento

-  scalano l’intero sistema in modo uniforme anche a fronte di carichi
   localizzati

Architetture monolitiche non si prestano allo sviluppo di applicativi
complessi che devono evolvere rapidamente ed ottimizzare il consumo di
risorse e costi rispetto ai carichi da gestire.

Gli applicativi con architettura multi-tier sono nati come evoluzione
dei monoliti. Sono composti da diversi strati a livello di stack
tecnologico, ad es. nel caso 3-tier: uno strato di dati, uno strato di
logica di business e uno di interazione con l’utente con lo scopo di
permettere una gestione separata dei livelli riducendo la complessità
per ognuno di essi. Nonostante questa divisione, le applicazioni di
questo tipo aumentano di complessità con l’aumento della ricchezza
funzionale e presentano gli stessi svantaggi dei monoliti in termini di
scalabilità.

Per superare i limiti di architetture monolitiche e multi-tier, si è
cominciato a scomporre gli applicativi per funzionalità di business,
considerandoli una collezione di servizi piuttosto che un unicum. Questo
tipo di applicativi hanno un’architettura conosciuta come SOA (“Service
Oriented Architecture”) che offre vantaggi in termini di:

-  scalabilità, in quanto ogni servizio può essere scalato
   indipendentemente dagli altri

-  gestione, in quanto le dimensioni ridotte di ogni servizio rispetto
   all’applicativo complessivo permettono un alto livello di controllo
   sul funzionamento o sull’impatto di un cambiamento

-  interoperabilità, in quanto ogni servizio espone un contratto (API)
   con cui altri servizi (interni o esterni) possono utilizzarlo

Architetture ancora più moderne rispetto a SOA sono quelle a
microservizi e che utilizzano container. I vantaggi principali di queste
architetture sono:

-  la definizione di componenti indipendenti e di dimensioni
   molto-ridotte (micro-servizi) che semplificano il lavoro di più team
   sullo stesso codice sorgente abilitando l’ownership a livello di
   micro-servizio, il controllo sugli impatti dei cambiamenti
   (testabilità), l’ammodernamento attraverso sostituzione di un
   micro-servizio obsoleto ed un processo di build più efficiente in
   quanto a livello di singolo micro-servizio

-  la definizione di interazione attraverso API RESTful che rendono la
   realizzazione dei micro-servizi non vincolata all’utilizzo di un
   unico stack tecnologico e rafforzano la capacità del team di sviluppo
   a lavorare in parallelo sullo stesso sistema

-  l’astrazione rispetto all’ambiente di run-time (container) che riduce
   le componenti cui l’applicativo dipende direttamente

I servizi si sviluppano e distribuiscono in modo indipendente e sono più
facili da manutenere, correggere e aggiornare, garantendo funzionalità
più agili per rispondere ai cambiamenti.

Per sfruttare appieno i benefici del cloud, gli applicativi monolitici o
multi-tier devono evolvere verso (e i nuovi applicativi devono essere
sviluppati con) architetture moderne, da SOA a microservizi.

Le architetture moderne sono caratterizzate da un basso accoppiamento,
cioè una tecnica volta a massimizzare l’indipendenza tra i diversi
componenti applicativi attraverso l’uso di API.

5.4.3.2 Design for failure
~~~~~~~~~~~~~~~~~~~~~~~~~~

L’approccio “design for failure” richiede di progettare applicazioni in
modo che un malfunzionamento dell’applicativo causi solo un degrado
proporzionale alla funzionalità che non funziona ma non pregiudichi la
fruizione nel complesso dell’applicativo. Secondo questo principio,
devono essere rispettate precise linee guida per lo sviluppo e la
gestione dell’applicativo:

-  sfruttare i meccanismi di fault-tolerance della piattaforma cloud
   (per approfondimento a riguardo vedi sezione 5.2.1.2 - Disponibilità)

-  utilizzare più zone di disponibilità (località fisiche separate
   offerte dal provider) per proteggere le applicazioni e i dati da
   eventuali guasti del datacenter

-  implementare una strategia di backup e ripristino costante e
   automatico

-  evitare di sincronizzare copie “in-memory” di grandi quantità di dati
   da uno o più storage centrali all'interno degli applicativi:
   scalabilità e ridondanza dei sistemi, sono possibili anche grazie
   alla facilità con cui è possibile creare e distruggere istanze
   replica dell’applicativo ed in caso di storage “in-memory” la
   creazione di un’istanza forzerebbe ogni volta una nuova ed onerosa
   sincronizzazione che impatterebbe a sua volta sulle tempistiche di
   restore del servizio

-  creare e manutenere immagini per macchine virtuali o container che
   contengano tutte le dipendenze necessarie agli applicativi così da
   mitigare errori nelle procedure di rilascio dovuti a possibili
   dipendendenze esterne non più soddisfatte

-  configurare un dashboard di monitoraggio che permetta di identificare
   il punto di malfunzionamento in caso di fallimento o problema di
   performance
