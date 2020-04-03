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

# Estableix el nom del fitxer (dataihora.lst)
date = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
FILENAME = (date) + ".lst"

# Desa el fitxer .lst
with open(FILENAME, 'w') as f:
    f.write(str(n)+"\n")
    f.writelines(lst)