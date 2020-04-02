import json
import httpx

key = input('Entra la teva API key: ')
token = input('Entra la teva API token: ')
rdid = input('Entra l\'ID de l\'escaleta: ')
url = "https://rundowncreator.com/uabcm/API.php?APIKey=" + key + "&APIToken=" + token + "&Action=getObjects&type=audio&OrderBy=Position&RundownID=" + rdid

r = httpx.get(url.format())
data = json.loads(r.text) 

filtered = []
for row in data:
    filtered.append(row['Payload'])

print('Output:')
output = []
for row in filtered:
    output.append({
            'filename': row['filename'],
            'duration': row['duration'],
    })
print(output)
final = input('Prem intro per acabar')