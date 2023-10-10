# Configuration

## Number of Rigs

Usually this will be 1, but in some cases at large events multiple rigs will be used. In this case you can specify the number of rigs here.

## Observability Cloud

### Realm

Realm name for the Observability Cloud realm you want to send data to e.g. `us1`, `eu0` etc.

### Access Token

Observability Cloud access token (must have `ingest` capability).

## Splunk Cloud/Enterprise

### HEC URL

HEC URL for Splunk Cloud/Enterprise e.g. `https://simulator.prod.splunkcloud.com:8088`.

### HEC Token

HEC Token for Splunk Cloud/Enterprise.

## Enable sending metrics

You are able to send the metrics to both Observability Cloud and Splunk Cloud/Enterprise. To enable either or both just tick the relevant boxes.

* Tick **Enable Observability Cloud** to enable sending data to O11y Cloud.
* Tick **Enable Splunk Cloud** to enable sending data to Splunk Cloud.

Finally click **Save Configuration**
