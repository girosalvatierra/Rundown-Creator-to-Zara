import json
import httpx
import sys

key = ""
token = ""
url = "https://rundowncreator.com/uabcm/API.php?APIKey=" + key + "&APIToken=" + token + "&Action=getRows&RundownID={}"



def main(rundown):
    r = httpx.get(url.format(rundown))
    data = json.loads(r.text)

    filtered = []
    for row in data:
        filtered.append({
                'font': row['font'],
            })

    print(filtered)







if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        print("ERROR: Dona'm una ID.")
