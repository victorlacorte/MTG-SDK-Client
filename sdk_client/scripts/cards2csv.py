import csv
import json
import sys

from sdk_client import card_utils


def main():
    set_name = sys.argv[1]
    with open(f'tests/data/{set_name}.json', 'r') as f:
        cards = json.load(f)
        cs = card_utils.CardSet(cards)
        cs.to_csv(f'{set_name}.csv')

def explicit_conversion():
    set_name = sys.argv[1]
    with open(f'mtg_sdk_client/data/{set_name}.json', 'r') as f:
        cards = json.load(f)
        cs = card_utils.CardSet(cards)

        with open(f'{set_name}.csv', 'w') as f:
            writer = csv.DictWriter(f,
                        fieldnames=(['set', 'number', 'name', 'rarity']),
                        restval='NA',
                        extrasaction='ignore',
                        dialect='unix')
            writer.writeheader()

            for card in cs:
                writer.writerow(card)

if __name__ == '__main__':
    # main()
    explicit_conversion()
