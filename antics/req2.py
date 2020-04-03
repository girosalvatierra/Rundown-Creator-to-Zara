import json
import httpx

key = input('Entra la teva API key: ')
token = input('Entra la teva API token: ')
rdid = input('Entra la ID de l\'escaleta: ')
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

lst = []
for row in output:
    lst.append(f"{row['duration']} {row['filename']}\n")
n = len(lst)


print(lst)

FILENAME = "output.lst"

final = input('Vols desar-ho? (Y/n)')
if final in ["Y","y"]:
    with open(FILENAME, 'w') as f:
        f.write(str(n)+"\n")
        f.writelines(lst)
