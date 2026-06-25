import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(parents=True, exist_ok=True)

fund_master = pd.read_csv(RAW_DIR / "fund_master.csv")
nav_history = pd.read_csv(RAW_DIR / "nav_history.csv")

print("Fund Master Shape:", fund_master.shape)
print("NAV History Shape:", nav_history.shape)

print("\nFund Master Head:")
print(fund_master.head())

print("\nNAV History Head:")
print(nav_history.head())

print("\nFund Master Dtypes:")
print(fund_master.dtypes)

print("\nNAV History Dtypes:")
print(nav_history.dtypes)

# Validate AMFI / scheme codes
master_codes = set(fund_master["scheme_code"])
nav_codes = set(nav_history["scheme_code"])

missing_codes = master_codes - nav_codes

print("\nMissing Scheme Codes:")
print(missing_codes)

# Data quality checks
fund_master_missing = fund_master.isnull().sum()
nav_history_missing = nav_history.isnull().sum()

fund_master_duplicates = fund_master.duplicated().sum()
nav_history_duplicates = nav_history.duplicated().sum()

# Create summary report
report = f"""
# Data Quality Summary

## Files Checked

- fund_master.csv
- nav_history.csv

## Dataset Shapes

- fund_master: {fund_master.shape}
- nav_history: {nav_history.shape}

## Duplicate Rows

- fund_master duplicates: {fund_master_duplicates}
- nav_history duplicates: {nav_history_duplicates}

## Missing AMFI / Scheme Codes

- Total missing scheme codes: {len(missing_codes)}
- Missing codes: {list(missing_codes)}

## Missing Values in fund_master

{fund_master_missing.to_string()}

## Missing Values in nav_history

{nav_history_missing.to_string()}

## Summary

All scheme codes from fund_master were checked against nav_history.
Risk grade and sub-category were not available in the mfapi.in API response.
"""

with open(REPORT_DIR / "data_quality_summary.md", "w") as f:
    f.write(report)

print("\nData quality summary saved in reports/data_quality_summary.md")