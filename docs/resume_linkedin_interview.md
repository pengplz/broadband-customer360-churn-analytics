# Resume, LinkedIn, and Interview Material

## Project Name

Broadband Customer 360 & Churn Analytics — Snowflake + Databricks

## Resume Version 1: Short Version

- Built an end-to-end Broadband Customer 360 and Churn Analytics pipeline using Snowflake, Databricks, SQL, Python, and Power BI.
- Designed Bronze, Silver, and Gold data layers to support monthly Active, New, Churn, revenue impact, Customer 360, and churn-risk reporting.
- Implemented production-style data quality monitoring, quarantine handling, pipeline run-control logging, validation, and regression testing.
- Developed Power BI dashboard pages for Executive Summary, Customer Behavior, Churn Risk, Data Quality, and Platform Story.

## Resume Version 2: Strong Data Engineer Version

- Designed and built a dual-platform Broadband Customer 360 analytics pipeline across Snowflake and Databricks using Bronze/Silver/Gold architecture.
- Generated realistic broadband source data including customers, subscriptions, payments, network usage, trouble tickets, product on-top, and calendar data.
- Built Silver clean tables with standardized dates, numeric fields, required-key validation, and business-ready structures.
- Developed Gold tables for monthly Active/New/Churn reporting, Customer 360, churn-risk features, and revenue impact analysis.
- Created a rule-based churn-risk feature table using rolling 3-month late payment count, trouble ticket count, usage drop, speed drop, service month, and on-top product adoption.
- Added data quality monitoring with row count checks, duplicate key checks, null key checks, freshness checks, and PASS/WARNING/FAIL status.
- Implemented quarantine handling to capture invalid Bronze records with rule name, severity, error message, business key, and original record payload.
- Created reconciliation and regression test frameworks to compare Snowflake and Databricks outputs and validate business logic.
- Built a Power BI dashboard showing subscriber KPIs, churn behavior, risk segmentation, data quality status, and pipeline monitoring.

## Resume Version 3: Senior-Style Version

- Architected and implemented a production-style Broadband Customer 360 and Churn Analytics platform across Snowflake and Databricks, following Bronze/Silver/Gold data modeling patterns.
- Built business-ready Gold tables for subscriber lifecycle reporting, revenue impact, customer behavior analytics, and churn-risk segmentation.
- Designed monitoring and reliability layers including DQ summary tables, quarantine records, pipeline run-control logs, validation summaries, and regression test outputs.
- Reconciled warehouse and lakehouse implementations to ensure consistent Active/New/Churn, revenue impact, Customer 360, and churn-risk results across platforms.
- Delivered Power BI executive dashboard with subscriber trends, churn risk analysis, customer behavior insights, and data quality visibility.

## LinkedIn Project Description

I recently built a portfolio project called **Broadband Customer 360 & Churn Analytics**.

The project simulates a real telecom/broadband data engineering use case: tracking monthly Active, New, and Churned customers, calculating revenue impact, creating Customer 360 analytics, identifying churn-risk customers, and monitoring data quality.

I implemented the same pipeline in both **Snowflake** and **Databricks** to compare a cloud data warehouse approach with a lakehouse approach.

Main components:

- Fake broadband source data generation using Python
- Bronze, Silver, and Gold data layers
- Snowflake SQL implementation
- Databricks SQL/lakehouse implementation
- Monthly Active/New/Churn Gold table
- Customer 360 monthly Gold table
- Churn-risk feature table
- Data quality monitoring
- Quarantine handling for invalid records
- Pipeline run-control logging
- Snowflake vs Databricks reconciliation
- Regression testing
- Power BI dashboard

The goal was not only to build tables, but to design the project like a production-style data platform with reliability, monitoring, documentation, and business value.

## LinkedIn Featured Project Text

**Broadband Customer 360 & Churn Analytics**

Built an end-to-end analytics pipeline in Snowflake and Databricks to simulate a real broadband data platform.

The project includes Bronze/Silver/Gold layers, Active/New/Churn reporting, Customer 360 modeling, churn-risk features, DQ monitoring, quarantine records, regression tests, reconciliation, and a Power BI dashboard.

This project demonstrates data engineering ownership from source data to business dashboard.

## Portfolio Summary

This project demonstrates:

- Data engineering architecture
- SQL transformation logic
- Snowflake and Databricks implementation
- Data quality monitoring
- Quarantine handling
- Churn-risk feature engineering
- Pipeline orchestration design
- Reconciliation and regression testing
- Power BI dashboarding
- Documentation and storytelling