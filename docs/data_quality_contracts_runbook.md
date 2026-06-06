# Data Quality Contracts and Gates Runbook

## Project

Broadband Customer 360 & Churn Analytics

## Phase

Version 7: Production-grade Data Quality and Governance

---

# Purpose

This runbook explains the custom data quality contract and gate framework.

The goal is to move from scattered validation queries to centralized, reusable data quality rules.

---

# Main Flow

```text
DQ contract config
→ DQ check execution
→ DQ check results
→ quarantine candidates
→ DQ gate decision
→ validation
Main Tables
DQ Contract Config
dev_broadband.monitoring.data_quality_contract_config

Purpose:

stores DQ rule definitions
defines table, layer, business subject
defines severity
defines gate action
stores executable check SQL
DQ Check Results
dev_broadband.monitoring.data_quality_check_results

Purpose:

stores result of each contract
stores failed count
stores PASS / FAIL / ERROR status
DQ Gate Decision
dev_broadband.monitoring.data_quality_gate_decision

Purpose:

produces final gate decision
decides whether pipeline can continue
DQ Quarantine Candidates
dev_broadband.monitoring.data_quality_quarantine_candidates

Purpose:

stores rows or grouped keys that violate selected DQ contracts
supports debugging and remediation
Gate Status
Status	Meaning
PASS	No blocking or warning failures
WARN	Warning-level failures exist
BLOCK	Critical blocking failures exist
Severity
Severity	Meaning
CRITICAL	Breaks correctness; should block production downstream processing
HIGH	Important issue; should warn and be reviewed
MEDIUM	Useful monitoring issue
LOW	Informational issue
Gate Actions
Gate action	Meaning
BLOCK	Stop downstream production processing
WARN	Continue but alert/review
OBSERVE	Track only
QUARANTINE	Capture bad records for remediation
Current Contracts

The first DQ contracts cover:

Bronze row count
Bronze deduplication
one current customer SCD2 row per customer
one current subscription SCD2 row per subscription
current SCD2 rows must have null end date
Customer 360 current row count
Customer 360 duplicate subscription check
CDC queue metadata completeness
CDC health not RED
Operational Query

Latest gate:

SELECT *
FROM dev_broadband.monitoring.data_quality_gate_decision
ORDER BY gate_evaluated_at DESC;

Failed contracts:

SELECT *
FROM dev_broadband.monitoring.data_quality_check_results
WHERE check_status IN ('FAIL', 'ERROR')
ORDER BY severity, contract_id;

Quarantine candidates:

SELECT *
FROM dev_broadband.monitoring.data_quality_quarantine_candidates
ORDER BY quarantined_at DESC;
Relationship to Databricks Expectations

Databricks Lakeflow expectations define data quality constraints with SQL expressions and can warn, drop invalid records, or fail an update.

This project starts with a custom DQ contract framework because it works with the notebook/job architecture already built. Later, selected rules can be migrated into Lakeflow expectations or Delta constraints where appropriate.

Interview Explanation

I created a data quality contract framework. It centralizes DQ rules, executes them consistently, stores check results, captures quarantine candidates, and produces a gate decision of PASS, WARN, or BLOCK for production-style pipeline control.