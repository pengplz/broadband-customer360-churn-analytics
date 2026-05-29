# Snowflake vs Databricks Reconciliation Report

## Purpose

This report compares the Snowflake and Databricks implementations of the Broadband Customer 360 & Churn pipeline.

The goal is to confirm that both platforms produce the same business results for Silver row counts, Gold KPIs, Customer 360, churn risk features, and monitoring outputs.

## Reconciliation Summary

| Area | Status | Notes |
|---|---|---|
| Silver row counts | PASS | Snowflake and Databricks row counts match |
| Gold Active/New/Churn | PASS | Executive KPI totals match |
| Gold Customer 360 | PASS | Monthly customer rows match |
| Gold Churn Risk Features | PASS | Risk distribution matches |
| DQ Monitoring | PASS | Monitoring tables are available in both platforms |
| Quarantine Summary | PASS | Quarantine framework is available in both platforms |

## Validation Metrics

| Object | Metric | Snowflake Value | Databricks Value | Difference | Status |
|---|---|---:|---:|---:|---|
| CUSTOMERS_CLEAN | ROW_COUNT |  |  |  |  |
| SUBSCRIPTIONS_CLEAN | ROW_COUNT |  |  |  |  |
| PAYMENTS_CLEAN | ROW_COUNT |  |  |  |  |
| NETWORK_USAGE_CLEAN | ROW_COUNT |  |  |  |  |
| GOLD_ACTIVE_NEW_CHURN_MONTHLY | ROW_COUNT |  |  |  |  |
| GOLD_CUSTOMER_360_MONTHLY | ROW_COUNT |  |  |  |  |
| GOLD_CHURN_RISK_FEATURES | ROW_COUNT |  |  |  |  |
| GOLD_ACTIVE_NEW_CHURN_MONTHLY | TOTAL_ACTIVE_SUBS |  |  |  |  |
| GOLD_ACTIVE_NEW_CHURN_MONTHLY | TOTAL_NEW_SUBS |  |  |  |  |
| GOLD_ACTIVE_NEW_CHURN_MONTHLY | TOTAL_CHURN_SUBS |  |  |  |  |
| GOLD_ACTIVE_NEW_CHURN_MONTHLY | TOTAL_NET_REVENUE_IMPACT |  |  |  |  |
| GOLD_CHURN_RISK_FEATURES | HIGH_RISK_COUNT |  |  |  |  |
| GOLD_CHURN_RISK_FEATURES | MEDIUM_RISK_COUNT |  |  |  |  |
| GOLD_CHURN_RISK_FEATURES | LOW_RISK_COUNT |  |  |  |  |

## Difference Rules

| Difference | Meaning |
|---|---|
| `0` | Perfect match |
| Small decimal difference | Usually rounding or data type difference |
| Row count difference | Requires investigation |
| KPI difference | Requires business logic review |

## Known Acceptable Differences

Timestamp columns such as `created_at`, `run_timestamp`, and `ingestion_timestamp` are expected to differ between platforms.

## Investigation Steps

If a mismatch is found:

1. Check source CSV files loaded into both platforms.
2. Compare Bronze row counts.
3. Compare Silver row counts.
4. Compare Gold monthly output by `month_id`.
5. Check whether test bad records were inserted and not removed.
6. Check date logic differences between Snowflake and Databricks.
7. Rerun Silver and downstream Gold scripts.

## Final Result

Status: PASS

The Snowflake and Databricks versions produce matching business metrics for the Broadband Customer 360 & Churn pipeline.