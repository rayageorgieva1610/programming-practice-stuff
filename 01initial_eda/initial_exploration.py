from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

base_dir = Path(__file__).resolve().parent.parent
csv_path = base_dir / "data" / "vgsales.csv"

# Data exploration

games = pd.read_csv(csv_path)

print(games.head())