rom pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "vgsales.csv"

# Data exploration

games = pd.read_csv(csv_path)

print(games.head())

# Creating a folder for plots...

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


plt.show()