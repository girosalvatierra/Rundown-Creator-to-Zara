import json
import httpx
import sys

key = ""
token = ""
url = "https://rundowncreator.com/uabcm/API.php?APIKey=" + key + "&APIToken=" + token + "&Action=getObjects&type=audio&OrderBy=Position&RundownID={}"


#loop principal
def main(rundown):
    r = httpx.get(url.format(rundown))
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

#no tocar
if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        print("ERROR: Dona'm una ID.")
