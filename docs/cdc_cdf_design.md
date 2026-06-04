# CDC and Change Data Feed Design

## Project

Broadband Customer 360 & Churn Analytics

## Phase

Version 5: CDC and Change Data Feed

---

# Purpose

This document explains the CDC and Change Data Feed design for the project.

The goal is to track row-level changes from key Delta tables and prepare the project for incremental downstream processing.

---

# What Is CDC?

CDC means Change Data Capture.

CDC answers:

- What changed?
- When did it change?
- Was it inserted, updated, or deleted?
- Which downstream process should react?

---

# What Is Databricks Change Data Feed?

Change Data Feed, or CDF, is a Delta Lake feature that records row-level changes for a Delta table after CDF is enabled.

CDF change records include:

- changed row values
- change type
- commit version
- commit timestamp

---

# Why CDC / CDF Matters

Without CDF, downstream jobs often need to reprocess full tables.

With CDF, downstream jobs can process only changed rows.

This is useful for:

- incremental Customer 360 updates
- downstream serving tables
- audit tables
- ML feature refresh
- SCD2 monitoring
- event-driven analytics

---

# Tables in Scope

| Table | Use Case |
|---|---|
| `dev_broadband.gold.dim_customer_scd2` | Track customer dimension changes |
| `dev_broadband.gold.dim_subscription_scd2` | Track subscription dimension changes |
| `dev_broadband.gold.gold_customer_360_monthly_scd2` | Track monthly Customer 360 changes |
| `dev_broadband.gold.gold_customer_360_current_scd2` | Track current snapshot changes |

---

# CDF Enablement

CDF is enabled with:

```sql
ALTER TABLE table_name
SET TBLPROPERTIES (delta.enableChangeDataFeed = true);


CDC / CDF Config Table

Config table:

dev_broadband.monitoring.cdc_cdf_config

Purpose:

list CDF-enabled tables
define business subject
define primary keys
define natural keys
define change use case
track active status
Baseline Table

Baseline table:

dev_broadband.monitoring.cdc_cdf_table_baseline

Purpose:

capture current Delta table version at setup time
support future CDF reads from a known starting version
Example CDF Query
SELECT *
FROM table_changes(
    'dev_broadband.gold.dim_customer_scd2',
    10
);

The second argument is the starting Delta table version.

Important Design Rule

CDF only tracks changes after it is enabled.

So this phase works like this:

Day 46: enable CDF and capture baseline versions
Day 47: create new customer/subscription changes
Day 48: read CDF changes after the baseline
Day 49: build CDC audit and serving patterns
Relationship to SCD2

SCD2 stores historical dimension versions.

CDF captures the row-level table changes that occurred while maintaining those versions.

They are different but complementary.

Area	SCD2	CDF
Purpose	Store dimension history	Expose table-level changes
Output	Current and historical rows	Insert/update/delete change records
Best for	Point-in-time analytics	Incremental processing
Example	Customer moved province	Dimension row was inserted/updated
Interview Explanation

I enabled Change Data Feed on key Delta Gold tables so the project can track row-level inserts, updates, and deletes going forward. I also created a CDC/CDF config table and baseline table so future jobs can read changes incrementally from known table versions.

