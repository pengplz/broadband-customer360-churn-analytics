# Step 11 — Create Day 59 notes

Paste this into:

```text
docs/v6_day7_notes.md
# Version 6 Day 7 / Overall Day 59 Notes

## Goal

Deploy the Databricks Bundle to dev and run the bundled workflow.

## Completed

- Validated the Databricks Bundle for dev target
- Previewed the bundle deployment plan
- Deployed the bundle to dev
- Reviewed bundle summary
- Ran the bundled workflow manually
- Recorded deployment evidence
- Recorded bundled workflow run result
- Created dev deployment audit table
- Created dev workflow run audit table
- Created dev run output validation table
- Created bundle dev deployment runbook

## New Notebook

- `notebooks/36_bundle_dev_deploy_run_validation.py`

## New SQL

- `databricks_sql/v6_07_bundle_dev_deploy_run.sql`

## New Tables

- `dev_broadband.monitoring.bundle_dev_deployment_audit`
- `dev_broadband.monitoring.bundle_dev_workflow_run_audit`
- `dev_broadband.monitoring.bundle_dev_run_output_validation`

## Important Commands

```bash
databricks bundle validate -t dev
databricks bundle plan -t dev
databricks bundle deploy -t dev
databricks bundle summary -t dev
databricks bundle run -t dev broadband_customer360_production_workflow
Safety Rules
dev only
reset_stream=false
prod not deployed
schedule remains paused
Engineering Value

The project is no longer only local files and notebooks.

It is now deployable as a Databricks Bundle to the dev target and runnable as a bundled workflow.

Interview Note

I deployed the Databricks Bundle to dev and ran the bundled workflow. I captured deployment/run evidence and validated the outputs across Bronze, SCD2, Customer 360, CDC, serving, and observability layers.

Next Step

Day 60 will validate and document the full workflow orchestration and productionization phase.