# Day 11 Notes

## Goal
Build the remaining Power BI dashboard pages.

## Completed
- Built Customer Behavior page
- Built Churn Risk page
- Built Data Quality page
- Added KPI cards
- Added slicers
- Added behavior analysis visuals
- Added churn-risk validation visuals
- Added DQ monitoring visuals
- Saved Power BI dashboard file

## Dashboard Pages Built

### Page 1: Executive Summary
Built on Day 10.

### Page 2: Customer Behavior
Uses `GOLD_CUSTOMER_360_MONTHLY`.

Main analysis:
- Payment behavior vs churn
- Usage trend
- Speed trend
- Trouble tickets vs churn
- On-top product adoption

### Page 3: Churn Risk
Uses `GOLD_CHURN_RISK_FEATURES`.

Main analysis:
- Risk level distribution
- High-risk customers by province
- Risk by segment
- Actual churn rate by risk level
- Top high-risk customer table

### Page 4: Data Quality
Uses:
- `DQ_MONITORING_SUMMARY`
- `DQ_QUARANTINE_SUMMARY`
- `PIPELINE_RUN_CONTROL`

Main analysis:
- DQ PASS / WARNING / FAIL
- Row count checks
- Duplicate checks
- Null key checks
- Freshness status
- Quarantine issue summary
- Pipeline run status

## Business Value
The dashboard now gives business users both subscriber insights and data trust visibility.

## Interview Note
This dashboard is not only KPI reporting. It also includes data quality monitoring, quarantine visibility, and pipeline status, which makes it closer to a production analytics solution.

## Next Step
Day 12 will polish the Power BI dashboard layout, add a platform story page, and prepare screenshots for GitHub.