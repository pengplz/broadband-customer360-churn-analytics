"""
Validate required repository structure for the Broadband Customer 360 Databricks bundle.

This script intentionally uses only the Python standard library.
It checks file/folder existence and obvious unsafe placeholder issues.
"""

from pathlib import Path
import sys


REQUIRED_FILES = [
    "databricks.yml",
    "resources/jobs/broadband_customer360_job.yml",
    ".github/workflows/databricks_bundle_ci.yml",
    "notebooks/01_bronze_ingestion.py",
    "notebooks/02_silver_cleaning.py",
    "notebooks/03_gold_active_new_churn.py",
    "notebooks/58_advanced_churn_mart_powerbi.py",
    "docs/cicd_github_actions_databricks_bundles_runbook.md",
    "docs/cicd_bundle_validation_deployment_hardening_runbook.md",
]

REQUIRED_DIRS = [
    "notebooks",
    "resources/jobs",
    ".github/workflows",
    "docs",
    "databricks_sql",
]

DANGEROUS_PATTERNS = [
    "dapi",                  # common Databricks PAT prefix pattern
    "DATABRICKS_TOKEN=",     # token should be in GitHub Secrets
    "password=",
    "private_key",
    "BEGIN PRIVATE KEY",
]


def main() -> int:
    repo_root = Path.cwd()
    errors = []
    warnings = []

    for folder in REQUIRED_DIRS:
        path = repo_root / folder
        if not path.exists() or not path.is_dir():
            errors.append(f"Missing required directory: {folder}")

    for file_path in REQUIRED_FILES:
        path = repo_root / file_path
        if not path.exists() or not path.is_file():
            errors.append(f"Missing required file: {file_path}")

    text_files_to_scan = [
        "databricks.yml",
        "resources/jobs/broadband_customer360_job.yml",
        ".github/workflows/databricks_bundle_ci.yml",
    ]

    for file_path in text_files_to_scan:
        path = repo_root / file_path
        if not path.exists():
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")

        for pattern in DANGEROUS_PATTERNS:
            if pattern.lower() in text.lower():
                errors.append(
                    f"Potential secret or unsafe pattern found in {file_path}: {pattern}"
                )

        if "DATABRICKS_HOST" in text and "secrets.DATABRICKS_HOST" not in text:
            warnings.append(
                f"{file_path} mentions DATABRICKS_HOST. Confirm it is read from GitHub Secrets."
            )

        if "DATABRICKS_TOKEN" in text and "secrets.DATABRICKS_TOKEN" not in text:
            warnings.append(
                f"{file_path} mentions DATABRICKS_TOKEN. Confirm it is read from GitHub Secrets."
            )

    print("Repository structure validation")
    print("=" * 40)

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nPASS: Required repository structure looks valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
