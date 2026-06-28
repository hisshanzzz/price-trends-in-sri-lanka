# Cost of Living Pulse

Jupyter notebook analyzing how everyday essentials got more expensive in Sri Lanka (2023-2024).

## Why

Families feel prices rising every month, but the pattern is hard to see in isolation. As an AI and Data Science student in Sri Lanka, I built this to visualize which essentials rose fastest — rice, fuel, electricity, transport — so the story is clear in charts, not guesswork.

## What this project does

- Loads monthly price data for seven essential categories
- Plots price trends over 24 months
- Compares percent change from January 2023 baseline
- Writes short conclusions about affordability pressure

## Run

```bash
pip install -r requirements.txt
jupyter notebook notebook/cost_of_living_analysis.ipynb
```

Or run the script version (saves charts to charts/):

```bash
py run_analysis.py
```

## Data

data/cost_of_living_sri_lanka.csv — monthly prices in LKR by category (2023-2024).
Values are synthetic but realistic for learning and visualization (not official CPI).

## Categories

| Category | What it represents |
|----------|-------------------|
| rice_kg | 1 kg rice |
| bread_loaf | Standard loaf |
| milk_litre | 1 litre fresh milk |
| chicken_kg | 1 kg chicken |
| petrol_litre | 92 octane per litre |
| electricity_kwh | Per kWh unit charge |
| bus_fare | Average single bus fare |

## Charts

After running, check charts/ for:

- price_trends.png — all categories over time
- pct_change_baseline.png — percent rise since Jan 2023

See [charts/README.md](charts/README.md) for how outputs are generated.

## Docs

| File | Purpose |
|------|---------|
| [data/README.md](data/README.md) | Data source notes and official CPI link |
| [data/COLUMNS.md](data/COLUMNS.md) | CSV column reference |
| [notebook/README.md](notebook/README.md) | Notebook overview |
| [docs/RUN.md](docs/RUN.md) | Run commands and example output |
| [docs/LIMITATIONS.md](docs/LIMITATIONS.md) | Synthetic data and scope notes |

## License

MIT — see [LICENSE](LICENSE).

## Author

Mohamed Jaufer Mohamed Hisshan — AI and Data Science student, Sri Lanka
