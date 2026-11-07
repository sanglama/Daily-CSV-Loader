# make_data.py
make_data.py
Generates 5 fake daily order files (orders_YYYY-MM-DD.csv).
Each file contains a few duplicate rows, and day 4 is empty on purpose.
All data is fake.

# load_data.py
load_data.py
Loads the daily CSV files into a DuckDB database (warehouse.duckdb).

Steps for each file:
1. Load the file into a staging table.
2. Skip the file if it is empty.
3. Keep only the latest row per id (ROW_NUMBER window function).
4. Upsert the result into the target table (insert new ids, update existing).

Safe to rerun: the target table never gets duplicate ids.

# view_data.py
view_data.py
Prints all rows of the target table so you can check the result.
