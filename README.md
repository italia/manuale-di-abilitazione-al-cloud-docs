# Manuale di abilitazione al cloud
Repo del doc [Manuale di abilitazione al cloud](https://docs.italia.it/italia/manuale-di-abilitazione-al-cloud/manuale-di-abilitazione-al-cloud-docs/)

# Dipendenze

Il repository è strutturato per essere compatibile con la piattaforma [Docs
Italia](https://docs.italia.it/). 
La piattaforma accetta documenti in formato RST o MD. 
Per informazioni sulla struttura di questo repository visita il [repository
dedicato](https://github.com/italia/docs-italia-starter-kit).

# Preview con docker-compose

Per lavorare utilizzando una preview del documento è sufficiente lanciare Docker

```
docker-compose up
```

la preview sarà visibile all'indirizzo [http://localhost:8000/](http://localhost:8000/)

## Preview con podman

Se si preferisce usare podman si può usare il seguente estratto che crea
un’immagine basandosi sul nome della directory corrente:

``` shell
IMAGE_NAME=$(basename $(readlink -f .))
podman build . -t "${IMAGE_NAME}"
podman run --detach -v .:/app -v ./preview_build/preview_configuration.py:/app/conf.py -p 8000:8000 "${IMAGE_NAME}"
xdg-open http://localhost:8000
podman run --detach -v .:/app -v ./preview_build/preview_configuration.py:/app/conf.py -p 8000:8000 --name "${IMAGE_NAME}" "${IMAGE_NAME}"
podman container logs -f "${IMAGE_NAME}"
podman container stop "${IMAGE_NAME}"
podman container rm "${IMAGE_NAME}"
```

# Come contribuire

Ogni contributo è benvenuto!
È possibile aprire delle issue per segnalare errori, problemi o per la
richiesta di nuove funzionalità.
Inoltre, è possibile aprire delle Pull Request per proporre direttamente delle
modifiche.

# Licenza 

Questo documento è rilasciato con una licenza CC BY 4.0.
