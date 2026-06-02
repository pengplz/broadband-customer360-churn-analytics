# Version 2 Day 7 / Overall Day 27 Notes

## Goal

Create a Snowflake Task graph to orchestrate stored procedures.

## Completed

- Created validation procedure for task graph
- Created scheduled root task
- Created child task for Silver refresh
- Created child task for Gold Active/New/Churn refresh
- Created child task for pipeline validation
- Viewed task graph dependencies
- Tested task graph manually
- Checked task history
- Checked procedure execution log
- Checked validation result table

## New Objects

- `MONITORING.SP_VALIDATE_SNOWFLAKE_PIPELINE_V2()`
- `MONITORING.TASK_V2_00_PIPELINE_START`
- `MONITORING.TASK_V2_01_REFRESH_SILVER`
- `MONITORING.TASK_V2_02_REFRESH_GOLD_ACTIVE_NEW_CHURN`
- `MONITORING.TASK_V2_03_VALIDATE_PIPELINE`
- `MONITORING.TASK_GRAPH_VALIDATION_RESULTS`

## Current Task Graph

```text
TASK_V2_00_PIPELINE_START
→ TASK_V2_01_REFRESH_SILVER
→ TASK_V2_02_REFRESH_GOLD_ACTIVE_NEW_CHURN
→ TASK_V2_03_VALIDATE_PIPELINE