# CSV Data Loader (DuckDB)

A small data pipeline that loads daily CSV files into a database and keeps the data clean.

## What it does
- Generates fake daily order files (`make_data.py`), including duplicate rows and one empty file
- Loads each file into a staging table, keeps only the latest row per `id`, and updates the target table (`load_data.py`)
- Skips empty files
- Can be rerun without creating duplicates in the target table

## How to run
1. `python make_data.py` creates the CSV files
2. `python load_data.py` loads them into `warehouse.duckdb`
3. `python view_data.py` shows the result

## Tech
Python, DuckDB, SQL (window functions, upsert)

## Data
All data is fake.

## Next steps
Row-count checks between staging and target, pytest tests, failure alerts
