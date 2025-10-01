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

## Pattern colouring utility

`pattern_coloring.py` converts the CSV that holds your card patterns into an
Excel workbook with one card per column. Cards that share a suit are filled
with the same background colour so you can immediately see suited groupings.

### Running the exporter

1. Install Python 3.9+ and the dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

2. Place your CSV anywhere on disk (it does *not* need to live inside this
   repository). The file only needs two columns named `pattern` and
   `combinations`. You can use `sample_patterns.csv` as a template for building
   your own sheet.

3. Run the exporter, pointing it at the location of your CSV and the desired
   Excel output path:

   ```bash
   python pattern_coloring.py /path/to/your_patterns.csv /path/to/output.xlsx
   ```

   If you omit the second argument, the workbook will be created right next to
   your CSV using the same name but with an `.xlsx` extension. The script works
   equally well on Windows, macOS, or Linux anywhere that Python is available.

Once the command finishes, open the generated Excel file in your preferred
spreadsheet application to view the colour-coded cards.
