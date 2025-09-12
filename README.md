# Local Analytics Warehouse with dbt & DuckDB

This project demonstrates a modern, local analytics pipeline using dbt for transformations and DuckDB as a high-speed, in-process data warehouse.

The pipeline ingests raw CSV data, models it using SQL, runs data quality tests to ensure integrity, and automatically generates a full documentation site with a data lineage graph. This showcases a code-first, version-controlled approach to analytics engineering.

---

## Technology Stack

* **Transformation:** dbt-core
* **Data Warehouse:** DuckDB
* **Languages:** Python (for data loading) & SQL (for modeling)
* **Key Concepts:** ELT, Data Modeling, Data Quality Testing, Automated Documentation

---

## Project Structure

* **`data/`**: Contains the raw input CSV files.
* **`load_data.py`**: A Python script to load the raw data from CSV into a DuckDB table.
* **`dbt_project/`**: The main dbt project folder containing all models, tests, and configurations.
* **`dbt_project/models/`**: Contains the SQL transformation models.

---

## How to Run

1.  Create and activate a Python virtual environment.
2.  Install dependencies: `pip install dbt-duckdb duckdb`
3.  Load the raw data: `python load_data.py`
4.  Navigate into the dbt project folder: `cd dbt_project`
5.  Run the dbt models: `dbt run`
6.  Run the data quality tests: `dbt test`
7.  View the documentation: `dbt docs generate && dbt docs serve`