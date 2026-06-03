# Version 3 Day 5 / Overall Day 35 Notes

## Goal

Understand streaming deduplication and design the deduplication strategy.

## Completed

- Created deduplication rules table
- Defined business keys for each source
- Defined deduplication strategy
- Analyzed duplicate records in unified raw payload table
- Compared total rows vs distinct business keys
- Identified exact payload duplicates
- Previewed latest-record ranking logic
- Created streaming deduplication design document

## New Table

- `dev_broadband.monitoring.deduplication_rules`

## New Notebook

- `notebooks/12_deduplication_analysis.py`

## New SQL

- `databricks_sql/v3_04_deduplication_analysis.sql`

## Deduplication Strategy

The first implementation will use:

```text
LATEST_BY_BUSINESS_KEY