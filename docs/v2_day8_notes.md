# Version 2 Day 8 / Overall Day 28 Notes

## Goal

Convert Databricks SQL scripts into notebooks so they can be orchestrated by Databricks Workflows.

## Completed

- Created Silver cleaning notebook
- Created Gold Active/New/Churn notebook
- Created Gold Customer 360 notebook
- Created Gold Churn Risk Features notebook
- Created DQ Monitoring wrapper notebook
- Created Regression Tests wrapper notebook
- Added notebook widgets for catalog and batch ID
- Manually ran notebooks in pipeline order
- Validated output table row counts
- Updated Databricks job YAML draft

## New Notebooks

- `notebooks/02_silver_cleaning.py`
- `notebooks/03_gold_active_new_churn.py`
- `notebooks/04_gold_customer_360.py`
- `notebooks/05_gold_churn_risk_features.py`
- `notebooks/06_dq_monitoring.py`
- `notebooks/07_regression_tests.py`

## Engineering Value

The Databricks pipeline is now modularized into notebook tasks.

This prepares the project for Databricks Workflow orchestration on Day 29.

## Current Notebook Run Order

```text
01_bronze_ingestion
→ 02_silver_cleaning
→ 03_gold_active_new_churn
→ 04_gold_customer_360
→ 05_gold_churn_risk_features
→ 06_dq_monitoring
→ 07_regression_tests