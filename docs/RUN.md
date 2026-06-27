# Running the analysis

## Notebook

```bash
pip install -r requirements.txt
jupyter notebook notebook/cost_of_living_analysis.ipynb
```

Run all cells. Charts are shown inline; re-run `run_analysis.py` to save PNGs to `charts/`.

## CLI script

```bash
py run_analysis.py
```

Example output:

```
Fastest-rising: petrol_litre (42.3%)
Charts saved to: charts
```

Generated files:

- `charts/price_trends.png`
- `charts/pct_change_baseline.png`
