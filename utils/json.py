import json

formatting = dict(sort_keys=True, indent=4, ensure_ascii=False)

def write_json(data, fname):
    with open(fname, 'w') as f:
        json.dump(data, f, **formatting)
