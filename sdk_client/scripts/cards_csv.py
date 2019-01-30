import csv
import re

import mtgsdk


if __name__ == '__main__':
    fields = [
        'cmc',
        'color_identity',
        'colors',
        'id',
        'image_url',
        'loyalty',
        'mana_cost',
        'multiverse_id',
        'name',
        'number',
        'power',
        'rarity',
        'rulings',
        'set',
        'set_name',
        'subtypes',
        'supertypes',
        'text',
        'toughness',
        'type',
        'variations']
        #'original_type',
        #'artist',
        #'border',
        #'flavor',
        #'foreign_names',
        #'hand',
        #'layout',
        #'legalities',
        #'life',
        #'names',
        #'original_text',
        #'printings',
        #'release_date',
        #'reserved',
        #'source',
        #'starter',
        #'timeshifted',
        #'watermark']

    #sets = ('m19,')

    restval = 'NA'
    extrasaction = 'ignore'
    dialect = 'unix'

    with open('cards.csv', 'w') as f:
        writer = csv.DictWriter(f,
                    fieldnames=fields,
                    restval=restval,
                    extrasaction=extrasaction,
                    dialect=dialect)
        writer.writeheader()
        #for s in sets:
        m19 = mtgsdk.Card.where(set='m19').all()
        for card in m19:
            d = {}
            for k in fields:
                v = getattr(card, k, None)
                if v:
                    if isinstance(v, str):
                        d[k] = re.sub('\n', ' ', v)
                    else:
                        # Numbers, etc?
                        d[k] = v
                else:
                    d[k] = None
            writer.writerow(d)
