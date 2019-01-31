import csv
import re

from mtgsdk import Card
from utils.json import write_json


LANGUAGE = 'English'
SET = 'rna'
RESTVAL = 'NA'
EXTRASACTION = 'raise'
DIALECT = 'unix'

def get_fieldnames(o):
    for k, v in o.__dict__.items():
        yield k

def get_collection(set_name, language):
    for c in Card \
              .where(language=language) \
              .where(set=set_name) \
              .all():
        yield dict(c.__dict__.items())


if __name__ == '__main__':
    write_json([c for c in get_collection(SET, LANGUAGE)],
               f'{SET}.json')
