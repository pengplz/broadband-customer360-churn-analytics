# Version 2 Day 2 / Overall Day 22 Notes

## Goal

Automate Databricks Bronze ingestion using a notebook-based ingestion process.

## Completed

- Created Databricks Bronze ingestion notebook
- Defined source file configuration
- Read CSV files as strings
- Added metadata columns
- Wrote data into Bronze Delta tables
- Created Databricks ingestion audit table
- Logged row counts, source file names, target tables, status, and timestamp
- Validated Bronze row counts

## New / Updated Files

- `notebooks/01_bronze_ingestion.py`
- `databricks_sql/v2_02_automated_databricks_ingestion.sql`
- `docs/v2_day2_notes.md`

## Bronze Metadata Columns

Each Bronze table now includes:

- `input_file_name`
- `ingestion_timestamp`
- `source_system`
- `batch_id`

## Engineering Value

This removes manual Databricks table loading and makes ingestion repeatable.

The pipeline now has:

- Config-driven file loading
- Batch ID tracking
- Audit logging
- Bronze metadata
- Repeatable notebook execution

## Databricks Ingestion Options

For this project, the notebook-based ingestion method is used first because it is simple and flexible.

Future improvements can use:

- `COPY INTO` for SQL-based incremental file loading
- Auto Loader for streaming or file-arrival ingestion

## Next Step

Day 23 will add stronger ingestion audit and file validation across both Snowflake and Databricks.