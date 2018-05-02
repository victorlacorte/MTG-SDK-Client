import csv
import re

import mtgsdk


if __name__ == '__main__':
    fields = [
        'id',
        'multiverse_id',
        'number',
        'name',
        'image_url',
        'set',
        'set_name',
        'rarity',
        'cmc',
        'mana_cost',
        'colors',
        'color_identity',
        'type',
        'supertypes',
        'subtypes',
        'loyalty',
        'power',
        'toughness',
        'rulings',
        'text',
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

    sets = [
        'dom',
        'rix',
        'xln']

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
        for s in sets:
            for card in mtgsdk.Card \
                            .where(language='English') \
                            .where(set=s) \
                            .all():
                d = {}
                for k in fields:
                    v = getattr(card, k, None)
                    if v:
                        if isinstance(v, str):
                            d[k] = re.sub('\n', ' ', v)
                        else:
                            d[k] = v
                    else:
                        d[k] = None
                writer.writerow(d)
