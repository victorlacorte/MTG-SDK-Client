import csv
import json

from sdk_client import card_utils


sets = ['m19', 'dom', 'rix', 'xln']

def color(card):
    if 'colors' in card:
        c = card['colors']
        if len(c) == 1:
            return c[0].lower()
        elif len(c) > 1:
            # Multiple colors are classified the same way
            return 'gold'
        else:
            raise ValueError(f'{card}')
    else:
        t = card['type'].lower()
        # We might have issues with artifact lands: should they be
        # classified as artifacts or lands?
        for val in ('artifact', 'basic land', 'land'):
            if val in t:
                return val
    return 'NA'  # maybe it should be 'colorless'


def main():
    with open('standard.csv', 'w') as fout:
        header = False
        for s in sets:
            with open(f'tests/data/{s}.json', 'r') as fin:
                cards = json.load(fin)

                writer = csv.DictWriter(fout,
                                        fieldnames=('name',
                                                    'image_url',
                                                    'set',
                                                    'number',
                                                    'color',
                                                    'rarity',
                                                    'cmc',
                                                    'layout'),
                                        restval='NA',
                                        extrasaction='ignore',
                                        dialect='unix')
                if not header:
                    writer.writeheader()
                    header = True

                for c in cards:
                    c['color'] = color(c)
                    writer.writerow(c)

if __name__ == '__main__':
    main()
