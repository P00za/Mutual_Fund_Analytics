import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

nav = pd.read_csv(RAW_DIR / "nav_history.csv")

if "scheme_code" in nav.columns:
    nav.rename(columns={"scheme_code": "amfi_code"}, inplace=True)

nav["date"] = pd.to_datetime(nav["date"], dayfirst=True, errors="coerce")
nav["nav"] = pd.to_numeric(nav["nav"], errors="coerce")

nav = nav.dropna(subset=["date", "amfi_code"])
nav = nav.sort_values(["amfi_code", "date"])
nav = nav.drop_duplicates(subset=["amfi_code", "date"])

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()
nav = nav[nav["nav"] > 0]

nav.to_csv(PROCESSED_DIR / "nav_history_cleaned.csv", index=False)

print("nav_history cleaned successfully")
print(nav.shape)
print(nav.head())