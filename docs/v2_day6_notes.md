# Version 2 Day 6 / Overall Day 26 Notes

## Goal

Convert Snowflake SQL pipeline steps into stored-procedure style.

## Completed

- Created procedure execution log table
- Created `SP_REFRESH_SILVER`
- Created `SP_REFRESH_GOLD_ACTIVE_NEW_CHURN`
- Created wrapper for `SP_REFRESH_GOLD_CUSTOMER_360`
- Created wrapper for `SP_REFRESH_GOLD_CHURN_RISK_FEATURES`
- Created wrapper for `SP_REFRESH_DQ_MONITORING`
- Created main pipeline wrapper `SP_RUN_SNOWFLAKE_PIPELINE_V2`
- Added procedure comments
- Validated procedure execution logs

## New Objects

- `MONITORING.PROCEDURE_EXECUTION_LOG`
- `MONITORING.SP_REFRESH_SILVER()`
- `MONITORING.SP_REFRESH_GOLD_ACTIVE_NEW_CHURN()`
- `MONITORING.SP_REFRESH_GOLD_CUSTOMER_360()`
- `MONITORING.SP_REFRESH_GOLD_CHURN_RISK_FEATURES()`
- `MONITORING.SP_REFRESH_DQ_MONITORING()`
- `MONITORING.SP_RUN_SNOWFLAKE_PIPELINE_V2()`

## Engineering Value

Stored procedures make the Snowflake pipeline easier to orchestrate.

Instead of manually running many SQL files, the pipeline can now be called step by step with `CALL` statements.

## Important Note

Only `SP_REFRESH_SILVER` and `SP_REFRESH_GOLD_ACTIVE_NEW_CHURN` contain full transformation logic today.

The Customer 360, Churn Risk, and DQ Monitoring procedures are wrappers. Their full SQL logic will be added in a future iteration.

## Interview Note

I converted Snowflake SQL scripts into callable stored-procedure-style pipeline steps and added procedure execution logging. This makes the pipeline easier to orchestrate, monitor, and extend.

## Next Step

Day 27 will create a Snowflake Task graph that calls these stored procedures in sequence.