# Boxscore AI — NBA Game Outcome Prediction

A Python machine-learning project that predicts NBA team wins using historical box-score statistics, opponent trends, and home-court advantage. Built using 2024–25 NBA regular-season data.

## Results

Three classifiers were evaluated on a chronological holdout of NBA games:

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | **0.6345** | **0.6345** | **0.6345** | **0.6345** | **0.6768** |
| Random Forest | 0.5803 | 0.5826 | 0.5663 | 0.5743 | 0.6271 |
| XGBoost | 0.6245 | 0.6250 | 0.6225 | 0.6237 | 0.6538 |

These are **team-row** results verified by running the cleaned notebook with the supplied SQLite database. The earlier interactive experiment reported slightly different Random Forest and XGBoost scores (0.5823 and 0.6305 accuracy respectively), likely due to differences in row ordering or notebook state; the cleaned run is the reproducible reference. Each NBA game has two team rows. The Logistic Regression experiment also produced exactly one predicted winner in each of 249 held-out games. Re-run `model.ipynb` to reproduce and verify metrics with the supplied database and installed package versions.

## Methodology

1. Load 2024–25 game logs from a local SQLite database (`games` table).
2. Compute rolling means of points, field-goal percentage, assists, and rebounds from each team's **previous five games**. `shift(1)` excludes current-game statistics to prevent target leakage.
3. Match each team with its opponent using `GAME_ID` and include both teams' historical averages, plus an `IS_HOME` indicator (nine model features).
4. Keep only complete games with two team rows; split chronologically by game date, keeping both teams in the same partition.
5. Fit Logistic Regression (with train-only scaling), Random Forest, and XGBoost; evaluate accuracy, precision, recall, F1, ROC-AUC, confusion matrices, and game-level consistency.

## Setup

Python 3.10+ recommended.

```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter notebook model.ipynb
```

The provided review ZIP includes `boxscore_ai.db` for local reproducibility. For a fresh database, run `python main.py` with network access to the NBA API. **Note:** the existing ingestion script is exploratory and may require changes to handle database refreshes or partial imports robustly. The `.gitignore` intentionally excludes `.db` files, so GitHub clones must create the database first or obtain it separately.

## Project files

- `model.ipynb` — cleaned end-to-end feature engineering, training, and evaluation.
- `eda.ipynb` — exploratory data analysis.
- `unsupervised.ipynb` — separate exploratory unsupervised-learning notebook.
- `main.py`, `database.py`, `models.py` — data ingestion and database schema.
- `run_query.py` — SQL exploration helper.

## Limitations

- One historical season only; no independent-season evaluation.
- Limited features; no injuries, lineup availability, betting lines, or team-strength ratings.
- Probability outputs are not validated for calibration.
- Performance is retrospective, not a guarantee for future games.
- Training is notebook-based; no deployed prediction API or production pipeline is claimed.

## Next steps

Evaluate on a new season, test calibration, and improve data ingestion/reproducibility.
