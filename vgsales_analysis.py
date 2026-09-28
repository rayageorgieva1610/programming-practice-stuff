from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "vgsales.csv"

# Data exploration

games = pd.read_csv(csv_path)

print(games.head())

# Creating a folder for plots

plots_dir = base_dir / "plots"
plots_dir.mkdir(exist_ok=True)


# Top 5 games by year 

def top_games_by_year(games, year):
    """Return the 5 best-selling games from a given year.
    :param games: pandas.DataFrame
    :param year: int
    :return: pandas.DataFrame
    """
    games_in_year = games[games["Year"] == year]
    return games_in_year.nlargest(5, "Global_Sales")


year = int(input("Enter a year: "))

top_5 = top_games_by_year(games, year)

print(f"\nTop 5 best-selling games in {year}:")
print(top_5[["Name", "Platform", "Global_Sales"]])

# Plot the results 

plt.figure(figsize=(10, 6))

plt.bar(top_5["Name"], top_5["Global_Sales"])

plt.title(f"Top 5 Best-Selling Games in {year}")
plt.xlabel("Game")
plt.ylabel("Global Sales (millions)")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()


plot_path = plots_dir / f"top_5_games_{year}.png"
plt.savefig(plot_path)

print(f"\nPlot saved to: {plot_path}")


plt.close()

# Comparative analysis of global sales between two years

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