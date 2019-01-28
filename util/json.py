import json


def write_json(data, fname):
    with open(fname, 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)
