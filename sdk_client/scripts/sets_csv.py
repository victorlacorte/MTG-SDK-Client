import csv

import mtgsdk

if __name__ == '__main__':
    all_sets = mtgsdk.Set.all()
    fields = [
        'code',
        'name',
        'gatherer_code',
        'old_code',
        'magic_cards_info_code',
        'release_date',
        'border',
        'type',
        'block',
        'online_only',
        'booster',
        'mkm_id',
        'mkm_name']
    restval = 'NA'
    extrasaction = 'ignore'
    dialect = 'unix'
    with open('sets.csv', 'w') as f:
        writer = csv.DictWriter(f,
                    fieldnames=fields,
                    restval=restval,
                    extrasaction=extrasaction,
                    dialect=dialect)
        writer.writeheader()
        for s in all_sets:
            writer.writerow({k: getattr(s, k, None) for k in fields})
