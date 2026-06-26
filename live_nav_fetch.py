import requests
import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")
raw_path.mkdir(parents=True, exist_ok=True)

schemes = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

all_nav_data = []

for scheme_name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        meta = data["meta"]
        nav_data = data["data"]

        df = pd.DataFrame(nav_data)

        df["scheme_code"] = meta["scheme_code"]
        df["scheme_name"] = meta["scheme_name"]
        df["fund_house"] = meta["fund_house"]
        df["scheme_category"] = meta["scheme_category"]
        df["scheme_type"] = meta["scheme_type"]

        file_path = raw_path / f"{scheme_name}_nav.csv"
        df.to_csv(file_path, index=False)

        all_nav_data.append(df)

        print(f"{scheme_name} NAV saved successfully")
        print(df.head())
        print(df.shape)
        print("-" * 50)

    else:
        print(f"Failed to fetch {scheme_name}")
        print("Status code:", response.status_code)

combined_df = pd.concat(all_nav_data, ignore_index=True)

combined_file = raw_path / "five_key_schemes_nav.csv"
combined_df.to_csv(combined_file, index=False)

print("Combined NAV file saved successfully!")
print("Saved file:", combined_file)
print(combined_df.shape)