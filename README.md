# Broadband Customer 360 & Churn Lakehouse

## Project Overview

This project is an end-to-end broadband analytics pipeline built in both Snowflake and Databricks.

The goal is to answer:

- How many broadband customers are Active, New, and Churned?
- What revenue is impacted by new and churned customers?
- Which customer segments are high-risk?
- Can business users trust the reporting data?

## Why This Project Matters

This project simulates a real production-style telecom data platform. It combines subscriber lifecycle reporting, Customer 360, churn-risk features, data quality monitoring, quarantine handling, and pipeline orchestration.

## Platforms

| Platform | Purpose |
|---|---|
| Snowflake | Cloud data warehouse implementation |
| Databricks | Lakehouse implementation |

## Tech Stack

- Snowflake
- Databricks
- SQL
- Python for fake data generation
- Medallion Architecture
- Data Quality Monitoring
- Quarantine Tables
- GitHub
- Power BI planned for dashboard

## Architecture

```mermaid
flowchart TD

    A[Fake Broadband CSV Data] --> B[Bronze Layer]
    B --> C[Silver Layer]
    C --> D[Gold Layer]
    D --> E[Power BI Dashboard]

    B --> F[Quarantine Records]
    C --> G[DQ Monitoring]
    D --> G

    H[Orchestration] --> B
    H --> C
    H --> D
    H --> F
    H --> G


Data Sources
Source	Description
customers.csv	Customer demographics
subscriptions.csv	Subscription lifecycle
payments.csv	Billing and payment behavior
network_usage.csv	Usage and speed data
trouble_tickets.csv	Customer issue data
product_ontop.csv	Add-on product data
calendar_months.csv	Monthly calendar reference
Data Layers
Bronze

Raw source tables with metadata.

Silver

Cleaned and standardized tables.

Gold

Business-ready reporting and analytics tables.

Gold Tables
Table	Purpose
gold_active_new_churn_monthly	Monthly Active, New, Churn, churn rate, and revenue impact
gold_customer_360_monthly	One row per customer/subscription/month
gold_churn_risk_features	Churn-risk feature table with LOW/MEDIUM/HIGH risk level
Monitoring Tables
Table	Purpose
dq_monitoring_summary	Data quality status by table
dq_quarantine_records	Invalid records with rule metadata
dq_quarantine_summary	Summary of quarantine issues
pipeline_run_control	Pipeline execution tracking
Business Metrics
Active Subscribers
New Subscribers
Churned Subscribers
Net Adds
Churn Rate
New Revenue
Churn Revenue
Net Revenue Impact
High-Risk Customers
Project Structure
broadband-customer360-dual-platform/
│
├── data_generator/
├── data/
├── snowflake_sql/
├── databricks_sql/
├── resources/
├── docs/
└── powerbi/
Run Order
Generate fake source data
Create/load Bronze tables
Build Silver clean tables
Build Gold Active/New/Churn table
Build Gold Customer 360 table
Build Gold Churn Risk Features table
Build DQ Monitoring
Build Quarantine Records
Review pipeline run-control logs
Documentation
Document	Description
docs/architecture.md	Architecture explanation
docs/data_dictionary.md	Table and column definitions
docs/pipeline_runbook.md	Run order and support guide
docs/snowflake_vs_databricks.md	Platform comparison
docs/resume_story.md	Resume bullets and interview explanation
Portfolio Value

This project demonstrates:

End-to-end data pipeline design
Dual-platform implementation
Medallion architecture
Business KPI development
Customer 360 modeling
Churn-risk feature engineering
Data quality monitoring
Quarantine handling
Orchestration design
Documentation and runbook ownership


# Broadband Customer 360 & Churn Analytics — Snowflake + Databricks

## Project Overview

This project is an end-to-end broadband analytics platform built in both **Snowflake** and **Databricks**.

The project simulates a real telecom data engineering use case: tracking broadband subscribers, identifying churn, measuring revenue impact, building Customer 360 analytics, monitoring data quality, and presenting insights through Power BI.

## Business Questions

This project answers:

- How many broadband customers are active each month?
- How many customers are new?
- How many customers churned?
- What is the revenue impact of new and churned customers?
- Which provinces, segments, or network operations have higher churn?
- Which customers are at high risk of churn?
- Can business users trust the reporting data?

## Why This Project Is Valuable

This is not only a SQL or dashboard project.

It demonstrates a production-style data engineering workflow:

- Source data generation
- Bronze, Silver, and Gold data layers
- Snowflake implementation
- Databricks implementation
- Customer 360 modeling
- Churn risk feature engineering
- Data quality monitoring
- Quarantine handling
- Pipeline orchestration design
- Regression testing
- Power BI dashboarding
- Documentation and runbook ownership


## Project Status

| Area | Status |
|---|---|
| Fake data generator | Completed |
| Snowflake Bronze/Silver/Gold | Completed |
| Databricks Bronze/Silver/Gold | Completed |
| Active/New/Churn table | Completed |
| Customer 360 table | Completed |
| Churn Risk Features | Completed |
| DQ Monitoring | Completed |
| Quarantine Handling | Completed |
| Orchestration Design | Completed |
| Reconciliation | Completed |
| Regression Tests | Completed |
| Power BI Dashboard | Completed |
| Documentation | In Progress |

## End-to-End Run Order

| Step | Script / Area | Description |
|---:|---|---|
| 1 | `data_generator/generate_fake_broadband_data.py` | Generate fake broadband CSV data |
| 2 | `01_bronze_tables.sql` | Create/load raw Bronze tables |
| 3 | `02_silver_tables.sql` | Clean and standardize data |
| 4 | `03_gold_active_new_churn.sql` | Build Active/New/Churn monthly Gold table |
| 5 | `04_gold_customer_360.sql` | Build Customer 360 monthly Gold table |
| 6 | `05_gold_churn_risk_features.sql` | Build churn risk feature table |
| 7 | `06_dq_monitoring.sql` | Build DQ monitoring summary |
| 8 | `07_quarantine_records.sql` | Capture invalid records |
| 9 | `08_pipeline_orchestration.sql` | Track pipeline run control |
| 10 | `09_validation_reconciliation.sql` | Reconcile Snowflake and Databricks outputs |
| 11 | `10_regression_tests.sql` | Run regression tests |
| 12 | Power BI | Build executive and monitoring dashboard |

## Resume-Ready Summary

This project can be summarized on a resume as:

> Built an end-to-end Broadband Customer 360 and Churn Analytics pipeline across Snowflake and Databricks using Bronze/Silver/Gold architecture, SQL transformations, data quality monitoring, quarantine handling, reconciliation, regression testing, and Power BI dashboarding.

Key outcomes:

- Created monthly Active/New/Churn and revenue impact reporting
- Built Customer 360 monthly Gold table
- Created churn-risk feature table
- Added DQ monitoring and quarantine records
- Reconciled Snowflake and Databricks outputs
- Built executive-ready Power BI dashboard

## Known Limitations

This project is designed as a portfolio simulation.

Current limitations:

- The source data is generated dummy data, not real production data.
- Some ingestion steps are manual for simplicity.
- Snowflake task automation is represented as a design/skeleton.
- Databricks workflow YAML may need path adjustment before deployment.
- Churn risk scoring is rule-based, not machine learning.
- Power BI is connected first to Snowflake; Databricks BI connection can be added as a future enhancement.

## Future Improvements

Planned improvements:

- Automate CSV ingestion fully
- Add Snowflake Tasks and stored procedures
- Deploy Databricks Workflow using Asset Bundles
- Add CI/CD validation
- Add Great Expectations or dbt tests
- Add ML-based churn prediction
- Add Power BI drill-through customer page
- Add alerting for DQ failures


## Project Completion Status

This project was completed as a 20-day portfolio build.

Final deliverables include:

- Dual-platform Snowflake and Databricks implementation
- Bronze/Silver/Gold data architecture
- Active/New/Churn monthly reporting
- Customer 360 monthly model
- Churn risk feature table
- Data quality monitoring
- Quarantine handling
- Pipeline run-control logging
- Snowflake vs Databricks reconciliation
- Regression tests
- Power BI dashboard
- Full documentation and demo material

## Final Learning Outcome

This project strengthened practical skills in:

- Data engineering architecture
- SQL transformation design
- Cloud data warehouse implementation
- Lakehouse implementation
- Data quality and monitoring
- Analytics modeling
- Dashboard storytelling
- Documentation and interview communication## Project Completion Status

This project was completed as a 20-day portfolio build.

Final deliverables include:

- Dual-platform Snowflake and Databricks implementation
- Bronze/Silver/Gold data architecture
- Active/New/Churn monthly reporting
- Customer 360 monthly model
- Churn risk feature table
- Data quality monitoring
- Quarantine handling
- Pipeline run-control logging
- Snowflake vs Databricks reconciliation
- Regression tests
- Power BI dashboard
- Full documentation and demo material

## Final Learning Outcome

This project strengthened practical skills in:

- Data engineering architecture
- SQL transformation design
- Cloud data warehouse implementation
- Lakehouse implementation
- Data quality and monitoring
- Analytics modeling
- Dashboard storytelling
- Documentation and interview communication

## Version 2 Progress

| Day | Improvement | Status |
|---:|---|---|
| 21 | Automated Snowflake ingestion using stage and audit table | Completed |
| 22 | Automated Databricks Bronze ingestion using notebook and audit table | Completed |
| 23 | File validation and stronger ingestion audit for Snowflake and Databricks | Completed |
| 24 | Added batch ID parameters and reusable ingestion configuration | Completed |
| 25 | Reran Silver and Gold from automated Bronze and validated end-to-end outputs | Completed |
| 26 | Converted Snowflake SQL steps into stored-procedure style | Completed |
| 27 | Created Snowflake Task graph for stored-procedure orchestration | Completed |
| 28 | Converted Databricks SQL scripts into workflow-ready notebooks | Completed |
| 29 | Created Databricks Workflow with notebook task dependencies | Completed |
Add this section:

```markdown
## Version 2: Production Automation Foundation

Version 2 upgrades the project from manually executed SQL scripts into a more production-style pipeline.

### Version 2 Improvements

| Day | Improvement | Status |
|---:|---|---|
| 21 | Automated Snowflake ingestion using stage and audit table | Completed |
| 22 | Automated Databricks Bronze ingestion using notebook and audit table | Completed |
| 23 | File validation and stronger ingestion audit | Completed |
| 24 | Batch ID parameters and reusable ingestion configuration | Completed |
| 25 | End-to-end refresh validation from automated Bronze | Completed |
| 26 | Snowflake stored-procedure-style pipeline steps | Completed |
| 27 | Snowflake Task Graph orchestration | Completed |
| 28 | Databricks workflow-ready notebooks | Completed |
| 29 | Databricks Workflow orchestration | Completed |
| 30 | Version 2 runbook and orchestration comparison | Completed |


### Version 2 Architecture

```text
Automated Ingestion
→ File Validation
→ Batch Audit
→ Silver / Gold Transformations
→ DQ / Regression Tests
→ Snowflake Task Graph
→ Databricks Workflow
Version 2 Documentation
Document	Purpose
docs/version2_runbook.md	End-to-end Version 2 operating guide
docs/version2_architecture.md	Version 2 architecture explanation
docs/orchestration_comparison.md	Snowflake Task Graph vs Databricks Workflow comparison
docs/databricks_workflow_runbook.md	Databricks Workflow operations guide
docs/version2_milestone_summary.md	Version 2 milestone closure summary

```markdown
## Version 3: Streaming and Multiplex Bronze


| Day | Improvement | Status |
|---:|---|---|
| 31 | Designed Databricks landing zone for streaming-style ingestion | Completed |
| 32 | Implemented Auto Loader basic ingestion for customers | Completed |
| 33 | Generalized Auto Loader into Multiplex Bronze design | Completed |
| 34 | Added unified raw-payload Multiplex Bronze table with metadata | Completed |
| 35 | Designed streaming deduplication strategy and duplicate analysis | Completed |
| 36 | Implemented deduplicated Bronze payload table | Completed |
| 37 | Tested late-arriving data handling with raw and deduped Bronze | Completed |
| 38 | Validated streaming ingestion layer and created streaming runbook | Completed |

## Version 4: SCD Type 2 Dimensions

| Day | Improvement | Status |
|---:|---|---|
| 39 | Designed SCD Type 2 dimensions for customers and subscriptions | Completed |
| 40 | Built initial Customer SCD Type 2 dimension | Completed |
| 41 | Built initial Subscription SCD Type 2 dimension | Completed |
| 42 | Implemented SCD Type 2 merge/update logic | Completed |
| 43 | Tested customer and subscription SCD2 change scenarios | Completed |
| 44 | Connected SCD Type 2 dimensions to Customer 360 | Completed |
| 45 | Validated and documented full SCD Type 2 phase | Completed |

## Version 5: CDC and Change Data Feed

| Day | Improvement | Status |
|---:|---|---|
| 46 | Designed CDC / Change Data Feed and enabled CDF on key Delta tables | Completed |
| 47 | Generated CDC test changes after CDF enablement | Completed |
| 48 | Extracted and stored Change Data Feed records | Completed |
| 49 | Built CDC audit summaries and downstream change-processing pattern | Completed |
| 50 | Built CDC-driven current snapshot refresh pattern | Completed |
| 51 | Added CDC observability, data quality checks, and SLA monitoring | Completed |
| 52 | Validated and documented full CDC / Change Data Feed phase | Completed |

### CDC and Change Data Feed Milestone

Days 46–52 implemented CDC and Delta Change Data Feed, including CDF enablement, baseline tracking, post-CDF test changes, CDF extraction, CDC processing queue, CDC serving tables, CDC-driven current snapshot refresh, observability, SLA monitoring, validation, and runbook documentation.

## Version 6: Workflow Orchestration and Productionization

| Day | Improvement | Status |
|---:|---|---|
| 53 | Designed Databricks workflow orchestration DAG | Completed |
| 54 | Tested and refined Databricks workflow execution pattern | Completed |
| 55 | Added job run auditing and failure notification design | Completed |
| 56 | Added retry strategy, timeout rules, and workflow reliability settings | Completed |
| 57 | Added environment separation and deployment configuration | Completed |
| 58 | Validated and refined Databricks Bundle deployment structure | Completed |





