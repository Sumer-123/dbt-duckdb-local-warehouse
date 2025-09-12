import duckdb
import os

# Path to the database file within your project folder
db_path = 'dbt_project.db'

# Connect to the DuckDB database file
con = duckdb.connect(db_path)

# Create a schema for our raw data
con.execute("CREATE SCHEMA IF NOT EXISTS raw;")

# Load the CSV data into a table named 'raw_sales'
con.execute("CREATE OR REPLACE TABLE raw.raw_sales AS SELECT * FROM read_csv_auto('data/sales_data.csv');")

print(f"Successfully loaded sales_data.csv into the 'raw.raw_sales' table in '{db_path}'.")
con.close()