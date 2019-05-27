4.4 Lock-in
===========

Il lock-in è un fenomeno di natura tecnica ed economica tale per cui
un’organizzazione non riesce a svincolarsi facilmente da una scelta
tecnologica precedentemente effettuata. Tra i fattori che più spesso lo
causano vi sono:

-  costi di transizione molto alti, che impediscono di cambiare
   tecnologia o fornitore se non ad un costo (non solo monetario) molto
   elevato

-  mancanza di informazioni esaustive sul sistema attuale, che impedisce
   ad un nuovo fornitore di subentrare in maniera efficiente

Esistono diverse tipologie di lock-in, ma anche diverse pratiche per
prevenirlo o almeno ridurlo. Esserne a conoscenza ancor prima di
iniziare una migrazione al cloud può aiutare la pubblica amministrazione
a mitigare i rischi e i costi connessi a questo fenomeno.

4.4.1 Tipologie di lock-in nella pubblica amministrazione
---------------------------------------------------------

Il caso di lock-in più comune nell’ambito della pubblica amministrazione
è quello legato ai fornitori. Solitamente, infatti, le pubbliche
amministrazioni instaurano con quest’ultimi rapporti solidi e di lungo
periodo, dai quali difficilmente si svincolano per non ritrovarsi a
gestire i problemi connessi al cambio di un fornitore ben consolidato.
Questi problemi rappresentano i cosiddetti costi di transizione e
possono essere molteplici e di diversa natura. Troviamo costi di natura:

-  **burocratica**: come ad esempio la progettazione e lo svolgimento
   della procedura di gara per la selezione di un nuovo fornitore

-  **tecnologica**: come ad esempio la migrazione dei dati creati fino a
   oggi dal vecchio al nuovo fornitore

-  **economica**: come ad esempio i costi da pagare per eseguire
   l’operazione di migrazione dei dati di cui sopra

Nell’ ambito dei fornitori di soluzioni tecnologiche ci sono diverse
tipologie di lock-in a cui prestare attenzione:

-  **lock-in sul dato**: può verificarsi nel caso vengano utilizzati
   software che non permettono di esportare i dati generati nel corso
   del loro utilizzo secondo formati considerati standard o che lavorano
   con formati proprietari. Questi software tendono a generare un forte
   lock-in a causa degli alti costi in cui si incorre per migrare i dati
   sui nuovi sistemi

-  **lock-in sulla conoscenza**: può verificarsi nel caso ci sia una
   scarsa documentazione del software e delle decisioni prese e/o una
   carenza (o assenza totale) di materiale di formazione. Queste
   mancanze comportano una bassa condivisione della conoscenza acquisita
   dal fornitore e aumentano dunque il lock-in sullo stesso. In questo
   caso, infatti, la pubblica amministrazione è completamente dipendente
   dal fornitore iniziale per l’ottenimento delle suddette informazioni
   e non è in grado di fornirle in maniera semplice ad un nuovo
   affidatario

-  **lock-in contrattuale:** può verificarsi nel caso vi siano clausole
   contrattuali che rendono costoso e difficile il cambio di fornitore o
   software

4.4.2 Come mitigare il lock-in
------------------------------

Vi sono una serie di pratiche tecnologiche, metodologiche e contrattuali
che, se attuate dalla pubblica amministrazione e dai suoi fornitori sin
dall’inizio di un affidamento, permetteranno di ridurre e mitigare il
lock-in insieme ai costi e ai rischi ad esso associati.

4.4.2.1 Pratiche tecnologiche
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Come buone pratiche tecnologiche da adottare per mitigare il rischio di
lock-in da fornitore consigliamo di:

-  garantire l’interoperabilità mediante l’esposizione di API come
   definito anche dalle `linee guida di
   AgID <https://www.agid.gov.it/it/infrastrutture/sistema-pubblico-connettivita/il-nuovo-modello-interoperabilita>`__
   e mediante lo scambio di dati in formati standard come JSON o XML

-  evitare l’utilizzo di formati di dato proprietari, ma favorire invece
   i formati standard e open

-  avere la possibilità di esportare (e possibilmente importare) i dati
   in un formato standard che garantisca l’interoperabilità e la
   portabilità ad altri sistemi

-  favorire l’utilizzo di strumenti e framework di sviluppo open e
   diffusi rispetto a soluzioni sviluppate internamente e di difficile
   manutenibilità per altri fornitori

-  nel caso di servizi PaaS o IaaS, favorire l’utilizzo di servizi
   basati su tecnologie open source e valutare l’utilizzo di servizi
   unici del cloud service provider solo se il valore ottenuto
   giustifica il maggior costo di switch (ovvero di cambiamento)

-  garantire la portabilità dell’applicativo tramite l’utilizzo di stack
   tecnologici indipendenti dalla piattaforma

-  favorire l’indipendenza degli applicativi dalle loro dipendenze
   esterne e di piattaforma come ad esempio hardware, sistema operativo
   o servizi specifici dei cloud service provider (PaaS o IaaS) tramite
   l’utilizzo di strumenti di containerizzazione come Docker e
   `architetture che separino il core applicativo della
   piattaforma <https://dzone.com/articles/hexagonal-architecture-what-is-it-and-how-does-it>`__

-  favorire l’uso di tecnologie open source

-  in caso di software sviluppato ad-hoc per l’amministrazione,
   assicurarsi di avere la proprietà e l’accesso al codice sorgente

4.4.2.2 Pratiche metodologiche
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le pratiche metodologiche da adottare per mitigare il rischio di lock-in
con il fornitore sono principalmente orientate alla condivisione della
conoscenza e possono essere suddivise in due aree: documentazione e
metodologia di lavoro.

**Documentazione**

Spesso giudicata poco utile e non manutenuta nel tempo, la
documentazione gioca tuttavia un ruolo molto importante sulla riduzione
del lock-in. Questa, infatti, è uno degli strumenti fondamentali che la
pubblica amministrazione ha per preservare internamente per successive
consultazioni la conoscenza generata dal fornitore.

La chiave per una documentazione efficace sta nel concentrarsi solo
sugli aspetti chiave e realmente importanti che la rendano così uno
strumento strategico e non un ulteriore costo non necessario. Le
informazioni importanti che devono essere documentate sono di vario
tipo. Tra queste troviamo:

-  **decisioni significative**: decisioni impattanti che generalmente
   possono essere riconosciute dai seguenti aspetti:

   -  richiedono molto tempo per essere concordate

   -  sono critiche nel raggiungimento di un requisito di progetto

   -  il loro impatto nel medio-lungo termine non è chiaro da subito

   -  impattano una grossa parte del sistema in oggetto

   -  una volta prese ed attuate è difficile tornare alla situazione
      precedente

Per natura, queste decisioni si distinguono in:

-  **architetturali**: decisioni di progettazione software che
   soddisfano un requisito funzionale o non funzionale e che hanno un
   impatto significativo sull’architettura del sistema

-  **relative al business**: decisioni che rientrano nell’ambito più
   strategico dell’amministrazione o di un progetto specifico

I formati che consigliamo di adottare per questo tipo di decisioni sono
l’\ **Architectural Decision Records** (`ADR <https://adr.github.io>`__)
e il corrispondente **Business Decision Records** (BDR). Questi “record”
nel tempo formeranno una memoria storica e cronologica delle decisioni
prese, risulta quindi fondamentale l’immutabilità del contenuto e il
fatto che non debbano mai essere cancellate, anche quando le decisioni
sono state sostituite da altre. In allegato a queste linee guida trovate
un possibile template per ADR/BDR (vedi allegato “ADR-BDR Template”).

Questo tipo di documentazione può essere conservata direttamente
all’interno dei repository di codice sorgente, se a scriverla sono
persone coinvolte nello sviluppo software, altrimenti si consiglia di
crearla e conservarla con un software specifico per la gestione della
documentazione.

-  **artefatti generati durante il processo di migrazione**: artefatti
   che devono essere conservati in aggiunta alle decisioni significative
   prese per tenere traccia dell’importante conoscenza generata durante
   il processo di migrazione. Alcuni esempi non esaustivi sono:

   -  diagramma architetturale per visualizzare l’organizzazione delle
      risorse infrastrutturali on-premise e/o in cloud, evidenziando in
      particolare:

      -  macchine virtuali

      -  database

      -  storage

      -  networking

      -  sistemi di bilanciamento del carico

      -  sistemi di backup

      -  servizi specifici del cloud service provider

   -  procedure di alerting e monitoring

   -  procedure di rilascio

   -  procedure di patching

   -  procedure di review della sicurezza

   -  guida alla gestione delle identità e rispettivo accesso ai sistemi
      (IAM)

   -  documentazione delle API dei servizi

   -  documentazione delle personalizzazioni sviluppate sugli
      applicativi

-  **materiale di formazione**: materiale informativo sui software
   adottati dall’amministrazione, per evitare che il fornitore sia il
   detentore unico di questa conoscenza. La presenza di documentazione
   che evidenzi come interagire ed eventualmente amministrare il
   software permetterà all’amministrazione di essere più autonoma e
   veloce nell’organizzazione e formazione dei suoi impiegati,
   avvalendosi del supporto del fornitore solo in casi particolari e più
   complessi.

Uno dei principali rischi associato alla documentazione è che essa
smetta di essere manutenuta regolarmente diventando, nel peggiore dei
casi, una fonte di informazioni obsolete e soprattutto sbagliate. Una
tecnica utile a mitigare questo rischio è quella di creare meeting
ricorrenti in cui fare revisione delle informazioni documentate fino a
quel momento, così da tenere sempre alto il livello di attenzione su
questo strumento strategico e identificare tempestivamente eventuali
mancanze.

**Metodologia di lavoro**

Lavorare insieme ai fornitori seguendo buone pratiche di collaborazione
e condivisione può ridurre significativamente il rischio di lock-in. Per
questo motivo, consigliamo di adottare le seguenti buone pratiche:

-  **incontri** **di allineamento**: incontri ricorrenti che aiutino a
   raggiungere un buon grado di condivisione della conoscenza riducendo
   i rischi connessi al lock-in su di essa. In particolare, consigliamo
   di organizzare i seguenti incontri di allineamento:

   -  | **showcase:** un incontro di circa un’ora da organizzare alla
        fine di ogni iterazione (ogni una o due settimane) durante il
        quale si presentano i risultati raggiunti e il valore prodotto
        nell’iterazione corrente e si discute il piano per l’iterazione
        successiva integrando eventuali feedback (vedi capitolo 5.1.4)
      | Partecipanti: team del fornitore, team tecnico
        dell’amministrazione, responsabili di progetto
        dell’amministrazione
      | Durata massima: 60 minuti

   -  | **tech review:** meeting in cui si riuniscono il personale
        tecnico dell’amministrazione e del fornitore per poter
        condividere considerazioni importanti in merito ad architettura
        e codice del software o decisioni importanti dal punto di vista
        infrastrutturale.
      | Partecipanti: team tecnico del fornitore, team tecnico
        dell’amministrazione
      | Durata massima: 60 minuti

-  **pairing:** tecnica in cui due persone lavorano insieme per
   risolvere un problema così da condividere opinioni e soluzioni in
   maniera trasparente e rapida. Nello specifico ambito dello sviluppo
   software questa tecnica viene denominata “Pair Programming”. Uno dei
   suoi vantaggi è la facilità con cui si condividono conoscenze e
   contesto aumentando nel complesso il flusso dell’informazione
   all’interno del team e aiutando a conservare la conoscenza
   all’interno dell’amministrazione

-  **visual management:** tecnica di comunicazione che attraverso
   l’utilizzo di artefatti visuali punta a comunicare informazioni
   chiave per il team. Nell’ambito di una migrazione può essere usata,
   ad esempio, per la visualizzazione dei lavori in corso con una Kanban
   board (vedi capitolo 5.1.4). L’aspetto chiave di questa tecnica è
   appunto l’utilizzo di informazioni visuali come rimedio all’ambiguità
   interpretativa delle comunicazioni verbali.

4.4.2.3 Pratiche contrattuali
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`I criteri per la qualificazione dei Cloud Service Provider per la
PA <https://trasparenza.agid.gov.it/moduli/downloadFile.php?file=oggetto_allegati/181151234430O__OCircolare+2-2018_Criteri+per+la+qualificazione+dei+Cloud+Service+Provider+per+la+PA.pdf>`__,
richiedono esplicitamente ai CSP di garantire l'assenza di ogni tipo
lock-in dell’Acquirente nei confronti del Fornitore Cloud. È bene però
integrare questo primo livello di mitigazione del rischio considerando
le pratiche tecnologiche e metodologiche illustrate sopra ancor prima di
iniziare l’affidamento.

In particolare, nella fase di pianificazione dell’affidamento, è
necessario che l'amministrazione non solo definisca i bisogni funzionali
relativi al software richiesto, ma consideri anche, oltre al costo
iniziale, i costi futuri relativi alla manutenzione della soluzione e
alla sua potenziale migrazione su nuovi sistemi o su fornitori diversi.

Si consiglia quindi, con lo scopo di mitigare i rischi e i costi
connessi al lock-in, di introdurre nei documenti di gara le opportune
clausole relative alle buone pratiche presentate in questo capitolo.

.. _section-1:
