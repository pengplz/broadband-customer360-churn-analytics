# Databricks Workflow Runbook

## Project

Broadband Customer 360 & Churn Analytics

## Workflow Name

`broadband_customer360_churn_v2`

## Purpose

This workflow runs the Databricks Version 2 pipeline from Bronze ingestion through Silver, Gold, DQ monitoring, and regression tests.

## Task Order

```text
bronze_ingestion
→ silver_cleaning
→ gold_active_new_churn
→ gold_customer_360
→ gold_churn_risk_features
→ dq_monitoring
→ regression_tests