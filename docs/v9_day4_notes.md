# Step 6 — Create Day 79 notes

Create:

```text
docs/v9_day4_notes.md

Paste this:

# Version 9 Day 4 / Overall Day 79 Notes

## Goal

Create churn segmentation for high-risk, revenue-risk, win-back, retention, nurture, and monitoring groups.

## Completed

- Created churn segmentation notebook
- Reused `dev_broadband.advanced_churn` schema
- Created segmentation rule config
- Created subscription segment assignment table
- Created segment summary table
- Created campaign recommendation table
- Created dashboard summary table
- Created validation table
- Created SQL validation file
- Created churn segmentation runbook

## New Notebook

```text
notebooks/57_churn_segmentation.py
New SQL
databricks_sql/v9_04_churn_segmentation.sql
Output Schema
dev_broadband.advanced_churn
New Tables
dev_broadband.advanced_churn.churn_segmentation_rule_config
dev_broadband.advanced_churn.churn_subscription_segment_assignment
dev_broadband.advanced_churn.churn_segment_summary
dev_broadband.advanced_churn.churn_segment_campaign_recommendation
dev_broadband.advanced_churn.churn_segment_dashboard_summary
dev_broadband.advanced_churn.churn_segmentation_validation
Engineering Value

The project now converts churn risk scoring into campaign-ready business segments.

Instead of only showing a churn risk score, the project can tell the business which customers should go into retention save, revenue-risk, win-back, nurture, or monitoring campaigns.

Interview Note

I created churn segmentation that turns risk scoring into business action. It assigns every subscription to a segment, calculates customer value tier, identifies primary risk reason, creates campaign recommendations, and produces a dashboard-ready segmentation summary.