import json
import os

from utils.json import formatting

JSON_DIR = 'data'
JSON_DB = 'db.json'
HEADER = ('multiverse_id', 'number' , 'name', 'set')


def main():
    # Steps
    # Open all JSON files in data/
    # Create a list of tuples with the fields of interest i.e. multiverse_id,
    # number, name and set
    # json.dump this data to a db.json file with all files of interest
    db = []
    with open(f'{JSON_DB}', 'w') as fout:
        for file in os.listdir(JSON_DIR):
            name, ext = os.path.splitext(file)
            if ext == '.json':
                with open(os.path.join(JSON_DIR, file), 'r') as f:
                    for entry in json.load(f):
                        #card = tuple(entry.get(h, 'NA') for h in HEADER)
                        #db.append(dict(zip(HEADER, card)))
                        card = {h: entry.get(h, 'NA') for h in HEADER}
                        db.append(card)
        json.dump(db, fout, **formatting)


if __name__ == '__main__':
    main()
