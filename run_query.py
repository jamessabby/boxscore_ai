import sqlite3

DB_PATH = "boxscore_ai.db"

with open("queries.sql", "r") as f:
    sql = f.read()

with sqlite3.connect(DB_PATH) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # Split by semicolon to support multiple queries in one file
    statements = [s.strip() for s in sql.split(";") if s.strip()]
    for i, stmt in enumerate(statements, 1):
        print(f"\n--- Query {i} ---")
        cur.execute(stmt)
        rows = cur.fetchall()
        for row in rows:
            print(dict(row))
