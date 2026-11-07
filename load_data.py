import duckdb, glob

con = duckdb.connect("warehouse.duckdb")
con.execute("""CREATE TABLE IF NOT EXISTS target (
    id INTEGER PRIMARY KEY, name VARCHAR, amount DOUBLE, updated_at DATE)""")

for path in sorted(glob.glob("orders_*.csv")):
    con.execute("DROP TABLE IF EXISTS staging")
    con.execute(f"CREATE TABLE staging AS SELECT * FROM read_csv_auto('{path}')")
    n = con.execute("SELECT COUNT(*) FROM staging").fetchone()[0]
    if n == 0:
        print(path, "is empty, skipped")
        continue
    con.execute("""
        INSERT INTO target
        SELECT id, name, amount, updated_at FROM (
            SELECT *, ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated_at DESC) rn
            FROM staging)
        WHERE rn = 1
        ON CONFLICT (id) DO UPDATE SET
            name = excluded.name, amount = excluded.amount, updated_at = excluded.updated_at
    """)
    print(path, "loaded", n, "rows")

print("Rows in target:", con.execute("SELECT COUNT(*) FROM target").fetchone()[0])