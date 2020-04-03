import json
import httpx
from datetime import datetime

key = input('Entra la teva API key: ')
token = input('Entra la teva API token: ')
rdid = input('Entra la ID de l\'escaleta: ')
url = "https://rundowncreator.com/uabcm/API.php?APIKey=" + key + "&APIToken=" + token + "&Action=getObjects&type=audio&OrderBy=Position&RundownID=" + rdid

r = httpx.get(url.format())
data = json.loads(r.text) 

filtered = []
for row in data:
    filtered.append(row['Payload'])

output = []
for row in filtered:
    output.append({
            'filename': row['filename'],
            'duration': row['duration'],
    })

lst = []
for row in output:
    lst.append(f"{row['duration']} {row['filename']}\n")
n = len(lst)

date = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
FILENAME = (date) + ".lst"

with open(FILENAME, 'w') as f:
    f.write(str(n)+"\n")
    f.writelines(lst)
