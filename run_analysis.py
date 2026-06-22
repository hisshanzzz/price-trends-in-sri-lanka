"""Run cost-of-living analysis."""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
ROOT = Path(__file__).parent
DATA = ROOT / "data" / "cost_of_living_sri_lanka.csv"
CHARTS = ROOT / "charts"
CHARTS.mkdir(exist_ok=True)
BASELINE = pd.Timestamp("2023-01-01")
def main():
    df = pd.read_csv(DATA)
    df["date"] = pd.to_datetime(df["year"].astype(str) + "-" + df["month"].astype(str) + "-01")
    plt.figure(figsize=(11, 6))
    for cat, g in df.groupby("category"):
        s = g.sort_values("date")
        plt.plot(s["date"], s["price_lkr"], marker="o", linewidth=1.8, label=cat)
    plt.title("Essential Prices in Sri Lanka (2023-2024)")
    plt.xlabel("Month"); plt.ylabel("Price (LKR)")
    plt.legend(loc="upper left", fontsize=8); plt.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(CHARTS / "price_trends.png", dpi=150); plt.close()
    base = df[df["date"] == BASELINE].set_index("category")["price_lkr"]
    latest_date = df["date"].max()
    latest = df[df["date"] == latest_date].set_index("category")["price_lkr"]
    pct = ((latest - base) / base * 100).sort_values(ascending=False)
    plt.figure(figsize=(8, 5)); pct.plot(kind="bar", color="#2980b9")
    plt.title(f"Price Rise Since Jan 2023 (to {latest_date.strftime('%b %Y')})")
    plt.xlabel("Category"); plt.ylabel("Percent change (%)")
    plt.xticks(rotation=30, ha="right"); plt.tight_layout()
    plt.savefig(CHARTS / "pct_change_baseline.png", dpi=150); plt.close()
    print("Fastest-rising:", pct.idxmax(), f"({pct.max():.1f}%)")
    print("Charts saved to:", CHARTS)
if __name__ == "__main__":
    main()
