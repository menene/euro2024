# -*- coding: utf-8 -*-
"""02 Euro Versus.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qf1LGB0EaK4YKyrFYxu8ht217iMAZHFo
"""

import pandas as pd
import matplotlib.pyplot as plt

def determine_winner(row, team1, team2):
    if row["HomeTeamName"] == team1 and row["HomeTeamGoals"] > row["AwayTeamGoals"]:
        return team1
    elif row["HomeTeamName"] == team2 and row["HomeTeamGoals"] > row["AwayTeamGoals"]:
        return team2
    elif row["AwayTeamName"] == team1 and row["AwayTeamGoals"] > row["HomeTeamGoals"]:
        return team1
    elif row["AwayTeamName"] == team2 and row["AwayTeamGoals"] > row["HomeTeamGoals"]:
        return team2
    else:
        return "Draw"

def head_to_head(df, team1, team2):
    head_to_head = df.query(
        f"(HomeTeamName == '{team1}' and AwayTeamName == '{team2}') or (AwayTeamName == '{team1}' and HomeTeamName == '{team2}')"
    ).copy()

    head_to_head["Winner"] = head_to_head.apply(
        determine_winner,
        axis=1,
        args=(team1, team2)
    )

    match_counts = (
        head_to_head["Winner"]
        .value_counts()
        .reindex([team1, team2, "Draw"], fill_value=0)
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    match_counts.plot(kind="bar", ax=ax)
    ax.set_title(f"{team1} vs {team2}")
    ax.set_xlabel("Resultado")
    ax.set_ylabel("Partidos")
    plt.xticks(rotation=0)
    plt.show()

df = pd.read_csv(
    "https://raw.githubusercontent.com/menene/euro2024/main/uefa_euro_matches.csv",
    encoding="utf8",
)

df["HomeTeamName"] = df["HomeTeamName"].str.rstrip()
df["AwayTeamName"] = df["AwayTeamName"].str.lstrip()

head_to_head(df, "France", "Spain")

team1 = input("Ingrese el nombre del primer equípo: ")
team2 = input("Ingrese el nombre del primer equípo: ")

head_to_head(df, team1, team2)