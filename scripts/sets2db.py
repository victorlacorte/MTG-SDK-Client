import json
import os

from utils.json import formatting

JSON_DIR = 'data'
HEADER = ('multiverse_id', 'number' , 'name', 'set')


def main():
    # Steps
    # Open all JSON files in data/
    # Create a list of tuples with the fields of interest i.e. multiverse_id,
    # number, name and set
    # json.dump this data to a db.json file with all files of interest
    for file in os.listdir(JSON_DIR):
        if file.endswith('.json'):
            print(os.path.join(JSON_DIR, file))


if __name__ == '__main__':
    main()
