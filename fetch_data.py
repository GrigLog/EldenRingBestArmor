import requests
import bs4
import json
from armor_piece import ArmorPiece

wiki = "https://eldenring.wiki.fextralife.com/"
pieces = [[], [], [], []]
parts = ["Helms", "Chest+Armor", "Gauntlets", "Leg+Armor"]
print("Getting data from wiki pages...")
for slot in range(4):
    html = bs4.BeautifulSoup(requests.get(wiki + parts[slot]).text, features="lxml")
    table = html.find("table").tbody
    for row in table.find_all("tr"):
        cols = row.find_all("td")
        ref = cols[0].find("a")
        name = list(ref.strings)[0]
        link = wiki + ref["href"][1:]
        try:
            stats = [float(col.contents[0]) for col in cols[1:15]]
            stats = [int(s) if int(s) == s else s for s in stats]
            piece = ArmorPiece(name, link, *stats)
            print(piece)
            pieces[slot].append(piece)
        except Exception as e:
            print("error parsing " + name + " (" + link + ")")
            print([col.contents[0] for col in cols[1:15]])
            print(e)
print("Done.\nWriting to file...")
with open("armor_data.json", "w") as file:
    json.dump(pieces, file, indent=4, default=vars)
print("Done.")