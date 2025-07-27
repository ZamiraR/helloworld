# hello world
well lets get started

## Big O Strategy Module

This repository now includes `big_o_strategy.py`, which contains
simple heuristics for the Big O (five-card Omaha hi/lo) poker variant.

The module exposes two primary functions:

* `evaluate_hand(hole_cards)` - rates a starting hand on a scale of 1-10.
* `preflop_action(hole_cards)` - suggests `raise`, `call`, or `fold`
  based on the rating.

Run the module directly to see an example evaluation:

```bash
python big_o_strategy.py
```
