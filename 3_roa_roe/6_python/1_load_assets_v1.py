import os
from pathlib import Path

import psycopg2
from psycopg2.extensions import connection as Connection
from dotenv import load_dotenv

# I load my DB credentials from the .env file at the repo root
load_dotenv()

# I build my paths from this file's own location, so they work from any folder.
# This file sits in 6_python, the DDL is in 5_PostgreSQL, the CSV is in data.
SCHEMA_SQL_PATH: str = str(Path(__file__).resolve().parent.parent / "5_PostgreSQL" / "1_ddl.sql")
CLEAN_CSV_PATH: str = str(Path(__file__).resolve().parent.parent / "data" / "2_assets_clean_v1.csv")

EQUITY_CSV_PATH: str = str(Path(__file__).resolve().parent.parent / "data" / "3_equity_income_v1.csv")

# I keep one COPY statement per table
COPY_ASSETS_SQL: str = "COPY roa_roe.assets FROM STDIN WITH (FORMAT csv, HEADER true)"
COPY_EQUITY_SQL: str = "COPY roa_roe.equity_income FROM STDIN WITH (FORMAT csv, HEADER true)"

# I expect one row per quarter in my equity table
EXPECTED_EQUITY_ROWS: int = 6

# I expect exactly this many rows after the load
EXPECTED_ROW_COUNT: int = 300_000

# my konspekt totals, the same ones my generator locked in
TOTALS_BY_DATE: dict[str, float] = {
    "2024-Q1": 10_800.0,
    "2024-Q2": 11_200.0,
    "2024-Q3": 11_600.0,
    "2024-Q4": 12_400.0,
    "2025-Q1": 12_800.0,
    "2025-Q2": 13_200.0
}

# I allow a tiny float tolerance when I compare the sums
INVARIANT_TOLERANCE: float = 1e-4


def connect() -> Connection | None:
    """Open a connection to my PostgreSQL database using .env credentials."""
    try:
        # the names on the left are what psycopg2 expects, the values come from my .env
        conn = psycopg2.connect(
            dbname=os.getenv("PGDATABASE"),
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD"),
            host=os.getenv("PGHOST"),
            port=os.getenv("PGPORT")
        )
        print("Connected to DB")
        return conn
    except psycopg2.Error as error:
        print(f"An error has occurred: {error}")
        return None


def create_table(conn: Connection, schema_sql_path: str) -> None:
    """Run my DDL file to drop and recreate the assets table."""
    # I read the SQL text out of my DDL file
    with open(schema_sql_path, mode="r", encoding="utf-8") as file:
        create_table_query = file.read()

    with conn.cursor() as cur:
        cur.execute(create_table_query)

    conn.commit()  # Commit changes to the database


def load_csv(conn: Connection, csv_path: str, copy_sql: str) -> None:
    """Bulk-load a CSV into a table with the given COPY statement."""
    # I open the CSV in text read mode and stream it straight into COPY
    with open(csv_path, mode="r", encoding="utf-8", newline="") as file:
        with conn.cursor() as cur:
            cur.copy_expert(copy_sql, file)

    conn.commit()


def count_rows(conn: Connection, table_name: str) -> int:
    """Return how many rows landed in the given table."""
    with conn.cursor() as cur:
        # the table name comes from my own constants, never from outside input
        query = f"SELECT COUNT(*) FROM {table_name};"
        cur.execute(query)
        result = cur.fetchone()
        row_count = result[0] if result else 0
        return row_count


def check_totals(conn: Connection) -> None:
    """Assert each date's amount sum still matches my konspekt totals."""
    with conn.cursor() as cur:
        query = """
        SELECT report_date, sum(amount) FROM roa_roe.assets GROUP BY report_date;
        """
        cur.execute(query)
        rows = cur.fetchall()

    # I compare every date's sum against my konspekt total
    for i in range(len(rows)):
        date = rows[i][0]
        actual = float(rows[i][1])
        expected = TOTALS_BY_DATE[date]
        assert abs(actual - expected) <= INVARIANT_TOLERANCE, (
            f"invariant failed for {date}: {actual} vs {expected}"
        )
        print("  ", date, ":", actual)


def main() -> None:
    """Create the tables, load both CSVs and verify the result."""
    conn = connect()
    if conn is None:
        # I stop here, there is nothing to load into
        return

    create_table(conn, SCHEMA_SQL_PATH)
    load_csv(conn, CLEAN_CSV_PATH, COPY_ASSETS_SQL)
    load_csv(conn, EQUITY_CSV_PATH, COPY_EQUITY_SQL)

    print("assets rows :", count_rows(conn, "roa_roe.assets"))         # I expect EXPECTED_ROW_COUNT
    print("equity_income rows :", count_rows(conn, "roa_roe.equity_income"))  # I expect EXPECTED_EQUITY_ROWS
    check_totals(conn)
    conn.close()


if __name__ == "__main__":
    main()