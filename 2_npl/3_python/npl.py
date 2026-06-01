import os
import psycopg2
from psycopg2.extensions import connection, cursor
from dotenv import load_dotenv

def connect_to_db() -> connection:
    """Open a connection using the .env settings and return it."""
    load_dotenv()

    conn = psycopg2.connect(
        host = os.getenv("PGHOST"),
        port = os.getenv("PGPORT"),
        dbname = os.getenv("PGDATABASE"),
        user = os.getenv("PGUSER"),
        password = os.getenv("PGPASSWORD")
    )

    print("Connected to the database")

    return conn

def load_clients(file_path: str, cur: cursor) -> None:
    """Read a client's CSV and insert every row into npl_ratio.clients table."""
    # Read clients.csv line by line, skipping the header.
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        next(file) # skip the header row

        for line in file:
            client_id, client_name, segment, industry = line.strip().split(",")
            cur.execute(
                "INSERT INTO npl_ratio.clients VALUES (%s, %s, %s, %s)",
                (int(client_id), client_name, segment, industry)
            )

def load_loans(file_path: str, cur: cursor) -> None:
    """Read a loans's CSV, fix the quarter format, and insert into npl_ratio.loans table."""

    # Read loans.csv the same way, converting the numeric fields.
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        next(file) # skip the header row

        for line in file:
            loan_id, client_id, report_quarter, currency, outstanding_amount, days_overdue, provisions_amount = line.strip().split(",")

            quarter, year = report_quarter.split(" ")
            report_quarter = year + "-" + quarter

            cur.execute(
                "INSERT INTO npl_ratio.loans VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (int(loan_id), int(client_id), report_quarter, currency, float(outstanding_amount), int(days_overdue), float(provisions_amount))
            )

def main() -> None:
    """Run the whole load: connect, insert clients, insert loans, commit."""
    conn = connect_to_db()
    cur = conn.cursor()

    load_clients("../data/clients.csv", cur)
    load_loans("../data/loans.csv", cur)

    # Save the changes and close the connection.
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()