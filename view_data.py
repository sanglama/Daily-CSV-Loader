import duckdb

con = duckdb.connect("warehouse.duckdb")
for row in con.execute("SELECT * FROM target ORDER BY id").fetchall():
    print(row)