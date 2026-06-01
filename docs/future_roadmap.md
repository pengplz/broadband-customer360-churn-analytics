# Future Roadmap

## Purpose

This document lists future improvements for the Broadband Customer 360 & Churn Analytics project.

The current version is complete as a portfolio project, but these enhancements could make it more production-like.

---

## Phase 1: Automation Improvements

| Improvement | Value |
|---|---|
| Automate CSV ingestion | Reduce manual loading |
| Add Snowflake stored procedures | Make Snowflake pipeline easier to run |
| Add Snowflake Tasks | Schedule Snowflake pipeline |
| Add Databricks Workflows | Schedule Databricks pipeline |
| Deploy Databricks Asset Bundle | Improve deployment practice |

---

## Phase 2: Testing and CI/CD

| Improvement | Value |
|---|---|
| Add dbt tests | Strong analytics engineering practice |
| Add Great Expectations | More formal data quality framework |
| Add GitHub Actions | Automated validation on commit |
| Add SQL linting | Improve SQL quality |
| Add unit tests for Python generator | Improve fake data reliability |

---

## Phase 3: Dashboard Enhancements

| Improvement | Value |
|---|---|
| Add customer drill-through page | Let users inspect individual customers |
| Add province drill-through page | Better regional analysis |
| Add risk driver decomposition | Explain why customers are high risk |
| Add tooltip pages | Better dashboard usability |
| Add Power BI theme | More professional design |

---

## Phase 4: Churn Analytics Enhancement

| Improvement | Value |
|---|---|
| Add ML churn model | Improve risk prediction |
| Compare rule-based vs ML risk | Better analytics story |
| Add feature importance | Explain drivers of churn |
| Add retention campaign simulation | Connect analytics to business action |
| Add uplift modeling concept | Advanced customer targeting |

---

## Phase 5: Production Engineering

| Improvement | Value |
|---|---|
| Add alerting for DQ failures | Faster issue response |
| Add SLA monitoring | Better operational control |
| Add lineage screenshots | Strong governance story |
| Add access control design | Enterprise readiness |
| Add cost monitoring | Platform ownership mindset |

---

## Priority Roadmap

Recommended order:

1. Automate ingestion
2. Add full Databricks Workflow
3. Add Snowflake Tasks
4. Add Power BI customer drill-through
5. Add GitHub Actions validation
6. Add dbt or Great Expectations
7. Add ML churn model

## Final Note

The current version is already strong for a portfolio project.

The next improvements should focus on automation, CI/CD, and ML enhancement only after the current project is clearly documented and published.