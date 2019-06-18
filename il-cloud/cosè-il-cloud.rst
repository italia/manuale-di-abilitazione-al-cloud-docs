1.1 Cos’è il cloud
======================

| Il *cloud computing* (in italiano *nuvola informatica*), più
  semplicemente cloud, è un modello di infrastrutture informatiche che
  consente di disporre, tramite internet, di un insieme di risorse di
  calcolo (ad es. reti, server, risorse di archiviazione, applicazioni
  software) che possono essere rapidamente erogate come servizio.
| Questo modello consente di semplificare drasticamente la gestione dei
  sistemi informativi, sia eliminando la gestione relativa ad
  applicativi fruibili direttamente online, sia trasformando le
  infrastrutture fisiche in servizi virtuali fruibili in base al consumo
  di risorse.

Rispetto alle tradizionali soluzioni hardware, il modello cloud consente
di:

-  usufruire delle applicazioni da qualsiasi dispositivo in qualsiasi
   luogo tramite l’accesso internet

-  avere importanti vantaggi di costo nell’utilizzo del software, in
   quanto consente di pagare le risorse come servizi in base al consumo
   (“pay per use”), evitando investimenti iniziali nell’infrastruttura e
   costi legati alle licenze di utilizzo

-  ridurre i costi complessivi collegati alla location dei data center
   (affitti, consumi elettrici, personale non ICT)

-  avere maggiore flessibilità nel provare nuovi servizi o apportare
   modifiche, con costi accessibili

-  effettuare in maniera continua gli aggiornamenti dell’infrastruttura
   e delle applicazioni

-  ridurre i rischi legati alla gestione della sicurezza (fisica e
   logica) delle infrastrutture IT

La maggior parte dei servizi di cloud computing rientra in tre ampie
categorie:

-  | **software-as-a-service** (**SaaS**), ovvero *software come
     servizio*: si tratta di un metodo per la distribuzione di
     applicativi software tramite internet, su richiesta e in genere in
     base a una sottoscrizione. Nel caso di una soluzione SaaS, i
     provider di servizi cloud ospitano e gestiscono il software e
     l’infrastruttura sottostante e si occupano delle attività di
     manutenzione, come gli aggiornamenti. Gli utenti si connettono
     all’applicazione tramite internet e possono accedervi da diverse
     tipologie di dispositivi (desktop, mobile, tablet, …). A differenza
     del modello ASP (`Application Service
     Provisioning <https://it.wikipedia.org/wiki/Application_service_provider>`__),
     dove i fornitori installano un’istanza di applicazione per ogni
     cliente personalizzandole a seconda delle richieste di ognuno, il
     paradigma SaaS fa uso di applicazioni
     “\ `multi-tenant <https://it.wikipedia.org/wiki/Multi-tenant>`__\ ”,
     cioè noleggiabili da più utenti contemporaneamente, con codice non
     customizzabile ma uguale per tutti. Un approccio, quest’ultimo, che
     garantisce il raggiungimento più facile di economie di scala da
     parte del fornitore.
   | Esempi di SaaS sono: Microsoft Office 365, tutte le app di Google,
     iCloud

-  | **platform-as-a-service** (**PaaS**)\ **,** ovvero *piattaforma
     distribuita come servizio*: si tratta di servizi cloud che
     forniscono strumenti e ambienti per lo sviluppo, il test, la
     distribuzione e la gestione di applicazioni software, solitamente
     tramite strumenti specifici forniti dal provider stesso e pannelli
     di configurazione fruibili via browser web. Una soluzione PaaS è
     progettata per consentire agli sviluppatori di progettare e creare
     concentrandosi sulle funzionalità dell’applicativo, lasciando al
     fornitore del servizio aspetti come la configurazione, la gestione
     dell’ambiente di esecuzione dell’archiviazione o dei database.
   | Esempi di PaaS sono: Google App Engine, AWS Beanstalk, Azure App
     Service, Heroku

-  | **infrastructure-as-a-service** (**IaaS**), ovvero *infrastruttura
     distribuita come servizio*: si tratta di servizi cloud che
     permettono di allocare risorse infrastrutturali fisiche e virtuali
     (server, macchine virtuali, risorse di archiviazione e networking)
     su richiesta mediante interfacce grafiche o mediante API
     (`Application Programming
     Interfaces <https://it.wikipedia.org/wiki/Application_programming_interface>`__\ *)
     c*\ on pagamento in base al consumo.
   | Esempi di IaaS sono: Google Compute Engine, AWS EC2, Azure Instance

Vi sono inoltre diversi modelli di dispiegamento dei servizi:

-  **cloud pubblico:** offerti da fornitori che mettono a disposizione
   dei propri utenti/clienti la potenza di calcolo e/o di memorizzazione
   dei loro data center. Il tipo di servizi cloud che vengono offerti
   dal fornitore (IaaS, PaaS, SaaS) dipende dalla politica del fornitore
   stesso, così come il prezzo e la tariffazione. Uno dei maggiori
   vantaggi del cloud pubblico per il cliente consiste nel fatto che
   egli può richiedere l'utilizzo dei servizi cloud di cui necessita nel
   momento in cui effettivamente ne ha bisogno, e solo per il tempo che
   gli sono necessari. In questo modo, il cliente può ridurre
   notevolmente gli investimenti in infrastrutture IT e ottimizzare
   l'utilizzo delle risorse interne che le gestiscono, oltre a trarre
   vantaggio dai già citati benefici.

-  **cloud privato:** installato dall'utente nel suo data center per suo
   utilizzo esclusivo. I servizi vengono forniti da elaboratori che si
   trovano interamente nel dominio del cliente che detiene controllo e
   totale responsabilità della gestione delle macchine sulle quali
   vengono conservati i dati e vengono eseguiti i suoi processi, assieme
   ai complessi aspetti relativi alla sicurezza dei dati. Oltre allo
   scenario in cui si possiede interamente l’infrastruttura sui propri
   data center, un altro scenario possibile è invece quello in cui
   l'utente installa il proprio cloud privato nel data center di un
   terzo soggetto (tipicamente un fornitore di servizi cloud), in cui
   dispone di macchine dedicate. In questo caso, l'utente ha il
   controllo delle macchine anche se non risiedono nel suo dominio, e
   può configurarle secondo le proprie necessità.

-  **cloud ibrido:** combinazione del modello pubblico e di quello
   privato, ovvero un modello in cui l'utente utilizza risorse sia del
   suo cloud privato che di un cloud pubblico. Ad esempio, un utente che
   dispone di un cloud privato, può utilizzare le risorse di un cloud
   pubblico per gestire improvvisi picchi di lavoro che non possono
   essere soddisfatti facendo ricorso unicamente alle risorse
   disponibili nel cloud privato. Tuttavia questo modello comporta
   comunque la proprietà e conseguente gestione della parte privata
   delle infrastrutture, risultando in maggiori costi e rischi.

Le linee guida in questo documento saranno orientate al modello di cloud
pubblico, in quanto più allineato agli obiettivi della strategia di
cloud enablement, ovvero:

-  minimizzazione dell’infrastruttura proprietaria di un ente

-  riduzione dell’onere di manutenzione ed ammodernamento continuo
   dell’infrastruttura e delle competenze necessarie per farlo

-  incremento della facilità di adozione delle soluzioni e dei servizi
   progressivamente disponibili grazie all’evoluzione di mercato

-  adozione di servizi ai più alti standard qualitativi di mercato,
   riflessi negli SLA garantiti

È possibile consultare le definizioni del modello cloud e le proprietà
specifiche dei servizi facendo riferimento al `documento del
NIST <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf>`__.

Non tutti i servizi e le infrastrutture di cloud computing sono uguali.
In alcuni casi tali servizi possono anche non rispettare i principali
standard di sicurezza, garanzie operative e affidabilità definiti a
livello internazionale. Questa disomogeneità può rappresentare un
rischio quando si affidano i propri dati a provider che non garantiscono
dei livelli minimi di sicurezza e affidabilità.

Il modello `Cloud della
PA <https://cloud.italia.it/projects/cloud-italia-docs/it/latest/cloud-della-pa.html>`__
consente di mitigare tale rischio, qualificando servizi e infrastrutture
cloud secondo specifici parametri di sicurezza e affidabilità idonei per
le esigenze della pubbliche amministrazioni. Il Cloud della PA si
compone di infrastrutture e servizi, qualificati da AGID sulla base di
un insieme minimo di requisiti, che possono essere confrontati e
consultati sul `Cloud
Marketplace <https://cloud.italia.it/marketplace/supplier/market/index.html>`__.
