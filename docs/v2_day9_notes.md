# Version 2 Day 9 / Overall Day 29 Notes

## Goal

Create a Databricks Workflow with notebook task dependencies.

## Completed

- Created Databricks Workflow manually in the Jobs UI
- Added Bronze ingestion task
- Added Silver cleaning task
- Added Gold Active/New/Churn task
- Added Gold Customer 360 task
- Added Gold Churn Risk Features task
- Added DQ Monitoring task
- Added Regression Tests task
- Configured task dependencies
- Added notebook parameters
- Ran workflow manually
- Created workflow validation table
- Updated Databricks job YAML
- Created Databricks Workflow runbook

## Workflow Name

`broadband_customer360_churn_v2`

## Workflow Task Order

```text
bronze_ingestion
→ silver_cleaning
→ gold_active_new_churn
→ gold_customer_360
→ gold_churn_risk_features
→ dq_monitoring
→ regression_tests