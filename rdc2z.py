import json
import httpx
from datetime import datetime

# Recupera les claus d'API des d'un fitxer de text
with open("claus.txt") as json_file:
    claus = json.load(json_file)
    key = claus['key']
    token = claus['token']

# Input RundownID
rdid = input('Entra la ID de l\'escaleta: ')
url = "https://rundowncreator.com/uabcm/API.php?APIKey=" + key + "&APIToken=" + token + "&Action=getObjects&type=audio&OrderBy=Position&RundownID=" + rdid

# Carrega la resposta de l'API a una llista de diccionaris 'data'
r = httpx.get(url.format())
data = json.loads(r.text) 

# Descarta totes les dades excepte les de 'Payload'
filtered = []
for row in data:
    filtered.append(row['Payload'])

# Descarta totes les dades excepte 'filename' i 'duration'
output = []
for row in filtered:
    output.append({
            'filename': row['filename'],
            'duration': row['duration'],
    })

# Crea una llista 'lst' amb una entrada per cada objecte i recompte d'objectes
lst = []
for row in output:
    lst.append(f"{row['duration']}	{row['filename']}\n")
n = len(lst)

# Carrega la resposta de l'API getRundowns a 'data2'
url2 = "https://rundowncreator.com/uabcm/API.php?APIKey=" + key + "&APIToken=" + token + "&Action=getRundowns&RundownID=" + rdid
r2 = httpx.get(url2.format())
data2 = json.loads(r2.text)

# Pren el títol de l'escaleta
titol = []
for cell in data2:
    titol.append(cell['Title'])
titolescaleta=str(titol)
titolescaleta=titolescaleta[2:len(titolescaleta)-2]+"_"

# Estableix el nom del fitxer (titol_data_hora.lst)
date = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
FILENAME = (titolescaleta) + (date) + ".lst"

# Desa el fitxer .lst
with open(FILENAME, 'w') as f:
    f.write(str(n)+"\n")
    f.writelines(lst)
