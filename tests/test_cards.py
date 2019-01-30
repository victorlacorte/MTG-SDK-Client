import json
import mtgsdk as mtg
import pytest

from sdk_client import card_utils


@pytest.fixture
def card():
    '''
    We should not perform GET requests to test our code. Instead, download some
    cards and save as JSON
    '''
    # card = mtg.Card.where(set='m19') \
    #                .where(page=1) \
    #                .where(pageSize=1) \
    #                .all()
    # return card[0]
    raise DeprecationWarning()

@pytest.fixture
def m19_cards():
    with open('tests/data/m19.json', 'r') as f:
        return json.load(f)

@pytest.fixture
def first_card(m19_cards):
    return m19_cards[0]

@pytest.mark.skip
def test_foreign_names(card):
    card_attr = vars(card)
    # print(card_attr)

    for elem in card_attr['foreign_names']:
        name = elem['name']
        lang = elem['language']
        if lang == 'Portuguese (Brazil)':
            card_attr['name_ptbr'] = name
            break

    print(card_attr['name'])
    print(card_attr['name_ptbr'])
    #assert False

@pytest.mark.skip(reason='Slow as fuck')
def test_extract_cards():
    cards = mtg.Card.where(set='m19').all()
    print(len(cards))
    assert False

def test_first_card(first_card):
    c = card_utils.Card(first_card)
    assert c.foreign_name('Portuguese (Brazil)') == 'Égide dos Céus'
    assert c.color() == 'white'

@pytest.mark.parametrize('n, expected', [
    (226, 'artifact'),
    (261, 'basic land'),
    pytest.param(261, 'land', marks=pytest.mark.xfail),
    (218, 'gold'),
    (248, 'land'),
    pytest.param(248, 'basic land', marks=pytest.mark.xfail),
])
def test_color(n, expected, m19_cards):
    for card in m19_cards:
        try:
            num = int(card['number'])
            if num == n:
                c = card_utils.Card(card)
                assert c.color() == expected
        except ValueError:
            continue

@pytest.mark.xfail(reason='Simple inspection')
def test_cardset(m19_cards):
    c = card_utils.CardSet(m19_cards)
    # c = card_utils.CardSet()
    # for card in m19_cards:
    #     c.append(card)
    print(sorted(c.fieldnames()))
    assert False
