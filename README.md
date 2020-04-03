# Rundown Creator to Zara

"rdc2z.py" és un script per generar playlists de [ZaraStudio](https://www.zarastudio.es/es/) a partir d'objectes de [Rundown Creator](http://rundowncreator.com/) amb el format

```xml
<audio  id=""  filename=""  duration="0">
```

"filename" és la ruta completa del fitxer d'àudio i "duration" n'és la seva durada en ms.

"durada_arx.py" és un script que retorna la durada en ms d'un fitxer en format ASF, FLAC, MP4, Monkey’s Audio, MP3, Musepack, Ogg Opus, Ogg FLAC, Ogg Speex, Ogg Theora, Ogg Vorbis, True Audio, WavPack, OptimFROG, o AIFF.

## Requisits previs

Per fer funcionar "rdc2z.py", necessitem [Python](https://www.python.org/downloads/) i el paquet [httpx](https://pypi.org/project/httpx/).

1. Instal·lem Python, marquem l'opció "Add to PATH"
2. Obrim una terminal (cmd a Windows) i instal·lem httpx

    ```bash
    pip install httpx
    ```

Per fer funcionar l'script "durada_arx.py", també necessitarem el paquet [mutagen](https://pypi.org/project/mutagen/)

```bash
pip install mutagen
```

## Utilització

1. Configurem el fitxer "claus.txt" amb les nostres claus de l'API (Ha d'estar al mateix directori que l'script)
    * Podem trobar les nostres dades per accedir a l'API a <https://rundowncreator.com/uabcm/Settings.php?Page=MySettings-API>
    * Recordeu que heu de marcar la casella "Enable my API key/token" i guardar per activar les vostres credencials de l'API.
2. Executem l'script "rdc2z.py" i hi escrivim la ID de l'escaleta que ens interessa, es crearà el fitxer .lst al mateix directori on hi tenim l'script amb el format \[data i hora actuals].lst

## ToDo

1. ~Manipular dades per generar un fitxer .lst~
    * També cal trobar alguna manera de tenir la duració dels fitxers per al Zara (En desenvolupament, veure <durada_arx.py>)
2. ~Fer funcionar les variables "key", "token" i "RundownID" com a inputs~ (Funciona a req2.py)
3. Crear una GUI
