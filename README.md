# programming-practice-stuff
just a repo where i will be committing code in my free time, to practice. 
# Video Game Sales Analysis

This is a small data analysis project I made to practice working with datasets in Python.

I'm using a video game sales dataset (`vgsales.csv`) and pandas to explore the data and answer some basic questions about video game sales.

## What I'm looking at

Some of the things I want to look at are:

- the best selling games
- sales across different genres
- the most popular platforms
- how sales changed over the years
- differences between sales in North America, Europe and Japan

## Dataset

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

## Tools

- Python
- pandas
- matplotlib

## Files

`vgsales.csv` contains the dataset.

`vgsales_analysis.py` contains the code I'm using to explore and analyze it.

## Progress


So far, the project can load and explore the dataset and find the top 5 best-selling games for any year entered by the user.

I'm going to keep adding new analyses and visualizations as I work on the project.
