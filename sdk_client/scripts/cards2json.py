import json

import mtgsdk as mtg


magic_sets = ('grn',)

def main():
    for s in magic_sets:
        cards = [vars(c) for c in mtg.Card.where(set=s).all()]
        with open(f'tests/data/{s}.json', 'w') as f:
            json.dump(cards, f, indent=4, sort_keys=True)

if __name__ == '__main__':
    main()
