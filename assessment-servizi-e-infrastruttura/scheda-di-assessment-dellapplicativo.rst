3.2 Scheda di assessment dell’applicativo
=============================================

Una volta identificati gli applicativi prioritari candidati alla
migrazione in cloud, si devono ora valutare in dettaglio gli aspetti e
le caratteristiche di ciascuno di essi per validarne l’opportunità
rispetto al rischio e poi scegliere la strategia di migrazione più
adatta (terzo step del processo presentato nel capitolo 2.3).

In particolare, gli obiettivi di questa seconda fase del processo sono:

-  ricostruire una conoscenza di base sugli applicativi che sono stati
   prioritizzati

-  evidenziare le informazioni utili (sia in ambito tecnico che di
   business) a supportare l’identificazione delle strategie di
   migrazione applicabili a ciascun applicativo

-  stimolare la comunicazione fra personale tecnico e non-tecnico per la
   decisione su quale strategia di migrazione sia più adatta a ciascun
   applicativo prioritizzato

Per facilitare il raggiungimento di questi risultati, abbiamo creato una
scheda di assessment dell’applicativo (vedi allegato “`Scheda di
assessment dell'applicativo <https://drive.google.com/open?id=1P8lcsCxEXKYk7oZVoHrS6rhNmqdPz4bHfzmsmWq4akQ>`_”) che l’amministrazione può compilare
seguendo le istruzioni riportate di seguito (ed esplicitate anche
direttamente sul foglio di lavoro).

In generale, la scheda di assessment dell’applicativo è stata pensata
per:

-  bilanciare sforzo e valore con un modello strutturato ma al contempo
   snello

-  stimolare valutazioni non abituali da fare in modo collaborativo

Le informazioni richieste non sono obbligatorie, ma la loro
specificazione aiuta a prendere decisioni più consapevoli. Le
informazioni temporaneamente non disponibili o di difficile recupero
possono essere tralasciate. I dati reali sono da privilegiare rispetto
alle stime se il loro recupero è sufficientemente agevole, altrimenti
stime basate sull’esperienza ed il buon senso possono assolvere al
medesimo obiettivo. Lo scopo non è la precisione e l’esaustività ma
evidenziare le tendenze e gli aspetti più critici.

Si consiglia di avvalersi del supporto e dell’esperienza dell’unità di
esecuzione e del centro di competenza per raccogliere le informazioni
migliori.

Vediamo ora insieme le diverse sezioni che compongono la scheda di
assessment e come compilarle.

3.2.1 Aspetti tecnologici
-----------------------------

Gli aspetti tecnologici sono quelle caratteristiche che distinguono
l’applicativo da un punto di vista tecnico e sui quali l’amministrazione
dovrà focalizzarsi per valutare come migrare l’applicativo. I campi da
riempire in questa sezione sono:

-  **Stack tecnologico**: componenti tecnologiche attualmente in uso, ad
   es. database usato e rispettiva versione, ambiente di runtime,
   sistemi di notifica, sistemi di gestione di code, web server

-  **Uso di componenti sostituibili con l'equivalente servizio
   cloud-native**: componenti on-premise utilizzate dall’applicativo che
   sono sostituibili con servizi gestiti dal cloud provider, ad es.
   database, LDAP, load balancer, SMTP server

-  **Dimensionamento delle componenti infrastrutturali**: componenti
   infrastrutturali attualmente in uso che garantiscono il corretto
   funzionamento dell'applicativo, ad es. # di server, dimensione dello
   storage, CPU, memoria (questa informazione aiuta in particolare a
   calcolare l’impatto economico che la migrazione al cloud
   dell’applicativo può avere)

-  **Utilizzo effettivo delle componenti infrastrutturali**: utilizzo
   effettivo delle risorse sulla base di misurazioni effettive o stime
   (questa informazione aiuta in particolare a dimensionare il cloud di
   destinazione e a calcolare l’impatto economico che la migrazione al
   cloud dell’applicativo può avere)

-  **Dipendenza dall'hardware fisico**: situazione attuale in cui
   l'applicativo si trova in termini di dipendenza dall’hardware fisico,
   specificando ad esempio se si usano macchine virtuali, container
   oppure se l'applicativo o parti di esso sono su macchine fisiche

-  **Misure di sicurezza**: minacce a cui l'applicativo è esposto,
   specificando quali componenti e dati sono più vulnerabili e
   richiedono protezione

-  **Sistemi on-premise da cui dipende**: sistemi on-premise interni ed
   esterni da cui l'applicativo dipende, ad es. IDP, LDAP, sistema di
   notifiche. Non devono essere inclusi qui i sistemi già in cloud, come
   le piattaforme abilitanti della PA (ad es. Spid, PagoPA)

-  **Sistemi on-premise che dipendono**: sistemi on-premise interni ed
   esterni che dipendono dell'applicativo, ad es. i sistemi che
   consumano i dati dell'applicativo

3.2.2 Vincoli tecnologici
-----------------------------

I vincoli tecnologici sono quegli aspetti tecnologici particolarmente
critici che hanno un ruolo stringente sulla scelta della strategia di
migrazione e sui quali l’amministrazione dovrà focalizzarsi per decidere
come effettivamente migrare l’applicazione. I campi da riempire in
questa sezione sono:

-  **Presenza di test di validazione**: presenza di test che possano
   validare le eventuali modifiche da effettuare sul codice sorgente per
   ridurre il rischio di regressione (ad es. test unitari, di
   integrazione, funzionali, performance). Per un approfondimento su
   questa tipologia di test vedi capitoli 5.5 e 6.4

-  **Modificabilità del codice sorgente**: livello di modificabilità del
   codice sorgente, che può essere:

   -  **nulla**, ovvero inesistente

   -  **parziale**, se il codice può essere parzialmente modificato ad
      es. influenzando le scelte evolutive del prodotto realizzato da
      terze parti

   -  **completa**, se il codice sorgente può essere completamente
      modificato ad es. in quanto se ne ha la proprietà o se la licenza
      del codice sorgente lo permette (ad es. open source)

-  **Disponibilità di documentazione tecnica**: disponibilità della
   documentazione tecnica che spiega il funzionamento interno
   dell'applicativo e delle sue componenti per intervenire in modo
   mirato e controllato. Per approfondimento sulla documentazione vedi
   capitolo 4.3.2.2

-  **Connettività minima necessaria**: impatto della connettività in
   termini di latenza ed ampiezza di banda, in relazione agli SLA che il
   fornitore deve garantire, sull'usabilità dell'applicativo. Si
   richiede di scegliere tra:

   -  **rete locale**, se l’accesso alla rete locale è un requisito
      vincolante all'usabilità di questo applicativo

   -  **internet**, se per l’applicativo l’accesso a internet è un
      requisito vincolante all'usabilità di questo applicativo

3.2.3 Dati
--------------

Ai dati è dedicata una sezione a parte in quanto rappresentano un
aspetto molto importante nel contesto di una migrazione (per
approfondimento sul tema vedi capitolo 6). I campi da riempire in questa
sezione sono:

-  **Dimensione della base di dati**: dimensione dei dati da migrare
   nell'unità di misura opportuna fra Byte, KB, MB, GB, TB, ecc.

-  **Frequenza di consultazione dei dati (annuale)**: ogni quanto i dati
   vengono consultati nell’arco di un anno

-  **Frequenza di aggiornamento dei dati (annuale)**: ogni quanto i dati
   vengono aggiornati nell’arco di un anno

-  **Ciclo di vita dei dati**: quantità di tempo dopo la quale il dato
   può essere considerato obsoleto e quindi eliminabile dal sistema.
   Seguire le indicazioni di data retention del GDPR laddove
   applicabili. Si consiglia qui, se ritenuto necessario, di
   differenziare per tipologia di dato

-  **Applicativi che trattano gli stessi dati**: applicativi che
   trattano gli stessi dati gestiti da questo applicativo (tutti o un
   sottoinsieme). In particolare, si fa riferimento a quegli applicativi
   che hanno una copia dell'insieme di dati considerato e che
   necessitano una sincronizzazione. Si consiglia di riportare in questo
   campo sia i nomi degli applicativi che il sottoinsieme dei dati
   trattati

3.2.4 Parti interessate
---------------------------

Le parti interessate sono tutte quelle persone e processi che, per
diverse ragioni, sono interessate nella migrazione dell’applicativo.
Alle persone l’amministrazione dovrà far riferimento per sapere chi
contattare nel caso di domande specifiche o considerazioni da fare sulla
migrazione dell’applicativo. Il campo da riempire in questa sezione è:

-  **Rappresentanti delle aree impattate**: persone da coinvolgere o da
   tenere informate sia perchè con potere decisionale, sia perché
   utilizzatrici dell'applicativo o perché impattate dalla migrazione.
   Si raccomanda di considerare un eventuale coinvolgimento di personale
   esterno all'amministrazione (ad es. fornitori con un'influenza sulla
   migrazione). Nella scheda di assessment è presente un foglio di
   lavoro separato da riempire con queste specifiche informazioni

-  **Processi impattati e punti di attenzione**: Riportare i processi
   interni o esterni dell'organizzazione che vengono impattati da questo
   applicativo e se vi sono dei punti d'attenzione da considerare
   durante il processo di migrazione

3.2.5 Bisogni
-----------------

I bisogni sono quelle informazioni che identificano l’utilizzo effettivo
dell’applicativo e le necessità che deve supportare. Considerare i
bisogni servirà all’amministrazione per valutare l’opportunità connessa
alla migrazione dell’applicativo. I campi da riempire in questa sezione
sono:

-  **# medio di utenti unici giornalieri negli ultimi 12 mesi**: numero
   medio di utenti unici in un giorno nell’ultimo anno. Il periodo
   considerato di 12 mesi vuole evitare periodi di prolungato
   inutilizzo. Per questo campo si consiglia di utilizzare, se
   disponibili, i dati degli strumenti di analytics

-  **# massimo di utenti unici giornalieri negli ultimi 12 mesi**:
   numero massimo di utenti unici in un giorno nell’ultimo anno. Il
   periodo considerato di 12 mesi vuole evitare periodi di prolungato
   inutilizzo. Per questo campo si consiglia di utilizzare, se
   disponibili, i dati degli strumenti di analytics

-  **# minimo di utenti unici giornalieri negli ultimi 12 mesi**: numero
   minimo di utenti unici in un giorno nell’ultimo anno. Il periodo
   considerato di 12 mesi vuole evitare periodi di prolungato
   inutilizzo. Per questo campo si consiglia di utilizzare, se
   disponibili, i dati degli strumenti di analytics. Se ci sono giorni
   in cui l'applicativo è inutilizzato o spento, mettere “0” come valore

-  **Periodi di utilizzo in una settimana**: fasce orarie in cui il
   servizio è utilizzato durante una settimana. Devono essere
   evidenziate qui eventuali fasce in cui si hanno picchi di utilizzo
   significativo. Se l'utilizzo è mediamente costante nell'arco della
   giornata e della settimana, indicare "utilizzo omogeneo"

-  **Periodi di utilizzo in un mese**: fasce orarie in cui il servizio è
   utilizzato durante il mese. Devono essere evidenziate qui eventuali
   fasce in cui si hanno picchi di utilizzo significativo. Se l'utilizzo
   è mediamente costante nell'arco del mese, indicare "utilizzo
   omogeneo"

-  **Periodi di utilizzo in un anno**: fasce orarie in cui il servizio è
   utilizzato durante l’anno. Devono essere evidenziate qui eventuali
   fasce in cui si hanno picchi di utilizzo significativo. Se l'utilizzo
   è mediamente costante nell'arco dell’anno, indicare "utilizzo
   omogeneo"

-  **Costi dell'infrastruttura**: tempi e costi per l'allestimento, la
   manutenzione dell'infrastruttura attuale ed il suo eventuale
   potenziamento (provisioning di nuove risorse). Questa informazione
   aiuta in particolare a calcolare l’impatto economico che la
   migrazione al cloud dell’applicativo può avere.

-  **Licenze**: tutte licenze che sono utilizzate, specificando il loro
   costo e quando scadono. Anche questa informazione aiuta in
   particolare a calcolare l’impatto economico che la migrazione al
   cloud dell’applicativo può avere. Nella scheda di assessment è
   presente un foglio di lavoro separato da riempire con queste
   specifiche informazioni. Per il riuso considerare le `indicazioni
   pubblicate su Docs
   Italia <https://docs.italia.it/italia/developers-italia/lg-acquisizione-e-riuso-software-per-pa-docs/it/bozza/>`__

-  **Criticità**: eventuali aspetti critici dell'applicativo, ad
   esempio:

   -  performance o stabilità che impattano l'operatività degli utenti
      finali o richiedono una spesa specifica per la loro risoluzione
      temporanea (perché una definitiva non è attualmente possibile)

   -  conformità normativa, ad esempio GDPR

   -  sicurezza

-  **Evoluzione del servizio nei prossimi tre anni**: aree di evoluzione
   previste o ipotizzate per il servizio supportato dall'applicativo per
   identificarne la centralità rispetto alla strategia
   dell'organizzazione. Tenere in considerazione, nel caso siano
   disponibili, i piani pluriennali definiti ed eventuali scadenze già
   definite. Considerare qui la tipologia e la numerosità delle
   evoluzioni attese per l'applicativo

3.2.6 Mercato
-----------------

Le informazioni riguardo al mercato aiutano ad esplorare le opportunità
presenti sul mercato per una migrazione al cloud dell’applicativo. I
campi da riempire in questa sezione sono:

-  **Alternative SaaS**: esistenza di alternative SaaS per l’applicativo
   in analisi all’interno del `Cloud
   Marketplace <https://catalogocloud.agid.gov.it/>`__
   di AGID

-  **Disponibilità di import dei dati**: garanzia che il fornitore SaaS
   provveda la possibilità di importare i dati all’interno del servizio
   SaaS tramite formati pubblici e aperti
