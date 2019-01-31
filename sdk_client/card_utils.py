from collections import UserDict, UserList
import csv
import re


class Card(UserDict):
    '''Represents a Magic card.'''

    def __init__(self, card):
        if isinstance(card, dict):
            self.data = card
        else:
            # This may be unnecessary: it covers the scenario in which we
            # receive a mtgsdk.Card 
            self.data = vars(card)

    def foreign_name(self, lang, *, imageUrl=False, multiverseid=False):
        '''
        foreign_names is a list of languages (dicts) and each has the following
        keys:

        * imageUrl
        * language
        * multiverseid
        * name

        for now we are interested in the language-name pair
        '''
        for d in self.data['foreign_names']:
            if d['language'] == lang:
                return d['name']
        return 'NA'

    def color(self):
        if 'colors' in self.data:
            c = self.data['colors']
            if len(c) == 1:
                return c[0].lower()
            elif len(c) > 1:
                # Multiple colors are classified the same way
                return 'gold'
            else:
                raise ValueError(f'{self.card}')
        else:
            t = self.data['type'].lower()
            # We might have issues with artifact lands: should they be
            # classified as artifacts or lands?
            for val in ('artifact', 'basic land', 'land'):
                if val in t:
                    return val
        return 'NA'  # maybe it should be 'colorless'


class CardSet(UserList):
    '''
    Represents a collection of Magic cards, likely from the same Magic set.
    '''
    def __init__(self, cards=[]):
        data = []
        for card in cards:
            data.append(Card(card))
        self.data = data

    def fieldnames(self):
        '''
        Return the aggregated result of iterating through all cards and
        collecting their keys (attributes).
        '''
        # names = set()
        # for card in self.data:
        #     for k in card.keys():
        #         names.add(k)
        # return names
        return {k for card in self.data for k in card.keys()}

    def to_csv(self, filename, *,
            lang='Portuguese (Brazil)',
            restval='NA',
            extrasaction='ignore',
            dialect='unix'):
        '''
        Something about this function does not seem right. Maybe it is due to
        it being very unflexible or "customized"
        '''
        names = self.fieldnames()
        names.add('color')
        names.add(lang.lower())
        names.discard('foreign_names')
        names.discard('colors')

        # We could probably pass a newline='' argument rather than performing a
        # re.sub
        with open(filename, 'w') as f:
            writer = csv.DictWriter(f,
                        fieldnames=sorted(names),
                        restval=restval,
                        extrasaction=extrasaction,
                        dialect=dialect)
            writer.writeheader()

            for card in self.data:
                card['color'] = card.color()
                card[lang.lower()] = card.foreign_name(lang)
                for k, v in card.items():
                    if isinstance(v, str):
                        card[k] = re.sub('\n', ' ', v)
                writer.writerow(card)
