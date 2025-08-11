# Configuration

## Number of Rigs

Usually this will be 1, but in some cases at large events multiple rigs will be used. In this case you can specify the number of rigs here.

## Event Name

This is the name of the event you are running. It will be used to identify the data in Splunk and Observability Cloud. It is recommended to use a unique name for each event to avoid confusion. The Event Name is also used on some of the Splunk dashboards to identify the event.

## Observability Cloud

**Realm:** Realm name for the Observability Cloud realm you want to send data to e.g. `us1`, `eu0` etc.

**Access Token:** Observability Cloud access token (must have `ingest` capability). This can be done by following the instructions [here](https://docs.splunk.com/Observability/admin/authentication-tokens/org-tokens.html#ingest-tokens).

## Splunk Cloud/Enterprise

**HEC URL:Port:** HEC URL and port for Splunk Cloud/Enterprise e.g. `https://simulator.prod.splunkcloud.com:8088`.

**HEC Token:** HEC Token for Splunk Cloud/Enterprise.

## Enable sending metrics

You are able to send the metrics to both Observability Cloud and Splunk Cloud/Enterprise. To enable either or both just tick the relevant boxes.

* Tick **Enable Observability Cloud** to enable sending data to O11y Cloud.
* Tick **Enable Splunk Cloud** to enable sending data to Splunk Cloud.

## Playback Mode

This defaults to `False`, meaning the container will listen for live data from the game. If set to `True`, then the container will replay pre-recorded data of 3 laps around Austria. This is useful for testing and development purposes, as it allows you to see how the container behaves with known data without needing to run the game.

Finally, click **Save Configuration**

## Indicators

When the collector is running, the port number of each Rig will light up green once UDP data is received. If the port number is grey, then no UDP data has been received for that Rig.
