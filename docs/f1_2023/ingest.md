# Ingest settings

Open the Web UI and expand the left hand menu, here you can configure where the game data is going to be sent.

![Listener Down](/assets/screenshots/f1_2023_web_ui_settings.png)

## Number of Rigs

Usually this will be 1, but in some cases at large events multiple rigs will be used. In this case you can specify the number of rigs here.

## Observability Cloud

Realm name for the O11y Cloud realm you want to send data to e.g. `us1`, `eu0` etc.

## Access Token

Observability Cloud access token (must have `ingest` capability).

Tick **Enable Observability Cloud** to enable sending data to O11y Cloud.

## HEC URL

HEC URL for Splunk Cloud/Enterprise e.g. `https://localhost:8088`.

## HEC Token

HEC Token for Splunk Cloud/Enterprise.

Tick **Enable Splunk Cloud** to enable sending data to Splunk Cloud.
