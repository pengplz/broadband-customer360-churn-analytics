# Version 2 Runbook

## Project

Broadband Customer 360 & Churn Analytics

## Version 2 Goal

Version 2 upgrades the original portfolio project from manual execution into a more production-style pipeline.

Main improvements:

- Automated Snowflake ingestion
- Automated Databricks ingestion
- File validation
- Ingestion audit
- Batch run control
- Reusable ingestion configuration
- Snowflake stored procedures
- Snowflake Task Graph
- Databricks notebook pipeline
- Databricks Workflow
- End-to-end validation

---

## Version 2 High-Level Flow

```text
Source CSV files
→ Automated Bronze ingestion
→ File validation
→ Ingestion audit
→ Silver cleaning
→ Gold business tables
→ DQ monitoring
→ Regression tests
→ Workflow validation