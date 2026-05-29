# Power BI Dashboard Design

## Project
Broadband Customer 360 & Churn Lakehouse

## Dashboard Goal
The dashboard helps business users monitor broadband subscriber movement, revenue impact, churn risk, customer behavior, and data quality.

## Main Business Questions

1. How many broadband customers are active?
2. How many customers are new?
3. How many customers churned?
4. What is the net revenue impact?
5. Which provinces or network operations have high churn?
6. Which customers are high risk?
7. Can business users trust the data?

## Data Source

Version 1 uses Snowflake Gold and Monitoring tables.

Main tables:

| Table | Purpose |
|---|---|
| `GOLD_ACTIVE_NEW_CHURN_MONTHLY` | Executive subscriber KPIs |
| `GOLD_CUSTOMER_360_MONTHLY` | Customer behavior and monthly profile |
| `GOLD_CHURN_RISK_FEATURES` | Churn risk segmentation |
| `DQ_MONITORING_SUMMARY` | Data quality status |
| `DQ_QUARANTINE_SUMMARY` | Invalid record summary |
| `PIPELINE_RUN_CONTROL` | Pipeline run tracking |

## Dashboard Pages

| Page | Purpose |
|---|---|
| Page 1: Executive Summary | Subscriber and revenue overview |
| Page 2: Customer Behavior | Payment, usage, tickets, and on-top product behavior |
| Page 3: Churn Risk | LOW / MEDIUM / HIGH risk analysis |
| Page 4: Data Quality | DQ status and quarantine issues |
| Page 5: Platform Story | Snowflake and Databricks implementation summary |

## Filters

Common filters:

- Month
- Province
- Network Operation
- Segment
- Package Name
- Churn Risk Level
- Customer Status

## Design Principle

The dashboard should tell a story:

1. What happened?
2. Where did it happen?
3. Why might it have happened?
4. Which customers are at risk?
5. Can we trust the data?