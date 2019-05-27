**3.4 Migrazione delle licenze software in cloud**
==================================================

Le licenze sono un aspetto da considerare con attenzione nella
migrazione al cloud in quanto riguardano diversi ambiti: sistemi
operativi, application server, database, strumenti e molto altro.

Gli accordi di licenza definiscono come il software di un fornitore può
essere utilizzato da un’organizzazione. La maggior parte di questi però
è stata scritta quando gli ambienti IT tipici erano costituiti da PC
desktop e server fisici di vari tipi, tutti di proprietà e gestiti dal
cliente. I data center disponevano di rack pieni di server per singole
applicazioni, ognuna con il proprio storage collegato. Negli ultimi due
decenni la sala server si è però evoluta attraverso la virtualizzazione
dei server stessi, fino alla virtualizzazione dell'intera infrastruttura
di calcolo. Allo stesso modo, l’utilizzo dei servizi da parte degli
utenti finali si è evoluto passando dalla fruizione su un singolo
dispositivo per utente a potenzialmente più dispositivi (laptop,
desktop, tablet, dispositivo mobile) per ogni utente.

Gli accordi di licenza a loro volta sono cambiati per tenere conto di
questo panorama in evoluzione. Tramite i diritti di utilizzo secondari
ad esempio, si consente l'uso del software in maniera non simultanea su
un desktop e un laptop, o, con la trasformazione sempre più verso
abbonamenti per utente, si consente l'implementazione su dispositivi
illimitati.

Nel mondo dei data center c'è stata un'evoluzione, per tenere conto
delle macchine virtuali e quindi dei processori ad alta densità di core.
Gran parte del software server side è ora concesso in licenza “per core”
o su base utente nominativa. In alcuni casi è stato anche interrotto il
collegamento tra l'hardware fisico sottostante e il software eseguito su
di esso. È stato concesso il diritto di spostare il software in modo
dinamico, solitamente a un costo aggiuntivo o con alcune restrizioni ed
alcuni fornitori stanno iniziando ad affrontare le sfide di licenza
presentate dalla containerizzazione.

I modelli di licenza del software sono dunque in costante evoluzione, al
passo con il corrispondente panorama tecnologico e, come parte
integrante del piano di migrazione al cloud, è compito delle
organizzazioni verificare se le licenze utilizzate on-premise possano
essere trasferite o convertite in licenze cloud o meno.

Abbiamo illustrato le diverse tipologie di licenze on-premise e open
source nel capitolo 3.1. Di seguito parleremo delle tipologie di licenze
cloud e di alcuni accorgimenti necessari quando si considera la
migrazione di un applicativo sotto licenza da on-premise al cloud.

**3.4.1 Tipologie di licenze cloud**
------------------------------------

Vi sono diverse tipologie di licenze cloud:

-  **licenza ad abbonamento**: permette di pagare per l’utilizzo del
   software o servizio per un determinato periodo di tempo con anche la
   possibilità di annullare in qualsiasi momento l’abbonamento.Questo
   tipo di licenze vengono solitamente fornite su periodi mensili o
   annuali. Pagando mensilmente si ha una maggiore flessibilità potendo
   scegliere se mantenere o meno il servizio attivo. Il pagamento di una
   licenza annuale può però portare a significativi risparmi sui costi.
   Molti fornitori consentono inoltre di iniziare con una licenza
   mensile per poi passare a una licenza annuale proporzionale, fornendo
   così una sorta di periodo di prova. Questo tipo di licenza è molto
   comune tra i fornitori di servizi SaaS.

-  **licenza per utilizzo** (**pay-as-you-go**): la tecnologia ha
   permesso ai fornitori di avere accesso a strumenti avanzati che gli
   permettono di monitorare accuratamente l'utilizzo dei loro software e
   servizi, aprendo la porta a un diverso tipo di licenza: per utilizzo
   o pay-as-you-go. Con questo tipo di licenza si paga sulla base della
   quantità del sistema che si utilizza. Vi sono diverse modalità di
   misurazione del consumo, come ad esempio:

   -  Numero di processi eseguiti sul server del fornitore

   -  Quantità di spazio su disco utilizzato

   -  Dimensione del database e / o numero di query effettuate

Questo tipo di licenza consente di iniziare con il numero di risorse
necessarie e di scalare con la crescita con l’assunzione che se viene
usato maggiormente il software o l'hardware, è perché si sta crescendo e
l’investimento maggiore è quindi giustificato. Un ultimo aspetto di
questa licenza è che consente ai venditori di monitorare l'utilizzo su
tutti i dispositivi, eliminando il problema, sia per il cliente che per
il fornitore, di provare a concedere in licenza il software su ciascun
dispositivo separatamente.

-  **licenza per istanza** (**pay-by-instances**): questo modello di
   licenza si applica principalmente ai servizi cloud IaaS e PaaS. In
   questo scenario, si paga per ogni server o istanza di macchina
   virtuale che il fornitore esegue. Questo modello di licenza offre
   molti dei vantaggi della licenza per utilizzo perché si paga solo ciò
   di cui hai bisogno e si utilizza. Risulta un modello di licenza molto
   conveniente soprattutto quando si debbono creare istanze per provare
   qualcosa o mostrare dei prototipi per i quali non sarà poi più
   necessario mantenere attiva l’istanza.

-  **Bring Your Own License** (**BYOL**): come visto in precedenza, vi
   sono varie licenze utilizzabili on-premise e una cosa in comune a
   tutte queste è il concetto di proprietà dell’hardware su cui vengono
   fatti girare gli applicativi. In cloud però non si possiede
   l'hardware, non si ha idea su quale server sia in esecuzione il
   software licenziato ed esistono dinamiche come la capacità di
   assegnare nuove risorse hardware in modo dinamico in caso di traffico
   in eccesso. Vi è quindi una nuova esigenza relativa a come
   assicurarsi di rispettare i requisiti di licenza relativi a
   territorio, calcolo e proprietà nel cloud. La risposta dei venditori
   è stata (in alcuni casi) consentire l’utilizzo delle licenze
   on-premise su infrastruttura cloud dedicata come istanze dedicate,
   host dedicati e istanze riservate. Le istanze dedicate possono essere
   utilizzate laddove la licenza consenta l’utilizzo per macchina
   virtuale mentre gli host dedicati forniscono la conformità per il
   software concesso in licenza per host fisico. Le istanze riservate
   possono essere utilizzate per ridurre potenzialmente i costi nel
   tempo - offrono infatti uno sconto in cambio di un impegno a lungo
   termine (come 12 mesi). Poiché il server è dedicato, viene
   considerato come un'estensione del data center on-premise dal punto
   di vista delle licenze. Sebbene questo tipo licenze possano
   consentire l'utilizzo di software esistenti on-premise in cloud, è
   solitamente necessario pagare un costo aggiuntivo. Oltre a questo
   costo è importante considerare anche l'aspetto relativo al rischio.
   La proprietà delle licenze infatti rimane e con essa la
   responsabilità di garantire la conformità in caso di processi di
   audit. Ad esempio, è necessario assicurarsi che le licenze
   precedentemente utilizzate on-premise siano ora utilizzate solo nel
   cloud.

**3.4.2 Gestione delle licenze per la migrazione al cloud**
-----------------------------------------------------------

La gestione delle licenze in una prospettiva che privilegi la migrazione
al cloud deve seguire questi approcci:

-  Le licenze in scadenza vanno considerate con priorità per la
   migrazione ad una soluzione cloud-based (applicativo “opportunità da
   cogliere”) e le licenze mantenute attive solo il tempo minimo
   necessario a completare la migrazione

-  Le licenze ad uso perpetuo vanno considerate per BYOL se possibile o
   per la dismissione ed il passaggio ad una soluzione cloud con la
   relativa licenza. In caso vi siano investimenti significativi in
   ammortamento è necessario definire un termine per la dismissione
   della licenza e pianificare la migrazione in modo che il sistema in
   cloud sia disponibile e pienamente operativo per quel termine

-  | I software
     `middleware <https://it.wikipedia.org/wiki/Middleware>`__
     on-premise sotto licenza come ad esempio gli application server o
     DBMS sono tipicamente sfruttati da più di un applicativo. Questi
     componenti non vengono migrati immediatamente in quanto sono
     necessari a tutti quegli applicativi ancora on-premise e in attesa
     di migrazione.
   | Il risultato è una situazione ibrida in cui è necessario mantenere
     attivi sia i middleware on-premise che i middleware, o loro
     alternative, in cloud.
   | Oltre che l’impatto sulla gestione, questa duplicazione di ambienti
     anche se temporanea comporta un costo relativo alle licenze per le
     quali è dunque importante considerare bene l’impatto sul costo
     della migrazione ed eventuali accordi possibili con i fornitori di
     servizi su tipologie di licenze ibride.
