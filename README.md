# programming-practice-stuff

just a repo where i will be committing code in my free time, to practice.

# Video Game Sales Analysis

This is a small data analysis project I made to practice working with datasets in Python.

I'm using a video game sales dataset (`vgsales.csv`) and pandas to explore the data and answer some basic questions about video game sales.

# What I'm looking at

Some of the things I want to look at are:

- the best selling games
- sales across different genres
- the most popular platforms
- how sales changed over the years
- differences between sales in North America, Europe and Japan

# Dataset

The dataset contains information about video games such as:

- name
- platform
- year of release
- genre
- publisher
- North American sales
- European sales
- Japanese sales
- other sales
- global sales

The sales figures are in millions of copies.

## Current Analysis

### Data Exploration

The first part of the project explores the dataset by displaying the first few rows and looking at the available data.

### Top 5 best-selling games by year

The program lets the user enter a year and returns the five best-selling games released that year based on global sales.

For example, for 2015:

| Game | Platform | Global Sales (millions) |
|---|---|---:|
| Call of Duty: Black Ops 3 | PS4 | 14.24 |
| FIFA 16 | PS4 | 8.49 |
| Star Wars Battlefront (2015) | PS4 | 7.67 |
| Call of Duty: Black Ops 3 | XOne | 7.30 |
| Fallout 4 | PS4 | 6.96 |

The year is entered by the user when the program runs, so the analysis can be repeated for different years without changing the code.

### Visualization

The program creates a bar chart for the selected year, comparing the global sales of the five best-selling games.

These plots are automatically saved in the `02top_5_games/plots/` folder so I can keep the results from different years.

### Comparing global sales between two years

I also added a comparative analysis where the user can enter two years.

The program calculates the total global video game sales for each year and compares them using a bar chart.

The comparison plots are saved in the `03comparative_analysis/plots/` folder, which makes it easier to see how overall video game sales changed between two different years.

## Tools

- Python
- pandas
- matplotlib

## Project Structure

`data/vgsales.csv` contains the dataset.

`01initial_eda/initial_exploration.py` contains the initial data exploration.

`02top_5_games/top_games_by_year.py` contains the analysis and visualization of the top 5 best-selling games for a selected year.

`02top_5_games/plots/` contains the generated top 5 game visualizations.

`03comparative_analysis/compare_years.py` contains the comparison of total global sales between two selected years.

`03comparative_analysis/plots/` contains the generated comparison plots.

## Progress

So far, the project can load and explore the dataset, find the top 5 best-selling games for any year entered by the user, visualize those results, compare total global sales between two different years and save the generated plots.

I'm going to keep adding new analyses and visualizations as I work on the project.