from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

base_dir = Path(__file__).resolve().parent.parent
csv_path = base_dir / "data" / "vgsales.csv"

games = pd.read_csv(csv_path)

plots_dir = Path(__file__).resolve().parent / "plots"
plots_dir.mkdir(exist_ok=True)

def compare_years(games, year1, year2):
    """
    Compare total global video game sales between two years.

    :param games: pandas.DataFrame
    :param year1: int
    :param year2: int
    :return: pandas.Series
    """
    sales_year1 = games[games["Year"] == year1]["Global_Sales"].sum()
    sales_year2 = games[games["Year"] == year2]["Global_Sales"].sum()

    comparison = pd.Series({
        year1: sales_year1,
        year2: sales_year2
    })

    return comparison


year1 = int(input("\nEnter the first year to compare: "))
year2 = int(input("Enter the second year to compare: "))

comparison = compare_years(games, year1, year2)

print("\nTotal global sales:")
print(comparison)

# Comparative analysis + visualization

plt.figure(figsize=(8, 5))

plt.bar(
    comparison.index.astype(str),
    comparison.values
)

plt.title(f"Global Video Game Sales: {year1} vs {year2}")
plt.xlabel("Year")
plt.ylabel("Global Sales (millions)")

plt.tight_layout()

plot_path = plots_dir / f"sales_comparison_{year1}_{year2}.png"
plt.savefig(plot_path, dpi=300, bbox_inches="tight")

print(f"\nComparison plot saved to: {plot_path}")

plt.show()