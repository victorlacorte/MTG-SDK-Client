import pytest
from mtgsdk import Card

from src.scripts.cards_csv import get_fieldnames


@pytest.fixture(scope='module')
def card():
    return Card.where(set='rna').where(page=1).where(pageSize=1).all()[0]

@pytest.mark.skip
def test_initial():
    c = Card.find(386616)
    assert c.name == 'foo'

def test_get_fieldnames(card):
    print(list(get_fieldnames(card)))
    assert False
