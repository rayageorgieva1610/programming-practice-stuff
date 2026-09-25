from pathlib import Path
import pandas as pd

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "vgsales.csv"

# --- Data exploration ---

games = pd.read_csv(csv_path)

print(games.head())

# --- Top 5 games by year ---

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