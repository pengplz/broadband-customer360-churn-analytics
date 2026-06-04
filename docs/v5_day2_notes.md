# Version 5 Day 2 / Overall Day 47 Notes

## Goal

Generate CDC test changes after Change Data Feed has been enabled.

## Completed

- Confirmed CDF is enabled on SCD2 dimension tables
- Captured pre-change Delta versions
- Created customer CDC test change file
- Created subscription CDC test change file
- Registered CDC test changes
- Re-ran unified raw payload ingestion
- Rebuilt deduplicated Bronze payload
- Re-ran SCD2 merge/update logic
- Verified SCD2 history still works after CDF enablement
- Previewed CDF records with `table_changes`
- Created CDC test validation SQL

## New Notebook

- `notebooks/24_generate_cdc_test_changes.py`

## New SQL

- `databricks_sql/v5_02_generate_cdc_test_changes.sql`

## New Tables

- `dev_broadband.monitoring.cdc_test_change_registry`
- `dev_broadband.monitoring.cdc_test_change_validation`

## Test Changes

### Customer

Changed:

```text
province
segment