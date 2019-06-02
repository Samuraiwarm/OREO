# ☆OREO☆

Oreo generator because why not

---

# Dependencies
- python3

# How to run

For one oreo, run `python3 oreo.py`

To edit the oreo ratio, follow the conventions in `oreo.py`. 2 variables are allowed to be edited: `oreo_prob` and `oreo_terminate`

```
# init
oreo_prob = {
	'O': 180, # cookie
	'RE': 45, # cream
	'CRE': 30, # chocolate cream
	'SRE': 20, # strawberry cream
}
oreo_terminate = 0.1 # probability of terminating oreo sequence
```

Sample output of `oreo.py`

```
OSREOOOSREOOOOOSRECREOOCREOOREOO
{'O': 15, 'RE': 1, 'CRE': 2, 'SRE': 3}
```

For multiple oreos, run `python3 multiOreo.py` and input the number of oreo sets when prompted.

Sample output of `multiOreo.py`
```
> How many sets of OREOs do you want? 9001
...
...
...
OOOOREOORE
RECREOOOOOOREOOOREOSRE
OOOO
OOOCRE

Longest oreo = OSREREOOOOOOREOREREOOREOOOSREOOOREOOOREOOORESRESREOOCREREREOREOORECREOREOOOOOOOOOOOREREOCREOOOOOREOOOSREOO , length = 74
oreo count: {'O': 50, 'RE': 16, 'CRE': 3, 'SRE': 5}
```

# Todo
- Generated oreo images
- Hopefully random reviews from the output