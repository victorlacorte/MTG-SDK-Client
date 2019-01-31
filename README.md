[MTG Python SDK](https://github.com/MagicTheGathering/mtg-sdk-python) client
that generates a spreadsheet with cards info for collection management.

The initial focus will be on MTG Arena legal sets.

### Test
Without pytest:
`python setup.py pytest`

Otherwise:
`pytest`


### Doc
`c = mtgsdk.Card...`, `c.__dict__` or `vars(c)` returns what we are expecting
from Card objects

### Card
#### Important keys
multiverse_id, name, number and set


### Issues
* Cards with "transform" on their text are counting twice for their rarities or
  set; something to keep in mind

### Golgari and Jund comparison
Decklist:
Maindeck

Before
24 lands

4 Woodland Cemetery
4 Overgrown Tomb
8 Forest
5 Swamp
2 Memorial to Folly
1 Detection Tower

(G/B 16/15, 12 untapped G for Llanowar)

After
23 lands

4 Woodland Cemetery
4 Overgrown Tomb
4 Blood Crypt
4 Stomping Grounds
4 Forest
2 Memorial to Folly
1 Dragonskull Summit

(G/B/R 16/15/9, 12 untapped G for Llanowar)
------------------------------------------------------------------------------

4 Llanowar Elves
4 Merfolk Branchwalker
1 Seekers' Squire
4 Wildgrowth Walker
2 Midnight Reaper
4 Jadelight Ranger
2 Ravenous Chupacabra
3 Carnage Tyrant

2 Cast Down
1 Domri, Chaos Bringer
4 Vraska's Contempt
3 Vivien Reid
3 Find // Finality

SB
4 Duress
2 Cast Down
1 Assassin's Trophy
1 Midnight Reaper
2 Thrashing Brontodon
3 Rhythm of the Wild
1 Domri, Chaos Bringer
1 Vraska, Relic Seeker

Cry of the Carnarium? Golden Demise?

------------------------------------------------------------------------------

RDW
-4 Llanowar Elves: very weak to Chainwhirler. Any other pingers?
-2 Carnage Tyrant: slow, only good on the play vs. Experimental Frenzy and even
then feels weak

+4 Duress: the idea is to protect Wildgrowth Walker vs. Lava Coil (Walker +
explorer in the same turn) or instant 3 damage spells (Lightning Strike and
Wizard's Lightning)
+1 Wildgrowth Walker
