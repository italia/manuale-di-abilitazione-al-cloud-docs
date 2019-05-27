.. _buone-pratiche-1:

6.2 Buone pratiche
==================

Nella migrazione si consiglia di utilizzare le seguenti buone pratiche:

1. prima di procedere con la migrazione eseguire un backup completo del
   database sorgente

2. trasferire i dati utilizzando la connessione internet se la loro
   dimensione è ragionevole rispetto alla connessione disponibile;
   utilizzare una connessione diretta con la piattaforma cloud per
   grandi quantità di dati;

3. utilizzare una connessione sicura durante il trasferimento dei dati
   verso il sistema di destinazione in modo da proteggere le
   informazioni sensibili

4. utilizzare i servizi di migrazione dei dati forniti direttamente dal
   cloud provider, se disponibili

5. assicurarsi che i dati nel database sorgente non possano essere
   modificati durante tutto il processo di migrazione e di validazione

6. comparare i tempi di esecuzione di un insieme di query sul sistema
   sorgente con quelli del sistema di destinazione per capire l’impatto
   sulle performance

7. suddividere la migrazione di tabelle con grandi quantità di dati in
   parti più piccole per migliorare le performance nel trasferimento

8. verificare che l’applicazione funzioni correttamente dopo la
   migrazione
