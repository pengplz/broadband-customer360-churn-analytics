# GitHub Publishing Checklist

## Before Publishing

| Check                                   | Done |
| --------------------------------------- | ---- |
| README is complete                      | ☐    |
| Dashboard screenshots are visible       | ☐    |
| SQL scripts are organized               | ☐    |
| Documentation files are complete        | ☐    |
| Power BI file is included               | ☐    |
| `.gitignore` is correct                 | ☐    |
| No credentials are committed            | ☐    |
| No real company data is committed       | ☐    |
| No `.env` file is committed             | ☐    |
| No tokens or private keys are committed | ☐    |

## GitHub Repository Settings

| Item            | Recommended Value                                                                               |
| --------------- | ----------------------------------------------------------------------------------------------- |
| Repository name | `broadband-customer360-churn-analytics`                                                         |
| Visibility      | Public, if no credentials or real data                                                          |
| Description     | Broadband Customer 360 & Churn Analytics using Snowflake, Databricks, SQL, Python, and Power BI |
| Topics          | snowflake, databricks, sql, python, powerbi, data-engineering, customer-360, churn-analytics    |

## Final Security Search

Run this before pushing.

### Git Bash / Mac / Linux

```bash
grep -R "password" .
grep -R "secret" .
grep -R "token" .
grep -R "private key" .
grep -R "account" .
```

### PowerShell

```powershell
Select-String -Path .\* -Pattern "password" -Recurse
Select-String -Path .\* -Pattern "secret" -Recurse
Select-String -Path .\* -Pattern "token" -Recurse
Select-String -Path .\* -Pattern "private key" -Recurse
Select-String -Path .\* -Pattern "account" -Recurse
```

Normal documentation text is okay. Real credentials are not okay.

## Git Commands

After final review:

```bash
git status
git add .
git commit -m "Day 18 prepare resume LinkedIn and GitHub publishing"
```

If you have not connected GitHub yet:

```bash
git remote add origin https://github.com/YOUR_USERNAME/broadband-customer360-churn-analytics.git
git branch -M main
git push -u origin main
```

If remote already exists:

```bash
git push
```
