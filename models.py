from sqlalchemy import Integer, String, Float, Date
from sqlalchemy.orm import mapped_column, Mapped
from database import Base
from datetime import date


class Games(Base):
    __tablename__ = "games"

    game_id: Mapped[int] = mapped_column(
        "GAME_ID", Integer, primary_key=True, index=True
    )
    team_id: Mapped[int] = mapped_column(
        "TEAM_ID", Integer, primary_key=True, index=True
    )
    season_id: Mapped[int] = mapped_column("SEASON_ID", Integer, nullable=False)
    game_date: Mapped[date] = mapped_column("GAME_DATE", Date, nullable=False)
    team_abbreviation: Mapped[str] = mapped_column(
        "TEAM_ABBREVIATION", String, nullable=False
    )
    matchup: Mapped[str] = mapped_column("MATCHUP", String, nullable=False)
    game_results: Mapped[str] = mapped_column("WL", String, nullable=False)
    points: Mapped[int] = mapped_column("PTS", Integer, nullable=False)
    assists: Mapped[int] = mapped_column("AST", Integer, nullable=False)
    steals: Mapped[int] = mapped_column("STL", Integer, nullable=False)
    blocks: Mapped[int] = mapped_column("BLK", Integer, nullable=False)
    tov: Mapped[int] = mapped_column("TOV", Integer, nullable=False)
    fgm: Mapped[int] = mapped_column("FGM", Integer, nullable=False)
    fga: Mapped[int] = mapped_column("FGA", Integer, nullable=False)
    fg_pct: Mapped[float] = mapped_column("FG_PCT", Float, nullable=False)
    fg3m: Mapped[int] = mapped_column("FG3M", Integer, nullable=False)
    fg3a: Mapped[int] = mapped_column("FG3A", Integer, nullable=False)
    ftm: Mapped[int] = mapped_column("FTM", Integer, nullable=False)
    fta: Mapped[int] = mapped_column("FTA", Integer, nullable=False)
    oreb: Mapped[int] = mapped_column("OREB", Integer, nullable=False)
    dreb: Mapped[int] = mapped_column("DREB", Integer, nullable=False)
    total_rebs: Mapped[int] = mapped_column("REB", Integer, nullable=False)
