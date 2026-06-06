# Bundle Dev Deploy and Run Runbook

## Project

Broadband Customer 360 & Churn Analytics

## Purpose

This runbook explains how to deploy the Databricks Bundle to the dev target and run the bundled workflow.

---

# Target

```text
dev

Catalog:

dev_broadband
Command Sequence
1. Validate
databricks bundle validate -t dev
2. Preview plan
databricks bundle plan -t dev
3. Deploy
databricks bundle deploy -t dev
4. Summarize
databricks bundle summary -t dev
5. Run
databricks bundle run -t dev broadband_customer360_production_workflow

or:

databricks bundle run -t dev --params "catalog=dev_broadband,source_subject=ALL,reset_stream=false" broadband_customer360_production_workflow
Safety Rules
Deploy dev only today.
Do not deploy prod.
Keep reset_stream=false.
Keep schedule paused.
Evidence to Capture

From bundle summary:

Workspace host
Workspace user
Workspace path
Job name
Job URL

From bundle run:

Run status
Run URL or Job URL
Any failed task
Validation Notebook

After running the bundle workflow, run:

notebooks/36_bundle_dev_deploy_run_validation.py

This records:

deployment status
run status
output validation
SCD2 checks
CDC checks
observability checks
Common Issues
Bundle validation fails

Check:

databricks.yml
resources/environment_targets.yml
resources/jobs/broadband_customer360_workflow.yml
Duplicate resource error

The same job is probably defined in more than one YAML file.

Keep the job only in:

resources/jobs/broadband_customer360_workflow.yml
Run fails because notebook path is wrong

Compare YAML paths to actual Databricks Workspace paths.

CDF extraction returns no rows

This may be okay if no new changes occurred after the last extraction.

Auto Loader reprocesses files

Check that:

reset_stream=false
Interview Explanation

I deployed the Databricks Bundle to the dev target, ran the bundled workflow, captured deployment and run evidence, and validated that the orchestrated pipeline still produced expected Bronze, SCD2, Customer 360, CDC, and observability outputs.