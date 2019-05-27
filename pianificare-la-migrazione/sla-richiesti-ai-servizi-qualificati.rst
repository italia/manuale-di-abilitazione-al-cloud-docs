4.3 SLA richiesti ai servizi qualificati
========================================

Gli SLA (service level agreement, ovvero accordi sul livello di un
servizio) sono un elemento importante di qualsiasi contratto con i
fornitori di servizi. Oltre a formalizzare le aspettative su tipo e
qualità del servizio, uno SLA definisce le misure da adottare quando non
vengono soddisfatti gli standard pattuiti. Infatti, uno SLA è un
documento che descrive il livello di servizio offerto da un fornitore a
un cliente, indicando le metriche con cui viene misurato il servizio e
misure o sanzioni da mettere in atto se i livelli concordati non sono
soddisfatti.

| Per redigere uno SLA per la fornitura di servizi cloud, è importante
  tenere in considerazione diversi aspetti che possono essere adeguati
  ai modelli di fruizione SaaS, PaaS e IaaS.
| I servizi qualificati da AgID dovranno rispondere a tutta una serie di
  requisiti e SLA come definito nella `Circolare n.2 del 9 Aprile
  2018 <https://trasparenza.agid.gov.it/moduli/downloadFile.php?file=oggetto_allegati/181151234430O__OCircolare+2-2018_Criteri+per+la+qualificazione+dei+Cloud+Service+Provider+per+la+PA.pdf>`__
  per i servizi IaaS e PaaS e nella `Circolare n.3 del 9 Aprile
  2018 <https://trasparenza.agid.gov.it/moduli/downloadFile.php?file=oggetto_allegati/181151237210O__OCircolare+3-2018_Criteri+per+la+qualificazione+di+servizi+SaaS+per+il+Cloud+della+PA+%28002%29.pdf>`__
  per i servizi SaaS. Di seguito riportiamo una più generica lista di
  metriche da tenere in sempre in considerazione nella definizione degli
  SLA per i servizi in cloud:

-  **metriche di uptime:** rappresenta l’ammontare di tempo in cui il
   servizio offerto sarà disponibile ed accessibile ai suoi utenti.
   Viene rappresentato da una percentuale di disponibilità, ad esempio:

   -  99.9% uptime rappresenta 8.77 ore di downtime in un anno

   -  99.99% uptime rappresenta 52.60 minuti di downtime in un ann.

   -  99.999% uptime rappresenta 5.26 minuti di downtime in un anno

   -  99.9999% uptime rappresenta 31.5 secondi di downtime in un anno

-  **capacità del servizio:** rappresenta la capacità in termini di
   carico o di numero di utenti massimi che possono accedere al servizio
   e le opzioni per poter espandere questo numero

-  **monitoring delle performance:** la definizione delle modalità con
   cui il fornitore monitorerà e riporterà le prestazioni del sistema

-  **sicurezza:** è importante definire metriche relative alla sicurezza
   del dato e alla regolamentazione del suo accesso, come ad esempio:

   -  protezione del dato

   -  livelli di crittografia

   -  politiche di backup

   -  permessi di accesso e consultazione del dato

   -  conformità alle normative vigenti

   -  modalità e tempi di comunicazione del provider in caso di data
      breach

-  **cambi di infrastruttura:** anche se nel caso di provider cloud i
   cambiamenti infrastrutturali sono molto più frequenti ed eseguiti in
   maniera trasparente, può essere utile richiedere al fornitore di
   essere informati in caso di aggiornamenti o cambiamenti rilevanti,
   così da pianificare e avvisare gli utenti di possibili downtime

-  **supporto:** il supporto è una parte fondamentale dei rapporti con i
   fornitori di servizi cloud e si può suddividere in due metriche
   fondamentali:

   -  **tempo di risposta:** rappresenta il tempo necessario al
      fornitore per rispondere ad una richiesta di supporto del cliente.
      Questo tempo è può essere variabile in base alla criticità della
      richiesta

   -  **tempo di risoluzione:** rappresenta il tempo necessario al
      fornitore per risolvere e chiudere una richiesta di supporto del
      cliente

Tramite l’utilizzo di questi accordi è quindi possibile definire i
cosiddetti Service Level Objectives (SLO) associati alle diverse
metriche considerate come nella seguente tabella d’esempio:

+-----------------------+-----------------------+-----------------------+
| **Metrica**           | **SLO**               | **Periodo**           |
+-----------------------+-----------------------+-----------------------+
| Uptime                | 99.95%                | 1 anno                |
+-----------------------+-----------------------+-----------------------+
| Tempo di risposta del | 75% delle richieste   | 3 mesi                |
| supporto              | verrà presa in carico |                       |
|                       | in meno di un minuto  |                       |
|                       | 85% delle richieste   |                       |
|                       | verrà presa in carico |                       |
|                       | entro due minuti      |                       |
|                       | 100% delle richieste  |                       |
|                       | verrà presa in carico |                       |
|                       | entro tre minuti      |                       |
+-----------------------+-----------------------+-----------------------+

| Questi accordi permettono a fornitore e amministrazione di definire
  chiaramente le rispettive aspettative in termini di qualità del
  servizio e supporto.
| Il fornitore dovrà produrre report frequenti e su richiesta
  dell’amministrazione, evidenziando i livelli relativi alle metriche
  concordate, così da fugare qualunque tipo di dubbi in caso di
  controversie.
