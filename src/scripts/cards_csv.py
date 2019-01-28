import csv
import re

from mtgsdk import Card


LANGUAGE = 'English'
SET = 'rna'
RESTVAL = 'NA'
EXTRASACTION = 'raise'
DIALECT = 'unix'

def get_fieldnames(o):
    for k, v in o.__dict__.items():
        yield k


if __name__ == '__main__':
    # Example: siply utilized to query "fieldnames"
    fieldnames = get_fieldnames(Card
            .where(set=SET)
            .where(page=1)
            .where(pageSize=1)
            .all()[0])

    with open(f'data/{SET}.json', 'w') as f:
        writer = csv.DictWriter(f,
                    fieldnames=list(fieldnames),
                    restval=RESTVAL,
                    extrasaction=EXTRASACTION,
                    dialect=DIALECT)
        writer.writeheader()

        for c in Card \
                    .where(language=LANGUAGE) \
                    .where(set=SET) \
                    .all():
            # d = {}
            # for k in fields:
            #     v = getattr(card, k, None)
            #     if v:
            #         if isinstance(v, str):
            #             d[k] = re.sub('\n', ' ', v)
            #         else:
            #             d[k] = v
            #     else:
            #         d[k] = None
            writer.writerow(dict(c.__dict__.items()))
