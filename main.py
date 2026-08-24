from nba_api.stats.endpoints import leaguegamelog
import pandas as pd
import sqlite3

gamelog = leaguegamelog.LeagueGameLog(season="2025-26")

df = gamelog.get_data_frames()[0]
print(df.info())
df.to_csv("leaguegamelog.csv", index=False)

data = pd.read_csv("leaguegamelog.csv")
# print(data.columns.tolist())

filtered_data = pd.read_csv(
    "leaguegamelog.csv",
    usecols=[
        "SEASON_ID",
        "TEAM_ID",
        "TEAM_ABBREVIATION",
        "GAME_ID",
        "GAME_DATE",
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
    ],
)
# print(filtered_data.info())

conn = sqlite3.connect("boxscore_ai.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS games (
        GAME_ID INT NOT NULL, 
        TEAM_ID INT NOT NULL,
        SEASON_ID INT NOT NULL,
        GAME_DATE DATE NOT NULL,
        TEAM_ABBREVIATION TEXT,
        MATCHUP TEXT NOT NULL, 
        WL TEXT NOT NULL,
        PTS INT NOT NULL,
        AST INT NOT NULL,
        STL INT NOT NULL,
        BLK INT NOT NULL,
        TOV INT NOT NULL,
        FGM INT NOT NULL,
        FGA INT NOT NULL, 
        FG_PCT REAL NOT NULL,
        FG3M INT NOT NULL,
        FG3A INT NOT NULL,
        FTM INT NOT NULL, 
        FTA INT NOT NULL,
        PRIMARY KEY (GAME_ID, TEAM_ID)
    )
    """
)

filtered_data.to_sql("games", conn, if_exists="append", index=False)

conn.commit()
conn.close()
