# Step 3 — Create `docs/lessons_learned.md`

Paste this:

```markdown
# Lessons Learned

## 1. Start with the Business Question

The most important lesson is that the project should start from business questions, not tools.

The key business questions were:

- How many customers are active?
- How many are new?
- How many churned?
- What revenue is impacted?
- Which customers are high-risk?
- Can the data be trusted?

This made the project easier to explain and more valuable.

## 2. Bronze/Silver/Gold Makes the Pipeline Clear

The Bronze/Silver/Gold architecture helped separate responsibilities:

| Layer | Responsibility |
|---|---|
| Bronze | Raw data and traceability |
| Silver | Cleaning and standardization |
| Gold | Business-ready reporting |
| Monitoring | Trust and reliability |

This structure made the project easier to maintain and explain.

## 3. Customer 360 Is More Than One Table

Customer 360 is not just joining data. It is creating a meaningful monthly customer view.

The table combines:

- Customer profile
- Subscription lifecycle
- Payments
- Usage
- Speed
- Trouble tickets
- Product adoption
- Customer status

This gives analysts and business users a single trusted view.

## 4. Churn Logic Must Be Time-Aware

Active, New, and Churn calculations depend heavily on date logic.

The most important logic was:

- Active: subscription active during the month
- New: subscription started in the month
- Churn: subscription ended in the month

Getting monthly snapshot logic correct is critical.

## 5. Data Quality Is Part of the Product

A pipeline is not complete just because Gold tables are created.

A reliable pipeline also needs:

- Row count checks
- Null key checks
- Duplicate checks
- Freshness checks
- PASS/WARNING/FAIL status
- Quarantine records

This makes the project more production-style.

## 6. Quarantine Handling Improves Trust

Instead of silently dropping bad records, quarantine tables make issues traceable.

Each bad record includes:

- Rule name
- Severity
- Error message
- Business key
- Original record payload

This improves debugging and communication with source-system owners.

## 7. Reconciliation Builds Confidence

Because the project was built in both Snowflake and Databricks, reconciliation was important.

Comparing row counts, KPI totals, revenue impact, and churn-risk distribution helped prove that both platforms produced consistent results.

## 8. Testing Protects the Pipeline

Regression tests help make sure future changes do not break business logic.

Useful tests included:

- Tables not empty
- Required keys not null
- Business keys unique
- Churn rate between 0 and 1
- Net Adds logic correct
- Revenue impact logic correct
- Valid risk levels

## 9. Power BI Should Tell a Story

The dashboard should not only show charts.

It should guide the user:

1. What happened?
2. Where did it happen?
3. Why might it have happened?
4. Who is at risk?
5. Can we trust the data?

## 10. Documentation Converts Work Into Portfolio Value

Documentation makes the project understandable.

The most useful documents were:

- Architecture
- Data dictionary
- Runbook
- Demo script
- Interview Q&A
- Resume story
- Reconciliation report
- Testing checklist

Good documentation helps recruiters and interviewers understand the value quickly.