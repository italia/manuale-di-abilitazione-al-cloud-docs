.. _la-validazione-1:

6.4 La validazione
==================

L’ultima fase del processo di migrazione deve prevedere i test di
accettazione finalizzati a garantire che tutti i dati che si vuole
trasferire sono stati effettivamente migrati correttamente.

Esempi di verifiche basilari e non esaustive eseguibili per verificare
la consistenza della migrazione sono:

-  eseguire le medesime query sul database sorgente e quello di
   destinazione ed assicurarsi che il risultato sia identico

-  verificare che il numero di record nel database sorgente e nel nuovo
   database sia il medesimo

È raccomandato di adottare anche tecniche avanzate per la validazione
della migrazione come quelle descritte di seguito.

6.4.1 Test di completezza
-------------------------

I test di completezza sono finalizzati a verificare che tutti gli
oggetti rilevanti a livello business che si vogliono migrare siano stati
effettivamente migrati con successo.

I test di completezza si basano sul concetto di Unità di Migrazione
(*Unit of Migration, UoM*), ovvero l’identificazione di ogni entità
rilevante a livello di business che può tradursi in una o più strutture
nella base dati (ad es. tabelle).

Le unità di migrazione sono importanti per capire quali entità non sono
state correttamente migrate (ad es. il cittadino i cui dati di anagrafe
non sono corretti). In caso di entità articolate su più tabelle si può
decidere che, a causa di un fallimento nella migrazione di un record in
una qualsiasi tabella, l’intera entità non vada migrata, causando quindi
la rimozione dei record legati a quella specifica entità inseriti prima
dell’errore (fallout management) o che quell’aspetto venga riportato
come errato.

La **riconciliazione** è una tecnica di verifica della completezza che
vuole assicurare che il numero di entità nel sistema sorgente sia il
medesimo nel sistema di destinazione. Come calcolarlo dipende dallo
specifico dominio di appartenenza delle entità che si stanno migrando.
Per alcuni domini un semplice conteggio dei record potrebbe essere
sufficiente, per altri potrebbe essere necessario eseguire operazioni
più complesse, come la cosiddetta validazione orizzontale o la
rigenerazione sullo stesso insieme di dati di report e analisi
disponibili dal sistema sorgente.

Il conteggio dei record deve considerare gli eventuali duplicati che
sono stati rimossi nel processo di migrazione e le entità per cui si
sono verificati errori:

*entità nel database sorgente = entità nel database destinazione +
entità rimosse perché duplicati - entità non migrate a causa di errori*

Per le entità non migrate a causa di errori deve essere identificato un
possibile rimedio.

La **validazione orizzontale** è una tecnica di verifica che si basa sul
conteggio di alcuni valori rilevanti delle entità che mira ad assicurare
che le trasformazioni, gli arricchimenti di dati, i consolidamenti e le
esclusioni non abbiano alterato aspetti fondamentali dell’unità di
migrazione. Ad esempio si potrebbe controllare il numero di pagamenti
sopra una determinata cifra, o il numero di cittadini per fasce d’età.

Un’altra tecnica che si può utilizzare è **ricreare una serie di report
generati nel sistema sorgente nel sistema destinazione e confrontarne il
risultato**.

6.4.2 Appearance test
---------------------

Gli appearance test mirano a ridurre il rischio di inconsistenza dei
dati. In questo tipo di test i tester, esperti di dominio, confrontano
manualmente i dati presenti nel sistema sorgente e destinazione
attraverso l’interfaccia utente dell’applicativo. Un esempio è
controllare che le informazioni di residenza riportate sulla scheda
utente di un cittadino, siano le stesse tra il sistema on-premise e
quello in cloud.

6.4.3 Test di integrazione
--------------------------

Questo tipo di test sono utilizzati quando più applicativi sono
interconnessi: quando un applicativo è impattato dalla migrazione, tutti
gli applicativi che ne dipendono sono anch’essi impattati. Le tecniche
di testing adottate sull’applicativo i cui dati sono stati migrati
possono essere utilizzate per validare il funzionamento anche degli
applicativi che dipendono da esso.
