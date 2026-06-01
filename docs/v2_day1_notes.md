# Version 2 Day 1 / Overall Day 21 Notes

## Goal

Automate Snowflake CSV ingestion using file format, internal stage, Bronze stage tables, Bronze raw tables, and ingestion audit logging.

## Completed

- Created CSV file format
- Created internal stage
- Created Bronze stage schema
- Created Bronze stage tables
- Loaded staged CSV files using COPY INTO
- Inserted staged data into Bronze raw tables with metadata
- Added batch ID
- Created ingestion audit table
- Validated row counts

## New Snowflake Objects

- `MONITORING.FF_CSV_BROADBAND`
- `MONITORING.STG_BROADBAND_SOURCE`
- `BRONZE_STAGE.CUSTOMERS_STAGE`
- `BRONZE_STAGE.SUBSCRIPTIONS_STAGE`
- `BRONZE_STAGE.PAYMENTS_STAGE`
- `BRONZE_STAGE.NETWORK_USAGE_STAGE`
- `BRONZE_STAGE.TROUBLE_TICKETS_STAGE`
- `BRONZE_STAGE.PRODUCT_ONTOP_STAGE`
- `BRONZE_STAGE.CALENDAR_MONTHS_STAGE`
- `MONITORING.INGESTION_AUDIT`

## Engineering Value

This improves the project because ingestion is now repeatable and auditable.

Each load captures:

- Batch ID
- Source file name
- Target table
- Row count
- Load status
- Load timestamp

## Next Step

Day 22 will automate Databricks Bronze ingestion.