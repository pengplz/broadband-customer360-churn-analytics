# Project Pitch

## 30-Second Pitch

I built a Broadband Customer 360 and Churn Analytics project using both Snowflake and Databricks.

The project tracks monthly Active, New, and Churned customers, calculates revenue impact, builds a Customer 360 table, creates churn-risk features, and visualizes the results in Power BI.

I also added data quality monitoring, quarantine handling, validation, regression testing, and pipeline run-control logging to make it closer to a production-style data engineering project.

## 2-Minute Pitch

This project simulates a real broadband data platform.

The business problem is that broadband companies need to understand how many customers are active, how many are new, how many churned, what revenue is impacted, and which customers are at high risk of churn.

I generated realistic dummy broadband data such as customers, subscriptions, payments, network usage, trouble tickets, on-top products, and calendar months.

Then I built the same pipeline in both Snowflake and Databricks.

The architecture follows Bronze, Silver, and Gold layers.

The Bronze layer keeps raw data.  
The Silver layer cleans and standardizes the data.  
The Gold layer creates business-ready tables.

The main Gold tables are:

1. `gold_active_new_churn_monthly`
2. `gold_customer_360_monthly`
3. `gold_churn_risk_features`

I also added production-style reliability features such as data quality monitoring, quarantine tables, pipeline run-control logging, Snowflake vs Databricks reconciliation, and regression tests.

Finally, I built a Power BI dashboard with pages for Executive Summary, Customer Behavior, Churn Risk, Data Quality, and Platform Story.

The value of this project is that it demonstrates end-to-end data engineering ownership, not just writing SQL queries.

## 5-Minute Demo Flow

### 1. Start with business problem

The dashboard answers:
- Active customers
- New customers
- Churned customers
- Revenue impact
- High-risk customers
- Data quality status

### 2. Show architecture

Explain:
- Source CSV
- Bronze
- Silver
- Gold
- Monitoring
- Dashboard

### 3. Show Gold tables

Explain:
- Active/New/Churn
- Customer 360
- Churn Risk Features

### 4. Show monitoring

Explain:
- DQ Monitoring
- Quarantine Records
- Pipeline Run Control
- Regression Tests

### 5. Show Power BI

Walk through:
- Executive Summary
- Customer Behavior
- Churn Risk
- Data Quality
- Platform Story

### 6. Close with value

This project shows that I can design, build, validate, monitor, and explain an end-to-end data platform.