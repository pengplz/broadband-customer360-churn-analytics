# Day 3 Notes

## Goal
Build the first Gold business table for monthly Active, New, Churn, churn rate, net adds, and revenue impact.

## Completed
- Created `gold_active_new_churn_monthly` in Snowflake
- Created `gold_active_new_churn_monthly` in Databricks
- Used Silver customer, subscription, and calendar tables
- Calculated active_flag, new_flag, and churn_flag
- Aggregated results by month, network operation, and province
- Added revenue impact metrics
- Ran validation checks
- Added table comments

## Business Logic

### Active
A subscription is active if:
- start_date is on or before the month end
- end_date is null or after the month end

### New
A subscription is new if:
- start_date is in the reporting month

### Churn
A subscription is churned if:
- end_date is in the reporting month

## Metrics
- active_subs
- new_subs
- churn_subs
- net_adds
- churn_rate
- new_revenue
- churn_revenue
- net_revenue_impact

## Next Step
Day 4 will build `gold_customer_360_monthly`, one row per customer per month.