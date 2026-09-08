from nba_api.stats.endpoints import leaguegamelog
import pandas as pd
import requests
from database import init_db
import sqlite3

# creates boxscore_ai.db and games table
init_db()

gamelog = leaguegamelog.LeagueGameLog(season="2024-25")
df = gamelog.get_data_frames()[0]

cols = [
    "GAME_ID",
    "TEAM_ID",
    "SEASON_ID",
    "GAME_DATE",
    "TEAM_ABBREVIATION",
    "MATCHUP",
    "WL",
    "PTS",
    "AST",
    "STL",
    "BLK",
    "TOV",
    "FGM",
    "FGA",
    "FG_PCT",
    "FG3M",
    "FG3A",
    "FTM",
    "FTA",
    "OREB",
    "DREB",
    "REB",
]
filtered_df = df[cols].copy()

conn = sqlite3.connect("boxscore_ai.db")

filtered_df["GAME_ID"] = filtered_df["GAME_ID"].astype(
    int
)  # matches the data type in models.py where game_id is an integer

saved_ids = pd.read_sql("SELECT GAME_ID FROM games", conn)[
    "GAME_ID"
]  # stores the current games as the initial values

new_games = filtered_df[
    ~filtered_df["GAME_ID"].isin(saved_ids)
]  # only stores the games that aren't in the current games

new_games.to_sql("games", conn, if_exists="append", index=False)

conn.commit()
conn.close()
