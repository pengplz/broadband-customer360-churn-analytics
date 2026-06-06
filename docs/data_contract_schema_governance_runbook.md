# Data Contract Documentation and Schema Governance Runbook

## Project

Broadband Customer 360 & Churn Analytics

## Phase

Version 7: Production-grade Data Quality and Governance

---

# Purpose

This runbook explains how the project documents data contracts and governs schema changes.

The goal is to prevent silent schema drift from breaking downstream pipelines.

---

# Main Flow

```text
Unity Catalog information_schema.columns
→ data contract documentation
→ schema baseline
→ schema drift detection
→ schema change request
→ governance decision
Main Tables
Data Contract Documentation
dev_broadband.monitoring.data_contract_documentation

Purpose:

document contracted tables and columns
classify column roles
identify possible sensitive columns
assign business and technical owners
Schema Baseline
dev_broadband.monitoring.data_contract_schema_baseline

Purpose:

store expected schema state
compare future actual schemas against this baseline
Schema Drift Result
dev_broadband.monitoring.data_contract_schema_drift_result

Purpose:

detect added, removed, changed, or reordered columns
Schema Change Request
dev_broadband.monitoring.data_contract_schema_change_request

Purpose:

create review records for detected schema drift
assign owner and approval status
Schema Governance Decision
dev_broadband.monitoring.data_contract_schema_governance_decision

Purpose:

produce PASS / WARN / REVIEW / BLOCK decision for schema governance
Drift Types
Drift type	Meaning	Default action
COLUMN_ADDED	Column appears in actual schema but not baseline	REVIEW
COLUMN_REMOVED	Baseline column is missing from actual schema	BLOCK
DATA_TYPE_CHANGED	Column type changed	BLOCK
NULLABILITY_CHANGED	Nullability changed	REVIEW
COLUMN_ORDER_CHANGED	Ordinal position changed	WARN
Governance Status
Status	Meaning
PASS	No schema drift detected
WARN	Non-blocking schema drift detected
REVIEW	Owner review required
BLOCK	Blocking schema drift detected
Operational Query

Latest governance decision:

SELECT *
FROM dev_broadband.monitoring.data_contract_schema_governance_decision
ORDER BY decision_timestamp DESC;

Blocking drift:

SELECT *
FROM dev_broadband.monitoring.data_contract_schema_drift_result
WHERE governance_action = 'BLOCK'
ORDER BY full_table_name, column_name;

Change requests:

SELECT *
FROM dev_broadband.monitoring.data_contract_schema_change_request
ORDER BY created_at DESC;
How to Approve a Schema Change

Example:

UPDATE dev_broadband.monitoring.data_contract_schema_change_request
SET
    request_status = 'APPROVED',
    approved_at = current_timestamp(),
    resolution_notes = 'Approved new optional column for downstream analytics.'
WHERE schema_change_request_id = '<request_id>';

After approval, update the baseline intentionally.

Why This Matters

Schema drift can break pipelines even when row counts and DQ checks look okay.

Examples:

source adds new column
source removes a column
data type changes from integer to string
nullable column becomes not nullable
key column changes unexpectedly

This framework makes schema changes visible and reviewable.

Interview Explanation

I added schema governance to the data quality framework. The project now documents contracted table schemas from Unity Catalog metadata, captures schema baselines, detects schema drift, creates schema change requests, assigns owners, and produces a PASS/WARN/REVIEW/BLOCK governance decision.