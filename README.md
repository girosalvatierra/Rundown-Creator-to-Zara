# Rundown Creator to Zara
De moment, només tenim un script. Per fer-lo funcionar, necessitem [Python](https://www.python.org/downloads/).

## Utilització
Primer cal editar l'script amb un editor de text per posar-hi les nostres dades per accedir a l'API, les podem trobar a https://rundowncreator.com/uabcm/Settings.php?Page=MySettings-API i les completem així:

```python
key = "[API Key]"
token = "[API Token]"
```


Amb Python instal·lat, obrim una terminal, anem a la carpeta on tenim l'script i entrem:

    py .\req.py [ID de l'escaleta]