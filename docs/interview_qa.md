# Interview Q&A

## 1. What is this project about?

This project is a Broadband Customer 360 and Churn Analytics pipeline.

It simulates a telecom/broadband data platform that tracks monthly Active, New, and Churned customers, calculates revenue impact, builds Customer 360 analytics, identifies churn-risk customers, and monitors data quality.

I built it in both Snowflake and Databricks to compare a cloud data warehouse approach with a lakehouse approach.

---

## 2. Why did you build it in both Snowflake and Databricks?

I wanted to show that the same business logic can be implemented across different modern data platforms.

Snowflake represents a cloud data warehouse approach.  
Databricks represents a lakehouse approach.

By building both, I can demonstrate platform flexibility and also validate whether the business outputs match across both systems.

---

## 3. What are the main data layers?

The project follows Bronze, Silver, and Gold layers.

Bronze stores raw source data with metadata.

Silver cleans and standardizes the data.

Gold creates business-ready tables for reporting and analytics.

There is also a Monitoring layer for data quality, quarantine records, pipeline run control, validation, and regression tests.

---

## 4. What are the main Gold tables?

The main Gold tables are:

1. `gold_active_new_churn_monthly`
2. `gold_customer_360_monthly`
3. `gold_churn_risk_features`

The first table supports executive KPIs.  
The second table creates one row per customer/subscription/month.  
The third table creates churn-risk features and risk levels.

---

## 5. How did you define Active, New, and Churn?

A subscription is Active if it started on or before the end of the reporting month and has no end date or ended after the month end.

A subscription is New if its start date is in the reporting month.

A subscription is Churned if its end date is in the reporting month.

---

## 6. How did you calculate churn rate?

Churn rate is calculated as:

```text
churn_subs / active_subs