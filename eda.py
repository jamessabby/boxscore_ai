import sqlite3
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency


conn = sqlite3.connect("boxscore_ai.db")
df = pd.read_sql("SELECT * FROM games", conn)
conn.close()

# checks whether is being at Home or Away correlates the Wins and Losses
df["is_home"] = np.where(df["MATCHUP"].str.contains("vs.").astype(int), 1, 0)
cross_tab = pd.crosstab(df["is_home"], df["WL"])
print(cross_tab)

chi2 = chi2_contingency(cross_tab)
p_value = chi2[1]
print(f"P-value: {p_value:.5f}")

# checks whether the teams winning in rebounding win more games
cross_tab2 = pd.crosstab(df["REB"], df["WL"])
print(cross_tab2)

chi2_2 = chi2_contingency(cross_tab2)
p_value = chi2_2[1]
print(f"P-value: {p_value:.5f}")
