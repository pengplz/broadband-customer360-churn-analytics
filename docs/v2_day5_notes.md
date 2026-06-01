# Version 2 Day 5 / Overall Day 25 Notes

## Goal

Rerun Silver and Gold from the automated Bronze layer and validate end-to-end pipeline outputs.

## Completed

- Reran Snowflake pipeline from automated Bronze to Silver, Gold, DQ, validation, and regression tests
- Reran Databricks pipeline from automated Bronze to Silver, Gold, DQ, validation, and regression tests
- Created Snowflake end-to-end refresh validation table
- Created Databricks end-to-end refresh validation table
- Validated Bronze row counts
- Validated Silver row counts
- Validated Gold row counts
- Validated Net Adds logic
- Validated Net Revenue Impact logic
- Validated DQ monitoring status
- Validated regression test status
- Updated reconciliation report
- Updated pipeline runbook

## New Objects

### Snowflake

- `MONITORING.END_TO_END_REFRESH_VALIDATION`

### Databricks

- `dev_broadband.monitoring.end_to_end_refresh_validation`

## Engineering Value

This proves that the new automated ingestion layer can safely feed the rest of the pipeline.

The project is now stronger because automated Bronze ingestion is connected to:

- Silver cleaning
- Gold business tables
- DQ monitoring
- Quarantine records
- Validation summary
- Regression tests
- Power BI-ready outputs

## Business Value

Business users can trust that the dashboard data is still valid after the ingestion process changed from manual loading to automated loading.

## Interview Note

I upgraded ingestion automation, then reran and validated the downstream pipeline end-to-end. This shows that I did not only automate one step, but also proved that downstream business outputs remained correct.

## Next Step

Day 26 will convert Snowflake SQL steps into stored-procedure style so the pipeline can be called more easily from orchestration.