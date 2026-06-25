
# Data Quality Summary

## Files Checked

- fund_master.csv
- nav_history.csv

## Dataset Shapes

- fund_master: (6, 5)
- nav_history: (19900, 7)

## Duplicate Rows

- fund_master duplicates: 0
- nav_history duplicates: 0

## Missing AMFI / Scheme Codes

- Total missing scheme codes: 0
- Missing codes: []

## Missing Values in fund_master

scheme_code        0
scheme_name        0
fund_house         0
scheme_category    0
scheme_type        0

## Missing Values in nav_history

date               0
nav                0
scheme_code        0
scheme_name        0
fund_house         0
scheme_category    0
scheme_type        0

## Summary

All scheme codes from fund_master were checked against nav_history.
Risk grade and sub-category were not available in the mfapi.in API response.
