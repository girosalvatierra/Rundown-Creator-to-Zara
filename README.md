# Rundown Creator to Zara
De moment, només tenim un script. 

## Requisits previs
Per fer-lo funcionar, necessitem [Python](https://www.python.org/downloads/) i el paquet [httpx](https://pypi.org/project/httpx/).

1. Instal·lem Python, marquem l'opció "Add to PATH"
2. Obrim una terminal i instal·lem httpx
```
$ pip install httpx
```

## Utilització
Primer cal editar l'script amb un editor de text per posar-hi les nostres dades per accedir a l'API, les podem trobar a https://rundowncreator.com/uabcm/Settings.php?Page=MySettings-API i les completem així:

```python
key = "[API Key]"
token = "[API Token]"
```


Obrim una terminal, des de la carpeta on tenim l'script i entrem:

    py .\req.py [ID de l'escaleta]
    
Podem fer servir l'escaleta ID=234 per provar-ho
   
## ToDo
1. Manipular dades per generar un fitxer .lst
    * També cal trobar alguna manera de tenir la duració dels fitxers per al Zara
2. Fer funcionar les variables "key", "token" i "RundownID" com a inputs
3. Crear una GUI
